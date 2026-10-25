# Cua Driver Testing Findings on Windows

## 1. Daemon Startup Delay After `autostart kick`

Running `cua-driver autostart kick` triggers the `cua-driver-serve` Scheduled Task via a hidden PowerShell wrapper (`Start-Process cua-driver.exe serve`). Checking `cua-driver status` immediately after `autostart kick` can briefly report `not running` while the child process initializes. Waiting about 1 second before checking status resolves this.

## 2. UWP App Handle in `run_script`

On Windows 11, UWP apps such as Calculator are hosted under `ApplicationFrameHost.exe`. In `run_script`, `cua.launch()` already returns the bound app handle directly:

```javascript
const app = await cua.launch({
  aumid: "Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
});
```

Calling `await cua.getApp("Calculator")` after `cua.launch()` fails because the window owner process is `ApplicationFrameHost.exe` rather than `Calculator`.

## 3. Single-Instance Browser Handoff (`launch_app` Timeout)

When launching a browser such as Brave (`brave.exe`) while background tray or helper processes are already running, `cua-driver launch_app` may time out even though the browser window opens on screen. The newly spawned `brave.exe` PID delegates window creation to the existing master `brave.exe` process and exits immediately.

Workaround:

1. Call `cua-driver list_windows` after launching to locate the active `brave.exe` `pid` and `window_id`.
2. Target that existing `pid` and `window_id` in subsequent calls.

## 4. Chromium Extension Popups and Focus Restoration

### Why Window-Scoped `foreground` Clicks Close Extension Popups

Clicking a browser toolbar extension icon (such as Bitwarden) requires a real input event because Chromium ignores synthetic background clicks (`ExpandCollapse.Expand` fails).

However, using a window-scoped click with `delivery_mode: "foreground"` (`element_token` + `pid` + `window_id`) wraps the click in a focus-restore guard:

1. `cua-driver` records `prior_fg_hwnd` (the main browser window HWND).
2. `cua-driver` sends `SendInput` at the extension icon coordinates.
3. Chromium opens the extension popup as a separate popup HWND, which takes foreground focus.
4. `cua-driver` immediately calls `SetForegroundWindow(prior_fg_hwnd)` to restore focus to the main browser window, which steals focus from the popup HWND and causes Chromium to immediately dismiss the popup.

### Two Working Solutions

#### Option A: Desktop-Scoped Click (Keeps the Native Popup Open)

Keep the browser in the foreground, take a desktop capture (`get_desktop_state`), and click using `scope: "desktop"` with screen coordinates:

```powershell
(@{
  session = "bw"
  scope = "desktop"
  capture_id = $desktopState.capture_id
  x = 2424
  y = 95
} | ConvertTo-Json -Compress) | cua-driver click
```

With `scope: "desktop"`, `cua-driver` sets `delivery.mode = "not_applicable"` and does not run the post-click `SetForegroundWindow` restore. The popup stays open and its UIA tree appears under `get_window_state` on the browser window (`Document "Bitwarden"`).

#### Option B: Open the Extension Popup URL in a Tab

Navigate a browser tab directly to the extension popup URL:

```text
chrome-extension://nngceckbapebfimnlniiiahkandclblb/popup/index.html
```

Because it renders inside a standard tab, it never closes on focus changes and works reliably with background UIA inspection and `set_value`.

## 5. Background vs. Foreground Input Routing in Chromium

- `get_window_state` and `set_value` (UIA `ValuePattern.SetValue`) work in background mode without stealing focus, including for the browser address bar and web form inputs.
- Commit actions on Chromium surfaces (`press_key "return"`, `hotkey`, and clicking web buttons) are ignored on the background `PostMessage` path and require `delivery_mode: "foreground"`.

## 6. When handling sensitive envrionment variables

For example, when you want to enter the `OPENAI_API_KEY` into some password textfield without exposing it to logs or LLM context,
You can read `$env:OPENAI_API_KEY` inside PowerShell and pipe the JSON payload directly to `cua-driver set_value`, this should not print the variable.
