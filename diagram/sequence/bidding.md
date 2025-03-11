```mermaid
sequenceDiagram
  autonumber
  actor Customer as Customer
  participant UI as UI
  participant System as System
  participant BidItem as BidItem
  participant BiddingHistory as BiddingHistory

  Customer->>UI: Visit /bid/{id}
  activate UI
  UI->>System: get_bid_item_by_id(id)
  activate System
  System->>BidItem: Retrieve bid item details
  activate BidItem
  BidItem-->>System: Return item info & status
  deactivate BidItem
  System-->>UI: Send bid item details
  deactivate System
  UI-->>Customer: Display bid item & status

  loop Every 3 seconds
    UI->>System: Check bid status (/bid_status/{id})
    activate System
    System->>BidItem: Get updated status
    activate BidItem
    BidItem-->>System: Return current bid status
    deactivate BidItem
    System-->>UI: Send updated status
    deactivate System
    alt If status is "Ended" or "Sold"
      UI-->>Customer: Refresh page to show "Auction Ended"
    end
  end

  Customer->>UI: Enter bid amount & submit
  UI->>System: submit_bid_page(bid_input, item_id, session)
  activate System
  System->>BidItem: Validate bid (higher than current price?)
  alt If bid is invalid
    BidItem-->>System: bid valid
    System-->>UI: Alert "Bid must be higher than current price"
  else If bid is valid
    System->>BidItem: Update price & top bidder
    System->>BiddingHistory: Record bid in history
    System-->>UI: Redirect to /bid/{id}
    UI-->>Customer: Show updated bid status
  end

  alt If auction ends
    System->>BidItem: Mark item as "Sold"
    System->>BiddingHistory: Record final bid result
    System->>Customer: Deduct final price from winner's e-bux
    System-->>UI: Notify auction end
  deactivate System
    UI-->>Customer: Show "Auction Ended"
  deactivate UI
  end

```
