---
name: web-search-and-crawl
description: Agent Skill for web search and crawl. Use when you want to search the web for anything, or read a webpage
---

# Web Search and Crawl

This is a combination of 3 skills:

- [`exa`](./exa/SKILL.md)
- [`jina`](./jina/SKILL.md)
- [`bocha`](./bocha/SKILL.md)

When to use which:

- `exa` for:
    - Default choice for web search
    - Can also do web crawl 
- `jina` for:
    - Default choice for web crawl
    - Can also do web search
- `bocha` for:
    - For searching contents likely from Chinese Internet (xiaohongshu, bilibili, weibo, etc.)


Otherwise, consider `use-browser` skill
