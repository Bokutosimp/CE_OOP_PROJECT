```mermaid
sequenceDiagram
    actor Seller
    participant UI
    participant System
    participant BidItem



 System ->> System : validate bid item
    alt Validation fails
        System -->> UI : return Exception
        UI -->> Seller : Show error message
    else
        System ->> System : validate bid stock amount
        alt Invalid bid stock amount
            System -->> UI : return Exception
            UI -->> Seller : Show error message
        else
            System ->> bidItem : add_amount(amount)
            activate bidItem
            bidItem -->> System : return updated bid item
            deactivate bidItem
            System -->> UI : return Exception
            UI -->> Seller : Show success message
        end
    end
```
