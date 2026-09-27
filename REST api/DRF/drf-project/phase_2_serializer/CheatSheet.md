# DRF Phase 2 — Serializers Cheat Sheet

## 1. Serializer কী?

Serializer হলো DRF-এর এমন একটি component যা API-এর জন্য data-এর **representation এবং validation boundary** হিসেবে কাজ করে।

দুই দিকে কাজ করে:

### Response side

text
Django Model/Object
        ↓
    Serializer
        ↓
 API Representation
        ↓
     Response


### Request side

text
Client JSON
    ↓
request.data
    ↓
Serializer
    ↓
Validation
    ↓
validated_data
    ↓
Model / Database


---

# 2. Basic Serializer

python
from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()


এখানে fields manually define করতে হয়।

---

# 3. ModelSerializer

Model-এর field থেকে serializer field automatically তৈরি করে।

python
class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ["id", "name", "price"]


### সাধারণ CRUD API-তে

text
ModelSerializer
      ↓
কম boilerplate
      ↓
automatic fields
      ↓
default create/update


---

# 4. Meta

সঠিক:

python
class Meta:
    model = Product
    fields = ["id", "name", "price"]


ভুল:

python
class meta:


Python case-sensitive।

---

# 5. fields

Explicit fields:

python
fields = ["id", "name", "price"]


সব model field:

python
fields = "__all__"


Production API-তে explicit fields সাধারণত বেশি deliberate এবং নিরাপদ API contract দেয়।

---

# 6. Incoming Data

Client:

json
{
    "name": "Keyboard",
    "price": 1000
}


View:

python
serializer = ProductSerializer(data=request.data)


এখানে:

python
request.data


হলো raw incoming API data।

---

# 7. is_valid()

python
serializer.is_valid()


Validation চালায়।

Better:

python
serializer.is_valid(raise_exception=True)


Invalid হলে DRF ValidationError raise করবে এবং সাধারণভাবে 400 response তৈরি করবে।

---

# 8. validated_data

python
serializer.validated_data


শুধু validation pass করা data।

text
request.data
    ↓
validation
    ↓
validated_data


validated_data পাওয়ার আগে:

python
serializer.is_valid()


করতে হবে।

---

# 9. errors

python
serializer.errors


Invalid data-এর validation errors পাওয়া যায়।

উদাহরণ:

json
{
    "price": [
        "Price cannot be negative."
    ]
}


---

# 10. required

python
name = serializers.CharField(required=True)


Client field না পাঠালে validation error।

---

# 11. allow_null

python
discount = serializers.IntegerField(allow_null=True)


এটা:

json
"discount": null


allow করে।

কিন্তু:

text
null ≠ 0
null ≠ ""


---

# 12. default

python
discount = serializers.IntegerField(default=0)


Client field না পাঠালে:

python
discount = 0


হবে।

---

# 13. read_only

python
id = serializers.IntegerField(read_only=True)


Client input-এ set করতে পারবে না, কিন্তু response-এ দেখতে পারবে।

text
Request  → ❌
Response → ✅


---

# 14. write_only

python
password = serializers.CharField(write_only=True)


Client পাঠাতে পারবে, কিন্তু response-এ দেখা যাবে না।

text
Request  → ✅
Response → ❌


Password-এর ক্ষেত্রে commonly useful।

**কিন্তু write_only password hash করে না।**

---

# 15. Field-level Validation

Pattern:

python
def validate_<field_name>(self, value):


Example:

python
def validate_price(self, value):
    if value < 0:
        raise serializers.ValidationError(
            "Price cannot be negative."
        )
    return value


### Important

ভুল:

python
def price_validate(self, value):


সঠিক:

python
def validate_price(self, value):


---

# 16. Object-level Validation

একাধিক field-এর মধ্যে relationship/rule check করতে:

python
def validate(self, attrs):
    if attrs["discount"] > attrs["price"]:
        raise serializers.ValidationError(
            "Discount cannot be greater than price."
        )

    return attrs


### Rule

text
একটা field-এর rule
    ↓
validate_<field>()

Multiple fields-এর rule
    ↓
validate()


---

# 17. Validation Flow

