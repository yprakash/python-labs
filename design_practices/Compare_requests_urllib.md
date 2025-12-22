# Compare: requests vs urllib
## Overview
Python provides multiple HTTP-related libraries. Two of the most commonly encountered are:
- `requests`
- `urllib` (standard library)

This document explains **why modern Python architectures use both**, instead of choosing one exclusively.

---
## Library Responsibilities
### requests
`requests` is optimized for **human-friendly HTTP interactions**.

Strengths:
- Simple, expressive API
- Automatic connection pooling
- Easy headers, cookies, sessions
- Excellent error handling
- Ideal for APIs and scraping

Limitations:
- Does not implement crawling standards
- No native `robots.txt` support
- No URL policy enforcement

---
### urllib
`urllib` is optimized for **protocol correctness and standards**.

Strengths:
- Part of Python standard library
- Implements RFC-compliant components
- Includes `robotparser` for robots.txt
- URL parsing, joining, normalization

Limitations:
- Verbose API
- Poor ergonomics for HTTP requests
- Not suitable for large-scale fetching

---
## The Best-of-both-Worlds Approach
Modern, well-architected systems use:

| Responsibility | Library |
|--------------|--------|
| HTTP transport | `requests` |
| Session reuse | `requests.Session` |
| robots.txt parsing | `urllib.robotparser` |
| URL parsing | `urllib.parse` |
| HTML parsing | `BeautifulSoup` |

Each tool does **one thing well**.

---
## Why Not Use Only requests?
Because crawling is not just HTTP.

Crawling also involves:
- Robots exclusion rules
- Per-origin policies
- User-Agent–specific permissions

`requests` deliberately avoids these concerns.

---
## Why Not Use Only urllib?
Because ergonomics matter.

`urllib.request`:
- is verbose
- lacks session management
- is harder to test
- is less readable

For real-world systems, this increases maintenance cost.

---
## Example Architecture
```text
URL
 ├─ urllib.parse        → normalize, extract origin
 ├─ urllib.robotparser  → check can_fetch()
 ├─ requests.Session    → fetch content
 └─ BeautifulSoup       → extract text
```
This separation:
- improves correctness
- improves testability
- reduces bugs
- matches browser + crawler standards

---
## Architectural Principle
> Use libraries for their intended responsibility, not convenience.

This avoids:
- reimplementing standards
- protocol bugs
- long-term maintenance debt

---
## Summary
- `requests` is for transport
- `urllib` is for rules and structure
- Combining them is not a hack — it is **good design**

This pattern scales from:
- simple scripts
- to production-grade crawlers
- to AI and non-AI pipelines alike
