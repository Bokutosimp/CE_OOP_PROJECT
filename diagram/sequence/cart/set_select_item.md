```mermaid
---
config:
  theme: dark
  look: classic
---

sequenceDiagram
    actor User
    participant UI
    participant System
    participant Customer
    participant Cart
    participant ItemInCart
    participant Item
    User ->>  UI: set_selected(item_id,select,session)
    activate UI
    activate System
    loop Find user by ID
        alt User found
            System->>Customer: get_user_by_id(user_id)
            activate Customer
            Customer-->>System: return user
            deactivate Customer
        else User not found
            System-->>UI: raise Exception('user not found')
        end
    end
    loop Find item by ID
        alt Item found
            System->>Item: get_item_by_id(item_id)
            activate Item
            Item-->>System: return item
            deactivate Item
        else Item not found
            System-->>UI:item not found
        end
    end
    System ->> Customer: set_select_item(item,select)
    activate Customer
    Customer ->> Cart: get_list_item_in_cart
    activate Cart
    Cart -->> Customer: return list item in cart
    Customer ->> Customer: loop list item in cart which match with item
    alt find match item
        Customer ->> Cart: set_select_item(index,select)
        Cart -->> Customer: success
        Customer ->> System :success
    else not found match item
        Customer -->> System: item not found in cart
    end
    deactivate Cart
    deactivate Customer
    System -->> UI : response message

    deactivate System
    UI --> User: response message
    deactivate UI

```
