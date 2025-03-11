sequenceDiagram
autonumber

    actor Customer
    participant UI
    participant System

    Customer ->> UI: search_item(query)
    activate UI
    UI ->> System: search_item(query)
    activate System
    System -->> UI: show results
    deactivate System
    UI -->> Customer: display search results
    deactivate UI
