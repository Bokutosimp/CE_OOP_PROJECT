```mermaid
---
config:
  theme: dark
---

classDiagram
direction TB
    class User {
	    - name : str
	    - user_id : str
	    - email : str
	    - phone_number : str
	    - username : str
	    - password : str
	    - birth_day : str
	    - gender : str
	    + logout() void
	    + buy()
	    + bid()
	    + add_to_cart()
	    + write_review()
	    + term_ngern()
    }
    class Admin {
	    + add_category() : void
    }
    class Customer {
	    - address : str
	    - e_bux : float
	    + add_to_cart(item : Item, amount : int)
	    + add_bid_money(bidItem : BidItem, amount : float)
	    + add_e_bux(amount : float)
	    + write_review()
    }
    class Seller {
	    + add_item() : void
	    + add_stock()
	    + add_bid_item()
	    + creat_discount_code()
    }
    class Item {
	    - price : float
	    - amount : int
	    - owner : Seller
    }
    class Code {
	    - ID : str
	    - expire : Date
    }
    class Discount {
	    - discount_percent : int
	    - owner : Seller
    }
    class FreeDelivery {
	    - min : int
    }
    class Cart {
	    + select_item()
	    + change_amount(item : Item,amount : int)
	    + place_order() : []
    }
    class Order {
	    - total_amount : float
	    - shipping_fee : float
	    - item_price : float
	    - list_item[] : ItemInCart[]
	    + apply_code()
	    + buy()
    }
    class ItemInCart {
	    - item : Item
	    - amount : int
	    - selected : bool
    }
    class ShippingStatus {
	    - status : str
	    - shipping_date
	    - get_item_date
    }
    class OrderHistory {
	    - order : Order
	    - shipping_status : ShippingStatus
    }
    class BidHistory {
	    - order : BitItem
	    - shipping_status : ShippingStatus
    }
    class System {
	    + login(user: User) : bool
    }
    class Category {
	    - ID : str
	    - name : str
    }
    class Review {
	    - score : int
	    - comment : str
	    - reviewer : Customer
    }
    class BidItem {
	    - start_price : float
	    - last_bid_date : Date
	    - min_bid_amount : float
	    - current_top : Customer
    }
    System o-- User
    System o-- Item
    System o-- Category
    System o-- Code
    Admin --|> User
    Customer --|> User
    Seller --|> Customer
    Customer "1" *-- "*" OrderHistory
    Category "*" <-- "*" Item
    Code <|-- FreeDelivery
    Code <|-- Discount
    Cart --* Customer
    ItemInCart --* Cart
    ItemInCart <-- Order
    Order <-- OrderHistory
    ShippingStatus <-- OrderHistory
    Review "1" --* "*" Item
    BidItem --|> Item
    BidHistory --> BidItem
    BidHistory "1" --o "*" Customer
    ItemInCart --> Item
    Review --> Customer
    ShippingStatus <-- BidHistory

```
sequenceDiagram
    actor Seller
    participant UI
    participant System
    participant Item
    participant bidItem

     Seller ->> UI : submit_product_page (product , session)
    activate UI
    UI ->> System : save_item(user_id, product.name , ... )
    activate System
    System ->> System : validate_name(name, list_items)
    alt Item already exists
        System -->> UI : Return error 
        UI -->> Seller : Show error message
    else
        System ->> System : Check role
        alt User is not a seller
            System -->> UI : Return error 
            UI -->> Seller : Show error message
        else
            System ->> System : Validate category_id
            alt Category not found
                System -->> UI : return error 
                UI -->> Seller : Show error message
            else
                System ->> Item : create_item(id, name , ...)
                activate Item
                Item -->> System : Return created item
                deactivate Item
                System ->> System : list_item.append(Item)
                System -->> UI : Confirm success
                UI -->> Seller : Show success message
            end
        end
    end
    deactivate System
    deactivate UI

    Seller ->> UI : submit_bid_product_page (product , session)
    activate UI
    UI ->> System : save_bid_item(user_id, product.name , ... )
    activate System
    System ->> System : validate_name(name, list_items)
    alt Item already exists
        System -->> UI : Return error (item already exists)
        UI -->> Seller : Show error message
    else
        System ->> System : Check role
        alt User is not a seller
            System -->> UI : Return error (User is not a seller)
            UI -->> Seller : Show error message
        else
            System ->> System : Validate category_id
            alt Category not found
                System -->> UI : Return error (Category not found)
                UI -->> Seller : Show error message
            else
                System ->> bidItem : create_bid_item(id, name , ...)
                activate bidItem
                bidItem -->> System : Return created bid item
                deactivate bidItem
                System ->> System : list_item.append(Item)
                System -->> UI : Confirm success
                UI -->> Seller : Show success message
            end
        end
    end



    Seller ->> UI : edit_item(session , item_id)
    activate UI
    UI ->> System : get_item_by_id(item_id)
    activate System
    System -->> UI : return item data
    deactivate System
    
    UI ->> System : edit_item(session , name , ... )
    activate System
    System ->> System : get_item_by_id(item_id)
    
    System ->> System : Validate updated data
    alt Validation fails
        System -->> UI : return error message
        UI -->> Seller : Show error message
    else
        System ->> System : Validate category_id
        alt Category not found
            System -->> UI : Return error 
            UI -->> Seller : Show error message
        else
            System --> Item : edit_item(name , cat_instances , ...)
            activate Item
            Item -->> System : Return edited item
            deactivate Item
            
            System ->> System : Save updated item to database
            System -->> UI : Confirm success
            UI -->> Seller : Show success message
        end
    end
    deactivate System
    deactivate UI

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
        System -->> UI : return error message
        UI -->> Seller : show error message
    else
        System ->> System : validate minimum bid amount
        alt Invalid bid amount
            System -->> UI : seturn error (Invalid bid amount)
            UI -->> Seller : show error message
        else
            System --> bidItem : edit_bid_item(name , price , category , description , img , start_time , end_time)
            activate bidItem
            bidItem -->> System : return edited bid item
            deactivate bidItem
            
            System ->> System : save updated bid item to database
            System -->> UI : confirm success
            UI -->> Seller : show success message
        end
    end
    deactivate System
    deactivate UI

    Seller ->> UI : update_stock(stock_product , session)
    activate UI
    UI ->> System : add_stock(user_id, item_id, amount)
    activate System
    System ->> System : get_item_by_id(item_id)
    
    System ->> System : validate item
    alt Validation fails
        System -->> UI : return error message
        UI -->> Seller : show error message
    else
        System ->> System : Validate stock amount
        alt Invalid stock amount
            System -->> UI : return error (Invalid stock amount)
            UI -->> Seller : Show error message
        else
            System ->> Item : add_amount(amount)
            activate Item
            Item ->> System : Return updated item
            deactivate Item
            System -->> UI : confirm stock update
            UI -->> Seller : Show success message
        end
    end
    deactivate System
    deactivate UI

    Seller ->> UI : update_bid_stock(bid_stock_product , session)
    activate UI
    UI ->> System : add_bid_stock(user_id, bid_item_id, amount)
    activate System
    System ->> System : get_bid_item_by_id(bid_item_id)
    
    System ->> System : validate bid item
    alt Validation fails
        System -->> UI : return error message
        UI -->> Seller : Show error message
    else
        System ->> System : validate bid stock amount
        alt Invalid bid stock amount
            System -->> UI : return error
            UI -->> Seller : Show error message
        else
            System ->> bidItem : add_amount(amount)
            activate bidItem
            bidItem ->> System : return updated bid item
            deactivate bidItem
            System -->> UI : confirm bid stock update
            UI -->> Seller : Show success message
        end
    end
    deactivate System
    deactivate UI

      Seller ->> UI : submit_discount_page(discount_code , session)
    activate UI
    UI ->> System : save_discount_code(discount_code.name , discount_code.discount_percentage , discount_code.detail)
    activate System
    
    System ->> System : generate discount ID 
    System ->> System : validate discount percentage
    alt Discount percent is invalid
        System -->> UI : return error 
        UI -->> Seller : Show error message
    else
        System ->> System : create new Didscount object
        System ->> System : append discount to list
        System -->> UI : return success message ("Discount code saved successfully")
        UI -->> Seller : show success message
    end
    
    deactivate System
    deactivate UI



```