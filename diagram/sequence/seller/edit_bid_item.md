```mermaid

sequenceDiagram 
    actor Seller 
    participant UI 
    participant System 
    participant BidItem

    Seller ->> UI : edit_bid_item(session , bid_item_id)
    activate UI 

    UI ->> System : get_bid_item_by_id(bid_item_id) 
    activate System 
    System -->> UI : Return bid item data 
    deactivate System

    UI ->> System : edit_bid_item(session , name , ... )
    activate System
    System ->> System : get_bid_item_by_id(bid_item_id)

    System ->> System : validate updated bid item data
    alt Validation fails
        System -->> UI : return Exception
        UI -->> Seller : show error message
    else
        System ->> System : validate minimum bid amount
        alt Invalid bid amount
            System -->> UI : return Exception
            UI -->> Seller : show error message
        else
            System ->> BidItem : edit_bid_item(name , ...)
            activate BidItem
            BidItem -->> System : return edited bid item
            deactivate BidItem

            System ->> System : save updated bid item to database
            System -->> UI : return "Item updated successfully"
            deactivate System
            UI -->> Seller : show success message
        end
    end
    deactivate UI


    ```