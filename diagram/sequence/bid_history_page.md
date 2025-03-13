```
sequenceDiagram
    actor Customer
    participant UI
    participant System
    participant BidHistory
    participant ShippingStatus

    Customer ->> UI: bid_history_page(session)
    UI ->> System: get_history_bids(user_id)
    System ->> System: get_user_by_id(user_id)
    System ->> System: get_bid_history()
    

        System ->> BidHistory: get_item()
        BidHistory ->> ShippingStatus: get_status()
        ShippingStatus -->> System: return status
        System ->> System: Check if status == 'Ended' or 'Sold'

    System -->> UI: return bid_history_list
    UI -->> Customer : Show bid history
    ```