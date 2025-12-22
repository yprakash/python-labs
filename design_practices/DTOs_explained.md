# DTOs Explained: TextDocument and Boundary Design
## What Is a DTO?
A Data Transfer Object (DTO) is a simple, structured object used to move data
between parts of a system without embedding behavior or business logic.

DTOs exist to:
- stabilize interfaces
- reduce coupling
- make pipelines explicit
- prevent accidental dependency leaks

---
## Why `TextDocument` Exists
Without a DTO, systems pass around:
- raw strings
- tuples
- dictionaries with implicit meaning

This leads to:
- unclear ownership
- missing metadata
- fragile integrations
- undocumented assumptions

`TextDocument` defines a **single canonical shape** for text.

---
## What `TextDocument` Represents
A `TextDocument` represents:
- the textual payload
- its origin
- when it was fetched or produced
- contextual metadata

It does NOT represent:
- how it was scraped
- how it will be summarized
- how it will be stored
- how AI models consume it

---
## Minimal Fields Explained

| Field | Purpose |
|---|---|
| `source` | Traceability, deduplication |
| `title` | Human readability |
| `text` | Core payload |
| `fetched_at` | Auditing, cache control |
| `metadata` | Safe extensibility |

---
## Immutability and Safety
`TextDocument` is immutable (`frozen=True`).

Benefits:
- prevents hidden side effects
- simplifies reasoning
- enables safe reuse
- makes pipelines deterministic

Transformations return **new instances**, not mutations.

---
## Boundary Normalization
DTOs enforce **boundary normalization**.

This means:
- upstream modules decide data shape
- downstream modules consume without assumptions
- SDKs, frameworks, and libraries do not leak across boundaries

Scrapers produce `TextDocument`.
Consumers depend only on `TextDocument`.

---
## Used in:
- ETL pipelines
- search engines
- document processing
- logging systems
- distributed architectures

LLMs consume documents; they did not invent them.

---
## Architectural Principle
> Stable data contracts outlive implementations.

DTOs are how you enforce that principle in Python.
