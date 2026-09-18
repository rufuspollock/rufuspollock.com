---
title: Changelog
syntaxMode: mdx
---

Weekly log of what shipped across my projects.

```base
filters:
  file.inFolder("changelog")
views:
  - type: list
    name: "Changelog"
    order:
      - file.name
    sort:
      - property: file.name
        direction: DESC
```
