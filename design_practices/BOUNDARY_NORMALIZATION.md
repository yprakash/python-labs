# Boundary Normalization

Boundary Normalization is a design practice for isolating external systems
(SDKs, APIs, vendors, services) from the rest of your codebase by translating
their concepts into **your own stable, internal representations**.

---
## What Is a Boundary?
A **boundary** is any place where your code talks to something you do not control.

Examples:
- Third-party SDKs (OpenAI, AWS, Stripe)
- External HTTP APIs
- Databases and drivers
- Message queues
- OS / filesystem calls

Anything outside your repo is *foreign territory*.

---
## What Does “Normalization” Mean?
> Convert foreign concepts at the boundary into local, intentional concepts before they enter your system.

You do **not** let raw external ideas flow inward.

---
## Why This Exists
External systems:
- change faster than your code
- evolve without your consent
- have their own terminology
- expose transport-level details you don’t care about

If you let those details leak inward:
- every caller becomes coupled to them
- refactors become global
- vendor changes become breaking changes

Boundary Normalization stops that spread.

---
## Exception Normalization (the familiar example)
### Without normalization
```python
from openai import RateLimitError

def do_something():
    call_openai()
```
Callers must now know:
- OpenAI exists
- its exception hierarchy
- which errors are retryable

OpenAI is no longer a dependency — it is part of your architecture.

---
### With normalization
Platform layer:
```python
def call_external():
    try:
        ...
    except BadRequestError as e:
        raise ValueError("Invalid request parameters sent to ...") from e
    except RateLimitError as e:
        raise RuntimeError("Temporary capacity issue") from e
```
Callers:
```python
def do_something():
    call_external()
```
Now callers reason in your domain, not the vendor’s. Callers now only see:
- `ValueError` for bad input
- `RuntimeError` for transient issues
- no knowledge of OpenAI (external system)
- no coupling to OpenAI’s exception hierarchy
- no knowledge of retryability
- no coupling to OpenAI’s retry policies
- no knowledge of OpenAI’s existence at all

---
## Boundary Normalization Is Broader Than Exceptions
Exceptions are just the most visible case.

The same rule applies to the following.

### 1. Data Shape Normalization
#### Bad (leaks vendor schema)
```python
response = openai_client.responses.create(...)
return response.output[0]["content"][0]["text"]
```
Callers now depend on:
- OpenAI response layout
- index positions
- SDK internals

#### Good (normalized shape)
```python
return response.output_text
```
Or:
```python
return {
    "text": response.output_text,
    "tokens": response.usage.total_tokens,
}
```
Callers see your data contract, not theirs.

---
### 2. Enum / Constant Normalization
#### Bad
```python
if error.code == "rate_limit_exceeded":
    ...
```
Vendor strings leak everywhere.
#### Good
```python
class LLMErrorType(Enum):
    RATE_LIMIT = "rate_limit"
    INVALID_INPUT = "invalid_input"
```
Boundary maps vendor codes → internal enums.

---
### 3. Transport → Semantic Errors
External systems speak in:
- HTTP status codes
- SDK-specific exceptions
- retry headers

Your system should speak in:
- configuration errors
- transient failures
- permission issues

Example mapping:

| Vendor Detail | Normalized Meaning               |
| ------------- | -------------------------------- |
| 400           | Invalid input                    |
| 401           | Misconfigured credentials        |
| 429           | Retryable capacity issue         |
| 5xx           | Temporary infrastructure failure |

---
### 4. Timeouts and Retries
#### Bad
```python
client.responses.create(timeout=30)
```
Timeout policy is now baked into every call.
#### Good
```python
call_external(timeout=DEFAULT_TIMEOUT)
```
Boundary owns:
- timeout defaults
- retry classification
- backoff strategy (if any)

Callers only choose _intent_, not mechanics.

---
### 5. Vendor Feature Containment
New SDK features should be:
- absorbed
- hidden
- selectively exposed

Example:
- tool calls
- reasoning tokens
- multimodal outputs

If exposed directly, you commit to them forever.

Boundary Normalization lets you expose only what is stable and intentional.

---
## What Boundary Normalization Is NOT
- It is not over-engineering
- It is not about hiding errors
- It is not about losing information

Proper normalization preserves diagnostics internally (`raise X from e`) while presenting a clean surface.

---
## When You Can Skip It
You may skip normalization if **all** are true:
- one-off script
- single call site
- short-lived code
- vendor lock-in is acceptable

If the code is shared or long-lived, skipping it is technical debt.

---
## Mental Model
Treat external systems like:
- unreliable
- unstable
- foreign protocols

Your boundary is a **custom adapter** that translates their language into yours.

---
## One-Sentence Rule
**Foreign concepts stop at the boundary. Only normalized concepts are allowed inside.**

---
