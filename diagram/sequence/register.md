sequenceDiagram
actor Visitor
participant UI
participant System
participant Customer

    Visitor ->> UI: register_form(name, email, username, ...)
    activate UI
    UI ->> System: create_customer(name, email, username, ...)
    activate System

    %% Check for duplicate email
    System ->> System: check if email exists
    alt email exists
        System -->> UI: error - "email already exists"
    else email not duplicate
        %% Check for duplicate username
        System ->> System: check if username exists
        alt username exists
            System -->> UI: error - "username already exists"
        else username not duplicate
            %% Create new customer instance
            System ->> Customer: create new customer instance
            Customer -->> System: success
            System -->> UI: "Customer created successfully"
        end
    end
    deactivate System
    UI -->> Visitor: reponse message
    deactivate UI
