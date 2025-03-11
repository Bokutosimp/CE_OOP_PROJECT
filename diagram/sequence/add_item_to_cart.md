sequenceDiagram
autonumber

    actor Customer
    participant UI
    participant System
    participant User
    participant Item
    participant Cart
    participant ItemInCart

    Customer ->> UI: add_to_cart(item_id,user_id, quantity)
    activate UI
    UI ->> System: add_to_cart(ite_id,user_id, quantity)
    activate System
    System ->> System : get_user_by_id(user_id)
    alt find user
    System ->> User: get_id
    activate User
    User -->> System: user instance
    deactivate User
    else user not found
    System -->> UI : not found
    end
    System ->> System :get_item_by_id(item_id)
    alt find item
    System ->> Item: get_item
    activate Item
    Item -->> System:item instance
    deactivate Item
    else not found
    System -->> UI : not found
    end
    alt quantity > 0
    System ->> User: add_to_cart(item,quantity)
    activate User
    alt
    User ->> Item : check_availability
    activate Item
    Item ->> Cart: get_list_item_in_cart
    Cart ->> Cart : check if item already in cart
    alt item already in cart
    Cart ->> ItemInCart : set_amount_in_cart
    ItemInCart -->> Cart : success add item to cart
    else item not in cart
    Cart -->> ItemInCart : create item in cart
    ItemInCart -->> Cart : success create item in cart
    end
    Cart -->> Item: response message
    Item -->> User: response message
    else
    Item -->> User : item out of stock
    end
    deactivate Item
    User -->> System: response message
    else quantity < 0
    User -->> System: invalid quantity
    deactivate User
    end
    deactivate System
    System -->> UI : reponse message
    UI -->> Customer : response message
    deactivate UI
