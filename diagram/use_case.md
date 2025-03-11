@startuml
:costumer:
:seller:
:admin:
package Admin{
usecase "create_category"
}
package Seller{
usecase "add_item"
usecase "add_stock"
usecase "add_category"
usecase "set_price"
usecase "start_bid"
}
package Costumer{
usecase "search_item"
usecase "buy"
usecase "add_to_cart"
usecase "remove_from_cart"
usecase "edit_cart"
usecase "discount"
usecase "payment_method"
usecase "payment"
usecase "review"
usecase "bid"
usecase "view_history"
}
/'costumer'/
costumer --> search_item
costumer --> buy
costumer --> add_to_cart
costumer --> remove_from_cart
costumer --> edit_cart
buy --> payment_method
add_to_cart .> payment_method : extend
payment_method --> payment
payment <. discount : extend
costumer --> review
costumer --> bid
costumer --> view_history

/'seller'/
seller --> add_item
add_item .> add_stock : include
add_item .> add_category : include
add_item <|-- set_price
add_item <|-- start_bid

/'admin'/
admin --> create_category

@enduml
