@startuml
skinparam linetype ortho
skinparam nodesep 60
skinparam ranksep 60
skinparam arrowThickness 2
skinparam usecase {
    BorderColor Black
    BackgroundColor LightGray
    FontSize 14
}

actor Customer
actor Seller
actor Admin

hide empty members

package "Admin Actions" {
    usecase "Create Category" as UC_CreateCategory
}

package "Seller Actions" {
    usecase "Add Item" as UC_AddItem
    usecase "Add Bid Item" as UC_AddBidItem
    usecase "Add Stock" as UC_AddStock
    usecase "Add Category" as UC_AddCategory
    usecase "Set Price" as UC_SetPrice
    usecase "Set Start Bid" as UC_StartBid
}

package "Customer Actions" {
    usecase "Search Item" as UC_SearchItem
    usecase "Buy" as UC_Buy
    usecase "Add to Cart" as UC_AddToCart
    usecase "Remove from Cart" as UC_RemoveFromCart
    usecase "Edit Cart" as UC_EditCart
    usecase "Apply Discount" as UC_Discount
    usecase "Make Payment" as UC_Payment
    usecase "Write Review" as UC_Review
    usecase "Bid" as UC_Bid
    usecase "View History" as UC_ViewHistory
}

/' Customer Use Cases '/
Customer --> UC_SearchItem
Customer --> UC_Buy
Customer --> UC_AddToCart
Customer --> UC_RemoveFromCart
Customer --> UC_EditCart
Customer --> UC_Review
Customer --> UC_Bid
Customer --> UC_ViewHistory

UC_Buy --> UC_Payment
UC_AddToCart .> UC_Payment : <<extend>>
UC_Payment <.. UC_Discount : <<extend>>

/' Seller Use Cases '/
Seller --> UC_AddItem
Seller --> UC_AddBidItem
UC_AddItem .> UC_AddStock : <<include>>
UC_AddItem .> UC_AddCategory : <<include>>
UC_AddItem .> UC_SetPrice : <<include>>

UC_AddBidItem .> UC_SetPrice : <<include>>
UC_AddBidItem .> UC_StartBid : <<include>>

/' Admin Use Case '/
Admin --> UC_CreateCategory

@enduml
