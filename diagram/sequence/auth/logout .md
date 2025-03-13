```mermaid
---
config:
  theme: dark
  look: classic
---

sequenceDiagram
    actor User
    participant UI
    User ->> UI: logout()
    UI -->> User: remove user session
```
