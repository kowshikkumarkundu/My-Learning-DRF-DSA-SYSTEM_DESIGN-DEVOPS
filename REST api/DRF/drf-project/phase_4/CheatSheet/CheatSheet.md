অবশ্যই। Phase 4-এর জন্য এমন একটা **practical cheat sheet** দিচ্ছি যেটা পরে project করার সময় সরাসরি দেখে মনে করতে পারবে।

# DRF Phase 4 — Generic Views & Mixins Cheat Sheet

## 1. Phase 4-এর মূল উদ্দেশ্য

Phase 3-এ আমরা `APIView` দিয়ে CRUD manually লিখেছি।

Phase 4-এ DRF-এর **Generic Views + Mixins** ব্যবহার করে সেই repetitive CRUD logic কমিয়ে ফেলি।

মূল progression:

```text
APIView
   ↓
GenericAPIView + Mixins
   ↓
Concrete Generic Views
```

---

# 2. GenericAPIView

```python
from rest_framework.generics import GenericAPIView
```

Basic structure:

```python
class ProductList(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### `queryset`

কোন database objects নিয়ে কাজ করবে সেটা বলে।

```python
queryset = Product.objects.all()
```

### `serializer_class`

কোন serializer ব্যবহার করবে সেটা বলে।

```python
serializer_class = ProductSerializer
```

---

# 3. Important GenericAPIView Methods

### `get_queryset()`

Default queryset-এর বদলে dynamic queryset দিতে পারি।

```python
def get_queryset(self):
    return Product.objects.filter(stock__gt=0)
```

Useful যখন:

* user অনুযায়ী data filter করতে হবে
* dynamic filtering দরকার
* permission অনুযায়ী queryset পরিবর্তন করতে হবে

---

### `get_serializer()`

Configured `serializer_class` থেকে serializer তৈরি করে।

Conceptually:

```python
self.get_serializer(...)
```

এর মাধ্যমে DRF serializer instance তৈরি করে।

---

### `get_object()`

Detail endpoint-এর নির্দিষ্ট object বের করতে ব্যবহৃত হয়।

```text
GET /products/5/
          ↓
      get_object()
          ↓
     Product #5
```

---

# 4. Mixins

Mixin হলো **reusable CRUD operation implementation**।

```python
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
```

| Mixin                | Main method        | কাজ            |
| -------------------- | ------------------ | -------------- |
| `ListModelMixin`     | `list()`           | সব object      |
| `CreateModelMixin`   | `create()`         | নতুন object    |
| `RetrieveModelMixin` | `retrieve()`       | একটি object    |
| `UpdateModelMixin`   | `update()`         | full update    |
| `UpdateModelMixin`   | `partial_update()` | partial update |
| `DestroyModelMixin`  | `destroy()`        | delete         |

---

# 5. GenericAPIView + Mixins

## List + Create

```python
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    ListModelMixin,
    CreateModelMixin,
)