Conceptually:

text
request.data
     ↓
Serializer fields
     ↓
Basic/type validation
     ↓
validate_<field>()
     ↓
validate()
     ↓
validated_data


উদাহরণ:

json
{
    "price": "abc"
}


IntegerField type validation-এই fail করতে পারে।

তাই validate_price() সবসময় পর্যন্ত পৌঁছাবে না।

---

# 18. create()

New object তৈরি করতে:

python
def create(self, validated_data):
    return Product.objects.create(**validated_data)


যদি:

python
validated_data = {
    "name": "Keyboard",
    "price": 1000
}


তাহলে:

python
Product.objects.create(
    name="Keyboard",
    price=1000
)


এর equivalent।

---

# 19. update()

Existing object update:

python
def update(self, instance, validated_data):
    instance.name = validated_data.get(
        "name",
        instance.name
    )

    instance.price = validated_data.get(
        "price",
        instance.price
    )

    instance.save()

    return instance


এখানে:

text
instance


হলো existing database object।

---

# 20. instance

Example:

python
product = Product.objects.get(id=5)

serializer = ProductSerializer(
    instance=product,
    data=request.data,
    partial=True
)


এখানে:

text
instance = existing Product
data     = new incoming data


---

# 21. serializer.save()

Serializer-এর context অনুযায়ী:

text
No instance
    ↓
save()
    ↓
create()


আর:

text
Existing instance
    ↓
save()
    ↓
update()


অর্থাৎ:

python
serializer.save()


নিজে থেকেই create/update path অনুযায়ী যায়।

---

# 22. partial=True

PATCH-এর মতো partial update-এ useful।

python
serializer = ProductSerializer(
    instance=product,
    data=request.data,
    partial=True
)


Client শুধু:

json
{
    "price": 1200
}


পাঠালেও পুরো object-এর সব required field আবার পাঠাতে হবে না।

---

# 23. Serialization / Response

Database object:

python
product = Product.objects.get(id=1)


Serializer:

python
serializer = ProductSerializer(product)


Response data:

python
serializer.data


Flow:

text
Model Object
     ↓
Serializer(object)
     ↓
serializer.data
     ↓
Response


---

# 24. many=True

একটা object:

python
ProductSerializer(product)


অনেকগুলো object:

python
ProductSerializer(
    products,
    many=True
)


many=True মানে:

> আমি collection/list serialize করছি।

---

# 25. Relationships — Basic Representation

### Primary Key

python
author = serializers.PrimaryKeyRelatedField(
    queryset=Author.objects.all()
)


Request:

json
{
    "author": 5
}


---

### SlugRelatedField

python
author = serializers.SlugRelatedField(
    slug_field="name",
    queryset=Author.objects.all()
)


Request:

json
{
    "author": "Rahim"
}


---

### Nested Serializer

python
author = AuthorSerializer()


Response:

json
{
    "author": {
        "id": 5,
        "name": "Rahim"
    }
}


Deep relationship discussion Phase 7-এ হবে।

---

# 26. SerializerMethodField

Model-এ field না থাকলেও calculated field তৈরি করা যায়।

python
final_price = serializers.SerializerMethodField()

def get_final_price(self, obj):
    return obj.price - obj.discount


Response:

json
{
    "price": 1000,
    "discount": 100,
    "final_price": 900
}


Pattern:

text
field_name
    ↓
get_field_name()


---

# 27. obj কী?

python
def get_final_price(self, obj):


obj হলো বর্তমানে serialize হওয়া model instance।

যেমন:

text
obj
 ├── name
 ├── price
 └── discount


তাই:

python
obj.price


দিয়ে price পাওয়া যায়।

---

# 28. to_representation()

পুরো output representation customize করতে পারি।

python
def to_representation(self, instance):
    data = super().to_representation(instance)

    data["price_with_currency"] = (
        f"{instance.price} BDT"
    )

    return data


Flow:

text
Model object
     ↓
normal DRF representation
     ↓
to_representation()
     ↓
custom modification
     ↓
final output


সাধারণ calculated field-এর জন্য SerializerMethodField যথেষ্ট হলে সেটাই prefer করা ভালো।

