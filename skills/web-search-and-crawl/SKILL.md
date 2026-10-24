---
name: web-search-and-crawl
description: Agent Skill for web search and crawl. Use when you want to search the web for anything, or read a webpage
---

# Web Search and Crawl

This is a combination of 3 skills:

- [`exa`](./exa/SKILL.md)
- [`jina`](./jina/SKILL.md)
- [`bocha`](./bocha/SKILL.md)
- [`deepseek-search-and-crawl`](./deepseek-search-and-crawl/SKILL.md)

When to use which:

- `exa` for:
    - Default choice for web search
    - Can also do web crawl 
- `jina` for:
    - Default choice for web crawl
    - Can also do web search
- `bocha` for:
    - For searching contents likely from Chinese Internet (xiaohongshu, bilibili, weibo, etc.)
- `deepseek-search-and-crawl` for:
    - Another search and crawl option for Chinese Internet
    - If `bocha` failed to find, try this one. Likewise, if `deepseek-search-and-crawl` failed to find, try `bocha`.
    - Is also the only crawl option for Chinese Internet.

Otherwise, consider `use-browser` skill