class ProductList(
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
```

Flow:

```text
GET
 ↓
get()
 ↓
self.list(request)
 ↓
ListModelMixin.list()
```

```text
POST
 ↓
post()
 ↓
self.create(request)
 ↓
CreateModelMixin.create()
```

---

# 6. Detail CRUD with Mixins

```python
class ProductDetail(
    GenericAPIView,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin
):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def patch(self, request, pk):
        return self.partial_update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
```

Mapping:

```text
GET     → retrieve()
PUT     → update()
PATCH   → partial_update()
DELETE  → destroy()
```

---

# 7. Concrete Generic Views

GenericAPIView + Mixins-কে আরও সহজ করার জন্য DRF ready-made classes দিয়েছে।

## List + Create

```python
from rest_framework.generics import ListCreateAPIView

class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

Automatically:

```text
GET  → list
POST → create
```

---

## Retrieve + Update + Delete

```python
from rest_framework.generics import RetrieveUpdateDestroyAPIView

class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

Automatically:

```text
GET    → retrieve
PUT    → update
PATCH  → partial_update
DELETE → destroy
```

---

# 8. সবচেয়ে গুরুত্বপূর্ণ Generic View Classes

| Generic View                   | Operations                 |
| ------------------------------ | -------------------------- |
| `ListAPIView`                  | GET list                   |
| `CreateAPIView`                | POST                       |
| `RetrieveAPIView`              | GET detail                 |
| `UpdateAPIView`                | PUT/PATCH                  |
| `DestroyAPIView`               | DELETE                     |
| `ListCreateAPIView`            | GET + POST                 |
| `RetrieveUpdateAPIView`        | GET + PUT + PATCH          |
| `RetrieveDestroyAPIView`       | GET + DELETE               |
| `RetrieveUpdateDestroyAPIView` | GET + PUT + PATCH + DELETE |

---

# 9. Standard CRUD-এর সবচেয়ে common pattern

Most basic CRUD API-এর জন্য:

```python
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

এই pattern মনে রাখলেই অনেক CRUD API খুব দ্রুত লেখা যায়।

---

# 10. PUT vs PATCH

```text
PUT
 ↓
update()
 ↓
Full update
```

```text
PATCH
 ↓
partial_update()
 ↓
Partial update
```

PATCH-এর ক্ষেত্রে DRF internally `partial=True` ব্যবহার করে।

---

# 11. `queryset` vs `get_queryset()`

### Static

```python
queryset = Product.objects.all()
```

সবসময় একই base queryset।

### Dynamic

```python
def get_queryset(self):
    return Product.objects.filter(stock__gt=0)
```

Request/user/context অনুযায়ী queryset পরিবর্তন করা যায়।

---

# 12. `serializer_class` vs `get_serializer()`

সাধারণ ক্ষেত্রে:

```python
serializer_class = ProductSerializer
```

Generic View internally serializer তৈরি করার সময়:

```python
self.get_serializer(...)
```

ব্যবহার করে।

তাই সাধারণ CRUD-এ manually:

```python
serializer = ProductSerializer(...)
```

লিখতে হয় না।

---

# 13. Custom behavior — `perform_*`

Generic Views ব্যবহার করেও custom behavior যোগ করা যায়।

### Create

```python
def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
```

### Update

```python
def perform_update(self, serializer):
    serializer.save()
```

### Destroy

```python
def perform_destroy(self, instance):
    instance.delete()
```

সব CRUD logic আবার manually rewrite করার দরকার নেই।

---

# 14. Generic View Request Flow

### List

```text
Client
 ↓
GET /products/
 ↓
ListCreateAPIView
 ↓
list()
 ↓
get_queryset()
 ↓
get_serializer(many=True)
 ↓
Response
```

### Create

```text
Client
 ↓
POST /products/
 ↓
ListCreateAPIView
 ↓
create()
 ↓
serializer validation
 ↓
serializer.save()
 ↓
DB
 ↓
201 Created
```

### Detail

```text
GET /products/5/
 ↓
RetrieveUpdateDestroyAPIView
 ↓
get_object()
 ↓
Product #5
 ↓
serializer
 ↓
Response
```

---

# 15. APIView vs Generic Views

## APIView

```python
class ProductList(APIView):

    def get(self, request):
        ...

    def post(self, request):
        ...
```

Use when:

* highly custom flow
* standard CRUD-এর বাইরে behavior
* method-level control দরকার

---

## Generic Views

```python
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

Use when:

* standard CRUD
* repetitive CRUD logic
* DRF-এর built-in behavior যথেষ্ট

---

# 16. Abstraction Ladder

সবচেয়ে important diagram:

```text
APIView
  │
  │ more abstraction
  ▼
GenericAPIView + Mixins
  │
  │ more abstraction
  ▼
Concrete Generic Views
  │
  │
  ▼
ViewSets + Routers
```

Phase 4-এর scope:

```text
GenericAPIView
       +
Mixins
       +
Concrete Generic Views
```

Phase 5:

```text
ViewSets
Routers
@action
```

---

# 17. Quick CRUD Mapping

```text
Collection URL
/api/products/

GET  → List
POST → Create
```

```text
Detail URL
/api/products/5/

GET    → Retrieve
PUT    → Update
PATCH  → Partial Update
DELETE → Destroy
```

---

# 18. কোন code কখন লিখব?

### Standard CRUD হলে:

```python
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

```python
class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

### একটু custom behavior দরকার হলে:

```python
class ProductList(
    GenericAPIView,
    ListModelMixin,
    CreateModelMixin
):
    ...
```

### অনেক custom/non-standard API হলে:

```python
class ProductView(APIView):
    ...
```

---

# 19. Phase 4-এর Golden Rule

```text
GenericAPIView
→ infrastructure/configuration

Mixin
→ reusable CRUD operation

Concrete Generic View
→ ready-made combination of GenericAPIView + required mixins
```

সবচেয়ে সহজভাবে:

```text
GenericAPIView = foundation
Mixin          = operation
Concrete View  = ready-made CRUD package
```

---

# 20. One-Minute Revision

```python
# Standard CRUD

class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

মনে রাখবে:

```text
ListCreateAPIView
    GET  → list
    POST → create

RetrieveUpdateDestroyAPIView
    GET    → retrieve
    PUT    → update
    PATCH  → partial_update
    DELETE → destroy
```

আর:

```text
queryset
→ কোন objects?

serializer_class
→ কোন serializer?

get_queryset()
→ dynamic queryset

get_object()
→ specific object

Mixins
→ reusable CRUD logic
```

**Phase 4-এর essence:**

> আগে তুমি CRUD logic লিখতে → এখন DRF-এর reusable abstraction ব্যবহার করে শুধু configure করো।
