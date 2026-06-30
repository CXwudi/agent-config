# Push agent configs from this repo to their target locations.
# Accepts --clear flag for clean rsync with --delete.
[arg('clear', long, value='true', help='Remove dest files not in source (clean sync)')]
push clear='':
  #!/usr/bin/env bash
  set -euo pipefail

  if [ "{{clear}}" = "true" ]; then
    RSYNC_DELETE="--delete"
    echo "Pushing agent configs (clear mode)..."
  else
    RSYNC_DELETE=""
    echo "Pushing agent configs..."
  fi

  # Create target parent dirs
  mkdir -p ~/.pi/agent ~/.agents ~/.claude ~/.gemini/config ~/.codex

  # Push a source file or directory to a destination.
  push_item() {
    local src="$1"
    local dst="$2"

    if [ -d "$src" ]; then
      # Trailing slash: copy contents of src into dst (not src itself)
      mkdir -p "$dst"
      rsync -a $RSYNC_DELETE "$src"/ "$dst"/
      echo "  $src/ → $dst/"
    else
      mkdir -p "$(dirname "$dst")"
      rsync -a $RSYNC_DELETE "$src" "$dst"
      echo "  $src → $dst"
    fi
  }

  push_item prompts ~/.pi/agent/prompts
  push_item skills ~/.agents/skills
  push_item skills ~/.claude/skills
  push_item skills ~/.gemini/skills
  push_item prompts/AGENTS.md ~/.codex/AGENTS.md
  push_item prompts/AGENTS.md ~/.claude/CLAUDE.md
  push_item prompts/AGENTS.md ~/.gemini/config/AGENTS.md
  push_item prompts/AGENTS.md ~/.pi/agent/AGENTS.md

  echo "Push complete."

link-config-to-here:
  #!/usr/bin/env bash
  set -euo pipefail
  
  # Just runs from the project root by default, but we use $(pwd) to ensure 
  # we have an absolute path for clarity and to avoid any ambiguity.
  TARGET_DIR="$(pwd)/linked-agent-config"
  mkdir -p "$TARGET_DIR"
  echo "Creating symlinks in $TARGET_DIR..."

  # Function to create symlink
  create_link() {
    local source=$1
    local name=$2
    local target="$TARGET_DIR/$name"

    # Expand tilde if present
    source="${source/#\~/$HOME}"

    if [ -e "$source" ] || [ -d "$source" ]; then
        echo "Linking $name -> $source"
        ln -sfn "$source" "$target"
    else
        echo "Warning: Source $source does not exist. Skipping $name."
    fi
  }

  # 1. ~/.claude.json
  create_link "$HOME/.claude.json" ".claude.json"

  # 2. ~/.claude/
  create_link "$HOME/.claude" ".claude"

  # 3. ~/.agents/
  create_link "$HOME/.agents" ".agents"

  # 4. ~/.codex/
  create_link "$HOME/.codex" ".codex"

  # 5. ~/.gemini (Gemini CLI & Antigravity CLI)
  create_link "$HOME/.gemini" ".gemini"

  # 6. ~/.pi (Pi Coding Agent)
  create_link "$HOME/.pi" ".pi"

  # 7. ~/.config/opencode (Opencode)
  create_link "$HOME/.config/opencode" "opencode"

  create_link "$HOME/.config/mise/config.toml" "mise_config.toml"

  # 8. Cline MCP settings json
  # Using the path found in .vscode-server
  CLINE_SETTINGS="$HOME/.vscode-server/data/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json"
  # Fallback for local vscode if server path fails
  if [ ! -e "$CLINE_SETTINGS" ]; then
    CLINE_SETTINGS="$HOME/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json"
  fi
  create_link "$CLINE_SETTINGS" "cline_mcp_settings.json"

  echo "Symlink creation complete."
