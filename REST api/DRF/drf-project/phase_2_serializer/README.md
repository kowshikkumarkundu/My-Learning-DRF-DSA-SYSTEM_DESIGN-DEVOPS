                 SERIALIZER
                     │
        ┌────────────┼────────────┐
        ↓            ↓            ↓
   Validation    Representation  Relationships
        │            │
        │            ├── ModelSerializer
        │            ├── SerializerMethodField
        │            └── to_representation()
        │
        ├── validate_<field>()
        ├── validate()
        ├── create()
        └── update()


## POST request flow
                    POST
                     ↓
              request.data
                     ↓
          ProductSerializer(data=...)
                     ↓
               is_valid()
                     ↓
        ┌────────────┴────────────┐
        ↓                         ↓
 field validation          object validation
        ↓                         ↓
 validate_price()             validate()
 validate_discount()
        └────────────┬────────────┘
                     ↓
             validated_data
                     ↓
                save()
                     ↓
                create()
                     ↓
          Product.objects.create()
                     ↓
                 Database
                     ↓
             Product object
                     ↓
        ProductSerializer(product)
                     ↓
             serializer.data
                     ↓
                  Response


খন সবচেয়ে important distinction

এই চারটা জিনিস যেন কখনো mix না করো:

| Situation                                  | Serializer                                                    |
| ------------------------------------------ | ------------------------------------------------------------- |
| Client থেকে নতুন data আসছে                 | `Serializer(data=request.data)`                               |
| Incoming data validate করতে হবে            | `.is_valid()`                                                 |
| নতুন object save করতে হবে                  | `.save()` → `create()`                                        |
| Existing object update করতে হবে            | `Serializer(instance=obj, data=...)` → `.save()` → `update()` |
| Database object response হিসেবে পাঠাতে হবে | `Serializer(obj).data`                                        |


## Phase 2 — Serializers

এখন আমরা DRF-এর সবচেয়ে central conceptগুলোর একটায় ঢুকব:

Serializer আসলে কেন দরকার?

এখানে আমরা প্রথমে code লিখব না। আগে বুঝব:

Python/Django Model
       ↕
   Serializer
       ↕
JSON/API representation

তারপর ধাপে ধাপে:

Serialization কী
Deserialization কী
Serializer
ModelSerializer
Fields
Validation
validated_data
create() / update()
read_only / write_only
required, allow_null, default
Nested serializers
Relationships
SerializerMethodField
Custom validation
পুরো serializer validation flow

এখান থেকেই আমরা actual database-backed API বানানো শুরু করব।