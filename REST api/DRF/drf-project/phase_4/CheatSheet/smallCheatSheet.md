# DRF Phase 4 — Cheat Sheet

## 1. GenericAPIView

```python
class ProductList(GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

* `queryset` → কোন data নিয়ে কাজ করবে
* `serializer_class` → কোন serializer
* `get_queryset()` → dynamic queryset
* `get_object()` → specific object

---

## 2. Mixins

```text
ListModelMixin       → list()
CreateModelMixin     → create()
RetrieveModelMixin   → retrieve()
UpdateModelMixin     → update()
                       partial_update()
DestroyModelMixin    → destroy()
```

---

## 3. GenericAPIView + Mixins

```python
class ProductList(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
```

Detail:

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

---

## 4. Concrete Generic Views — সবচেয়ে বেশি ব্যবহার

```python
class ProductList(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
```

Mapping:

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

---

## 5. Custom Hooks

```python
def perform_create(self, serializer):
    serializer.save(owner=self.request.user)
```

```text
perform_create()
perform_update()
perform_destroy()
```

Standard CRUD রেখে custom behavior যোগ করার জায়গা।

---

## 6. Abstraction Choice

```text
Custom API          → APIView

CRUD + control      → GenericAPIView + Mixins

Standard CRUD       → Concrete Generic Views

Resource + Router   → ViewSet  ← Phase 5
```

### Golden Rule

```text
GenericAPIView = foundation
Mixin          = CRUD operation
Concrete View  = ready-made CRUD
```
