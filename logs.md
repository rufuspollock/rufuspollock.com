---
title: Daily Logs
syntaxMode: mdx
---

```base
filters:
  file.inFolder("logs")
views:
  - type: list
    name: "Daily Logs"
    order:
      - file.name
    sort:
      - property: file.name
        direction: DESC
```
