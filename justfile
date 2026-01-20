setup-link:
  #!/usr/bin/env bash
  set -euo pipefail
  echo "Setting up symbolic links..."
  mkdir -p ${HOME}/.config/opencode
  mkdir -p ${HOME}/.claude
  mkdir -p ${HOME}/.gemini
  mkdir -p ${HOME}/.codex
  ln -sfn $(pwd)/agents ${HOME}/.config/opencode/agents
  ln -sfn $(pwd)/prompts ${HOME}/.config/opencode/prompts
  ln -sfn $(pwd)/skills ${HOME}/.claude/skills # This also cover opencode
  ln -sfn $(pwd)/skills ${HOME}/.gemini/skills
  ln -sfn $(pwd)/skills ${HOME}/.codex/skills
  echo "Symbolic links set up successfully."

reset-link:
  #!/usr/bin/env bash
  set -euo pipefail
  echo "Resetting symbolic links..."
  rm -f ${HOME}/.config/opencode/agents
  rm -f ${HOME}/.config/opencode/prompts
  rm -f ${HOME}/.claude/skills
  rm -f ${HOME}/.gemini/skills
  rm -f ${HOME}/.codex/skills
  echo "Symbolic links reset successfully."

link-config:
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

  # 3. ~/.codex/
  create_link "$HOME/.codex" ".codex"

  # 4. ~/.gemini (Gemini CLI)
  create_link "$HOME/.gemini" ".gemini"

  # 5. ~/.config/opencode (Opencode)
  create_link "$HOME/.config/opencode" "opencode"

  # 6. Cline MCP settings json
  # Using the path found in .vscode-server
  CLINE_SETTINGS="$HOME/.vscode-server/data/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json"
  # Fallback for local vscode if server path fails
  if [ ! -e "$CLINE_SETTINGS" ]; then
      CLINE_SETTINGS="$HOME/.config/Code/User/globalStorage/saoudrizwan.claude-dev/settings/cline_mcp_settings.json"
  fi
  create_link "$CLINE_SETTINGS" "cline_mcp_settings.json"

  echo "Symlink creation complete."