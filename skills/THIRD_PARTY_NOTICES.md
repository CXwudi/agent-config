# Third-Party Notices

This file is the single source of truth for third-party provenance, version
pinning, attribution links, and license notices for ported skills.

## obra/superpowers

- Repository: `https://github.com/obra/superpowers`
- Version used here: `v5.0.2`
- License: `MIT License`
- License file:
  `https://github.com/obra/superpowers/blob/v5.0.2/LICENSE`

These local skills are adapted derivatives of `obra/superpowers` skills.
Per-skill `attribution.md` files record file-level provenance and local
adaptation notes.

| Local skill | Local attribution | Upstream | Version | License | Notes |
| --- | --- | --- | --- | --- | --- |
| [`brainstorming`](brainstorming/SKILL.md) | [attribution](brainstorming/attribution.md) | `obra/superpowers` | `v5.0.2` | `MIT` | Local paths; generic wording |
| [`writing-plans`](writing-plans/SKILL.md) | [attribution](writing-plans/attribution.md) | `obra/superpowers` | `v5.0.2` | `MIT` | Merged local `plan` behavior |
| [`dispatching-parallel-agents`](dispatching-parallel-agents/SKILL.md) | [attribution](dispatching-parallel-agents/attribution.md) | `obra/superpowers` | `v5.0.2` | `MIT` | Generic dispatch wording |

## ast-grep/agent-skill

- Repository: `https://github.com/ast-grep/agent-skill`
- Version used here: `577f4d4507678f2c8cee150fae25e6ce309f70b1`
- License used here: `MIT License`
- License source:
  `https://github.com/ast-grep/ast-grep/blob/30401c0ec6f42e01730bc3c6fa0cf3f00beb4c96/LICENSE`

These local skills are adapted derivatives of `ast-grep/agent-skill`.
The upstream skill repository does not currently bundle a standalone license
file. Its README says the skill follows ast-grep's MIT license for included
documentation and examples, so this repo records the MIT license text from
`ast-grep/ast-grep` as the notice source for the vendored material.

| Local skill | Local attribution | Upstream | Version | License | Notes |
| --- | --- | --- | --- | --- | --- |
| [`ast-grep`](ast-grep/SKILL.md) | [attribution](ast-grep/attribution.md) | `ast-grep/agent-skill` | `577f4d4507678f2c8cee150fae25e6ce309f70b1` | `MIT` via `ast-grep/ast-grep` | Added local frontmatter metadata and pinned provenance |

## License Text

### MIT License: obra/superpowers

```text
MIT License

Copyright (c) 2025 Jesse Vincent

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### MIT License: ast-grep/ast-grep

```text
MIT License

Copyright (c) 2022 Herrington Darkholme

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
