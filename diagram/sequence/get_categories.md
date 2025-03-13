```mermaid
---
config:
  theme: dark
  look: classic
---

sequenceDiagram
autonumber

    actor User
    participant UI
    participant System

    User ->> UI: get_categories()
    activate UI
    UI ->> System: get_categories()
    activate System

    System -->> UI: return all categories


    deactivate System
    UI -->> User: return filtered_categories
    deactivate UI
```
