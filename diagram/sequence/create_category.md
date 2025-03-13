```mermaid
---
config:
  theme: dark
  look: classic
---

sequenceDiagram
autonumber

    actor Admin
    participant UI
    participant System
    participant Category

    Admin ->> UI: create_category(category_name,category_description,session)
    activate UI
    UI ->> System: category_category(id,name, description,admin_id)
    activate System

    System ->> System: validate_name()
    alt Successfully create category
        System -->> Category: create_category(id,name, description)
        activate Category
        Category -->> System: return success message
        deactivate Category
        System ->> UI: return success message
    else Duplicate category name
        System ->> UI: return error message
    end
    deactivate System
    UI ->> Admin : return response
    deactivate UI
```
