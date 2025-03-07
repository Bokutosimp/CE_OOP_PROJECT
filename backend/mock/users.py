users = [
    # Admin
    {
        "role": "admin",
        "name": "Admin User",
        "user_id": "admin001",
        "email": "admin@example.com",
        "phone_number": "123-456-7890",
        "username": "adminuser",
        "password": "adminpass",
        "birth_date": "1980-01-01",
        "gender": "M"
    },
    # Customers
    {
        "role": "customer",
        "name": "Customer One",
        "user_id": "cust001",
        "email": "cust1@example.com",
        "phone_number": "123-456-7891",
        "username": "custone",
        "password": "custpass1",
        "birth_date": "1990-01-01",
        "gender": "F",
        "address": "123 Main St",
        "e_bux": 100.0,
        "cart": None,
        "order_history": [
            {
                "order_id": "order001",
                "items": [
                    {"item_id": "item001", "name": "Laptop", "quantity": 1, "price": 500.0},
                    {"item_id": "item002", "name": "Mouse", "quantity": 2, "price": 20.0}
                ],
                "total_price": 540.0,
                "status": "Delivered",
                "order_date": "2025-03-01"
            },
             {
                "order_id": "order999",
                "items": [
                    {"item_id": "item001", "name": "Laptop", "quantity": 1, "price": 500.0},
                    {"item_id": "item002", "name": "Mouse", "quantity": 2, "price": 20.0}
                ],
                "total_price": 5403.0,
                "status": "Delivered",
                "order_date": "2025-03-01"
            }
        ]
    },
    # Sellers (also customers)
    {
        "role": "seller",
        "name": "Seller One",
        "user_id": "sell001",
        "email": "sell1@example.com",
        "phone_number": "123-456-7801",
        "username": "sellone",
        "password": "sellpass1",
        "birth_date": "1985-01-01",
        "gender": "M",
        "address": "808 Spruce St",
        "e_bux": 600.0,
        "cart": None,
        "store_name": "Store One",
        "store_address": "808 Spruce St",
        "order_history": [
            {
                "order_id": "order002",
                "items": [
                    {"item_id": "item003", "name": "Keyboard", "quantity": 1, "price": 45.0}
                ],
                "total_price": 45.0,
                "status": "Shipped",
                "order_date": "2025-03-02"
            }
        ]
    },
    {
        "role": "seller",
        "name": "Seller Two",
        "user_id": "sell002",
        "email": "sell2@example.com",
        "phone_number": "123-456-7802",
        "username": "selltwo",
        "password": "sellpass2",
        "birth_date": "1986-01-01",
        "gender": "F",
        "address": "909 Fir St",
        "e_bux": 650.0,
        "cart": None,
        "store_name": "Store Two",
        "store_address": "909 Fir St",
        "order_history": [
            {
                "order_id": "order003",
                "items": [
                    {"item_id": "item004", "name": "Monitor", "quantity": 1, "price": 150.0},
                    {"item_id": "item005", "name": "USB Cable", "quantity": 3, "price": 15.0}
                ],
                "total_price": 195.0,
                "status": "Processing",
                "order_date": "2025-03-03"
            }
        ]
    }
]