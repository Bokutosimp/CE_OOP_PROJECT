sequenceDiagram
  autonumber
  actor Customer
  participant UI
  participant System
  participant User
  participant ItemInCart
  participant Code
  participant Item
  participant Order
  participant ShippingStatus

  Customer ->> UI: Checkout
  UI ->> System: buy_item_in_cart(user_id, code)
  
  System ->> System: Validate shipping_date & get_item_date
  System ->> User: get_user_by_id(user_id)

  alt user not found
      User -->> System: return "User not found"
      System -->> UI: return error 
  else user found
      User -->> System: return user instance
  end

  System ->> System: buy_cart_check_stock(user_id)
  System ->> ItemInCart: Get total price from cart
  ItemInCart -->> System: return total_price

  alt total_price == 0
      System -->> UI: return "Please select at least one item"

  else total_price != 0
      System ->> Item: Get selected items from cart
      Item -->> System: return selected_items
      
      alt discount code is provided
          System ->> Code: Validate and apply discount
          Code -->> System: return discounted total_price
          System ->> Order: buy_item_with_code(user_id, code, selected_items, total_price)
          Order -->> System: return final price
          System -->> UI: return total_price

      else no discount code
          System ->> Order: Create Order(10.0, total_price, selected_items)
          Order -->> System: return order instance
          System ->> ShippingStatus: Create ShippingStatus(shipping_date, get_item_date)
          ShippingStatus -->> System: return shipping instance

          System ->> User: Add order to history
          System ->> User: Deduct e-Bux
          System -->> UI: return total_price
      end
  end