---

# 29. Complete POST Flow

python
serializer = ProductSerializer(
    data=request.data
)

serializer.is_valid(
    raise_exception=True
)

product = serializer.save()

return Response(
    ProductSerializer(product).data,
    status=201
)


Flow:

text
Client
  ↓
POST
  ↓
request.data
  ↓
Serializer(data=...)
  ↓
is_valid()
  ↓
validated_data
  ↓
save()
  ↓
create()
  ↓
Database
  ↓
Model instance
  ↓
Serializer(instance)
  ↓
serializer.data
  ↓
Response


---

# 30. Complete GET Flow

python
products = Product.objects.all()

serializer = ProductSerializer(
    products,
    many=True
)

return Response(serializer.data)


Flow:

text
Client
  ↓
GET
  ↓
View
  ↓
Database
  ↓
QuerySet
  ↓
Serializer(many=True)
  ↓
serializer.data
  ↓
Response


---

# 31. সবচেয়ে Important Mental Model

### POST

text
JSON
 ↓
request.data
 ↓
Serializer
 ↓
Validation
 ↓
validated_data
 ↓
save()
 ↓
Database


### GET

text
Database
 ↓
Model / QuerySet
 ↓
Serializer
 ↓
serializer.data
 ↓
Response
 ↓
JSON


---

# 32. Common Mistakes

### ভুল ১

python
serializer.validated_data


is_valid()-এর আগে ব্যবহার করা।

---

### ভুল ২

python
def price_validate(...)


সঠিক:

python
def validate_price(...)


---

### ভুল ৩

একই method দুইবার define করা:

python
def validate_marks(...):
    ...

def validate_marks(...):
    ...


দ্বিতীয়টা প্রথমটাকে overwrite করবে।

---

### ভুল ৪

read_only-কে permission মনে করা।

text
read_only ≠ authorization


---

### ভুল ৫

write_only=True দিলেই password secure হয়ে গেছে ভাবা।

text
write_only
    ≠
password hashing


---

### ভুল ৬

Serializer ব্যবহার করে ModelSerializer-এর মতো automatic model fields আশা করা।

python
serializers.Serializer


এ manual field declaration দরকার।

---

### ভুল ৭

SerializerMethodField-এর obj-কে field value ভাবা।

python
def get_grade(self, obj):


এখানে obj পুরো model instance।

তাই:

python
obj.marks


লাগতে পারে।

---

### ভুল ৮

many=True ভুলে যাওয়া।

একাধিক object:

python
ProductSerializer(
    products,
    many=True
)


---

# 33. Quick Revision Table

| Concept                 | মনে রাখার shortcut                           |
| ----------------------- | -------------------------------------------- |
| request.data          | Client-এর incoming data                      |
| is_valid()            | Validation চালায়                             |
| validated_data        | Validated input                              |
| errors                | Validation errors                            |
| save()                | Create/update trigger                        |
| create()              | New object                                   |
| update()              | Existing object                              |
| instance              | Existing object                              |
| partial=True          | Partial update                               |
| many=True             | Multiple objects                             |
| read_only             | Response only                                |
| write_only            | Request only                                 |
| validate_<field>      | Single field validation                      |
| validate()            | Multiple-field/object validation             |
| SerializerMethodField | Calculated/custom output field               |
| to_representation()   | Customize final representation               |
| ModelSerializer       | Model-based serializer with less boilerplate |

---

# 34. One-Line Mental Model

সবশেষে শুধু এটা মনে রাখো:

text
                    SERIALIZER

Client → request.data → Validate → validated_data → save() → DB
                                               
DB → Model/QuerySet → Serializer → serializer.data → Response → Client


Serializer শুধু **JSON বানানোর tool না**।

এটা API-এর **data representation + validation + model interaction boundary**।

---

## Phase 2 Status

এখন পর্যন্ত Phase 2-এর **core concepts covered**।

আরও ২–৩টা বিষয় properly practice করে তারপর Phase 2 officially complete করব:

1. Field options-এর edge cases
2. Writable nested serializer
3. Final Serializer challenge / revision

তারপর আমরা **Phase 3 — CRUD**-এ যাব।
