sequenceDiagram
autonumber

    actor User
    participant UI
    participant System
    participant Category

    User ->> UI: get_categories(query)
    activate UI
    UI ->> System: get_categories(query)
    activate System
    System ->> System : find categories by query
    System ->> Category : get_category
    activate Category
    Category ->> System : return category
    deactivate Category
    System ->> UI: return filtered_categories
    deactivate System
    UI ->> User: return filterd_categories
    deactivate UI
