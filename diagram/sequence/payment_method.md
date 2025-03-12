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
  participant Seller

  Customer ->>+ UI: Checkout
  UI ->>+ System: buy_item_in_cart(user_id, code)
  
  System ->> System: get_user_by_id(user_id)
  System ->>+ User: user_id

  alt user not found
      User -->> System: return "User not found"
      System -->> UI: return User not found 
      UI -->> Customer: return User not found 

  else user found
      User -->>- System: return user instance
  end

  System ->> System: buy_cart_check_stock(user_id)
  System ->+ ItemInCart: Get total price from cart
  ItemInCart -->>- System: return total_price

  alt total_price == 0
      System -->> UI: return "Please select at least one item"

  else total_price != 0
      System ->>+ Item: Get selected items from cart
      Item -->>- System: return selected_items
      
      alt discount code is provided
          System ->> System: buy_item_with_code(user_id, code, selected_items, total_price)
          System ->> System: apply_code(code)
          System ->>+ Code: Validate and apply discount
          Code -->>- System: return discounted percentage
          System ->>+ Order: Create Order(10.0, discounted_price, selected_items)
          Order -->>- System: return order instance
          System ->>+ ShippingStatus: Create ShippingStatus(shipping_date, get_item_date)
          ShippingStatus -->>- System: return shipping instance
          System ->>+ User: Add order to history
          User ->>+ System: add order success
          System -> User: Deduct e-Bux
          User ->>- System: deduct e-bux success
          System ->>+ Seller: add e-bux to Seller
          Seller ->>- System: add e-bux success
          System -->> UI: redirect to profile
          
      else no discount code
          System ->>+ Order: Create Order(10.0, total_price, selected_items)
          Order -->>- System: return order instance
          System ->>+ ShippingStatus: Create ShippingStatus(shipping_date, get_item_date)
          ShippingStatus -->>- System: return shipping instance
          System ->>+ User: Add order to history
          User ->>+ System: add order success
          System -> User: Deduct e-Bux
          User ->>- System: deduct e-bux success
          System ->>+ Seller: add e-bux to Seller
          Seller ->>- System: add e-bux success
          System -->> UI: redirect to profile
      end
  end
  UI ->>- Customer: redirect to profile
