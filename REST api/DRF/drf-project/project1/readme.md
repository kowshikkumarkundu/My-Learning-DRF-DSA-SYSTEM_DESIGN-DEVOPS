## phase 1
# project setup
    Django
    DRF
    Simple JWT
    Task app

## phase 2
# Model
    Task
    ↓
    owner → User

## phase 3
# Serializer
    TaskSerializer

## phase 4
# JWT authentication

    /login
    ↓
    access token
    ↓
    Authorization: Bearer ...
    ↓
    request.user

## phase 5
# CRUD

    POST
    GET
    PUT/PATCH
    DELETE

## phase 6
# Object-level security

    User 1 → Task 1
    User 2 → Task 2