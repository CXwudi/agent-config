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