---
name: commit
description: Safely handles the git commit process. Uses when asked for doing git commit. Smartly groups changes into single or multiple commits, drafts messages with gitmoji, and includes detailed bodies for larger changes.
---

# Commit Skill

This skill handles the git commit workflow with a focus on logical grouping and clear documentation.

## Workflow

1. **Analyze State**
    * Run `git status` to identify all untracked, modified, and deleted files.
    * Run `git diff` (unstaged) and `git diff --cached` (staged) to examine the actual code changes.

2. **Group Changes (Crucial Step)**
    * **Analyze the purpose** of changes across all files.
    * **Decision**:
        * *Single Commit*: If all changes are small or serve a single purpose (e.g., "fix login bug" involved 3 files), keep them together.
        * *Multiple Commits*: If changes cover distinct, unrelated tasks (e.g., "update documentation" AND "refactor database code"), split them into separate commits.
    * *Plan*: If multiple commits are needed, list which files go into which commit.

3. **Draft Commit Messages**
    For each identified commit group:
    * **Header**: `gitmoji <type>(<scope>): <subject>`
        * **Gitmoji**: Use the [Gitmoji Guide](https://gitmoji.dev/) (e.g., ✨ for features, 🐛 for bugs, ♻️ for refactor, 📝 for docs).
        * **Type**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`.
        * **Subject**: Imperative mood, concise.
    * **Body (Optional/Context-Dependent)**:
        * *Small/Simple changes*: No body or 1-2 sentences explaining *why*.
        * *Large/Complex changes*: Use a bulleted list to detail specific changes.

4. **Execute Commits**
    For each group:
    1. `git add <specific_files>` (Do not lazy use `git add .` unless all changes truly belong to one commit).
    2. `git commit -m "header" -m "body"`
    3. Verify success.

## Important Rules

* **NEVER** commit secrets, API keys, or `.env` files.
* **Atomic Commits**: Prefer smaller, focused commits over giant "dump" commits.
* **Verification**: Always run `git status` after operations to ensure the working directory state is what you expect.

## Examples

**Scenario 1: Mixed Changes**

* *Changes*: `auth.py` (bug fix), `README.md` (typo fix).
* *Action*: Split into two commits.
    1. `git add auth.py` -> `git commit -m "🐛 fix(auth): resolve token expiration issue"`
    2. `git add README.md` -> `git commit -m "📝 docs: fix typo in installation guide"`

**Scenario 2: Large Feature**

* *Changes*: 5 files related to a new "Dark Mode".
* *Action*: Single commit.
  * Title: `✨ feat(ui): implement dark mode theming`
  * Body:

        ```text
        - Add theme context provider
        - Update color palette in tailwind config
        - Add toggle switch to settings page
        - Fix contrast issues on dashboard
        ```
