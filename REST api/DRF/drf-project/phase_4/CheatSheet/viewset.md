হ্যাঁ, বুঝেছি। একবারে copy করার সুবিধার জন্য আমি পুরো cheatsheet-টা **একটা single code block**-এর মধ্যে দিচ্ছি। Code block-এর copy button চাপলেই পুরোটা একসাথে copy হবে।

```text
============================================================
              DRF VIEWSET + ROUTER CHEATSHEET
============================================================

1. VIEWSET কী?
------------------------------------------------------------
ViewSet = একটি resource-এর related API actions এক class-এর
মধ্যে organize করার abstraction.

ModelViewSet সাধারণ CRUD actions ready-made দেয়।

Example:

from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


2. ModelViewSet-এর প্রধান ACTIONS
------------------------------------------------------------

HTTP Method     URL                    Action
------------------------------------------------------------
GET             /products/             list()
POST            /products/             create()

GET             /products/5/           retrieve()
PUT             /products/5/           update()
PATCH           /products/5/           partial_update()
DELETE          /products/5/           destroy()


Mental Model:

ModelViewSet
    |
    |-- list()
    |-- create()
    |-- retrieve()
    |-- update()
    |-- partial_update()
    `-- destroy()


3. ROUTER কী?
------------------------------------------------------------
Router ViewSet-এর জন্য automatically URL routes তৈরি করে।

Example:

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    "products",
    ProductViewSet,
    basename="product"
)


4. Router URL include করতে হবে
------------------------------------------------------------

from django.urls import path, include

urlpatterns = [
    path("", include(router.urls)),
]


5. register() বুঝে রাখো
------------------------------------------------------------

router.register(
    "products",
    ProductViewSet,
    basename="product"
)

             "products"
                  |
                  v
             URL prefix

          ProductViewSet
                  |
                  v
          কোন ViewSet কাজ করবে

          basename="product"
                  |
                  v
       generated URL naming


IMPORTANT:
"products" model name থেকেই আসতেই হবে না।

এটাও valid:

router.register(
    "items",
    ProductViewSet,
    basename="product"
)

তাহলে URL হবে:

/items/
/items/5/


6. basename
------------------------------------------------------------
basename URL path নয়।

Example:

router.register(
    "kowshik",
    ProductViewSet,
    basename="product"
)

URL:

/kowshik/
/kowshik/5/

এখানে:

kowshik  = URL prefix
product  = basename


7. DefaultRouter
------------------------------------------------------------

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

DefaultRouter:
- ViewSet routes generate করে
- API root দেয়
- সাধারণত standard DRF API-তে ব্যবহার করা হয়


8. SimpleRouter
------------------------------------------------------------

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

SimpleRouter basic ViewSet routes generate করে,
কিন্তু DefaultRouter-এর API root থাকে না।

শুরুতে DefaultRouter মনে রাখলেই যথেষ্ট।


9. COMPLETE VIEWSET SETUP
------------------------------------------------------------

# views.py

from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()

router.register(
    "products",
    ProductViewSet,
    basename="product"
)

urlpatterns = [
    path("", include(router.urls)),
]


Generated routes:

GET     /products/
POST    /products/

GET     /products/5/
PUT     /products/5/
PATCH   /products/5/
DELETE  /products/5/


10. @action
------------------------------------------------------------
CRUD-এর বাইরে custom endpoint বানাতে @action ব্যবহার করা হয়।

Example:

from rest_framework.decorators import action
from rest_framework.response import Response


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"])
    def discount(self, request, pk=None):
        return Response({
            "message": "Discount applied"
        })


URL:

POST /products/5/discount/


11. detail=True
------------------------------------------------------------
Specific object-এর জন্য custom action।

Example:

@action(detail=True, methods=["post"])
def discount(self, request, pk=None):
    ...

URL:

/products/5/discount/

এখানে pk থাকে।

Meaning:

products
    |
    v
specific product
    |
    v
pk = 5


12. detail=False
------------------------------------------------------------
Collection-level custom action।

Example:

@action(detail=False, methods=["get"])
def featured(self, request):
    ...

URL:

GET /products/featured/

এখানে specific pk লাগে না।


13. Multiple HTTP Methods
------------------------------------------------------------

@action(
    detail=True,
    methods=["get", "post"]
)
def something(self, request, pk=None):
    ...


তাহলে:

GET  /products/5/something/
POST /products/5/something/


14. queryset
------------------------------------------------------------

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()

queryset বলে:

"এই ViewSet কোন database objects নিয়ে কাজ করবে?"


15. serializer_class
------------------------------------------------------------

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

serializer_class বলে:

"এই API কোন serializer ব্যবহার করবে?"


16. Dynamic get_queryset()
------------------------------------------------------------

def get_queryset(self):
    return Product.objects.filter(
        owner=self.request.user
    )

Useful যখন queryset request/user অনুযায়ী পরিবর্তন হবে।


17. perform_create()
------------------------------------------------------------
Create-এর সময় extra save logic করার জায়গা।

Example:

def perform_create(self, serializer):
    serializer.save(owner=self.request.user)


Flow:

POST
  |
  v
create()
  |
  v
validation
  |
  v
perform_create()
  |
  v
serializer.save()
  |
  v
Database


18. perform_update()
------------------------------------------------------------

def perform_update(self, serializer):
    serializer.save(
        updated_by=self.request.user
    )


19. perform_destroy()
------------------------------------------------------------

def perform_destroy(self, instance):
    instance.delete()

Custom delete logic থাকলে এখানে করা যায়।


20. ViewSet vs APIView
------------------------------------------------------------

APIView:

class ProductView(APIView):

    def get(self, request):
        ...

    def post(self, request):
        ...

    def patch(self, request, pk):
        ...


ViewSet:

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


APIView-তে:
HTTP methods অনুযায়ী নিজে method লিখি।

ViewSet-এ:
Resource/action based abstraction ব্যবহার করি।


21. ABSTRACTION LADDER
------------------------------------------------------------

APIView
    |
    v
GenericAPIView + Mixins
    |
    v
Concrete Generic Views
    |
    v
ViewSet + Router


APIView:
Maximum manual control


GenericAPIView + Mixins:
Reusable CRUD building blocks


Concrete Generic Views:
Standard CRUD-এর ready-made views


ViewSet + Router:
Resource-based API-এর compact abstraction


22. VIEWSET REQUEST MAPPING
------------------------------------------------------------

                 Router
                    |
                    v
             URL + HTTP Method
                    |
                    v
                ViewSet
                    |
       +------------+------------+
       |            |            |
       v            v            v
    list()       create()    retrieve()
       |            |            |
      GET          POST       GET /pk

Detail actions:

PUT       -> update()
PATCH     -> partial_update()
DELETE    -> destroy()


23. IMPORTANT ROUTES
------------------------------------------------------------

Collection:

GET     /products/
POST    /products/


Detail:

GET     /products/5/
PUT     /products/5/
PATCH   /products/5/
DELETE  /products/5/


Custom:

POST    /products/5/discount/

or:

GET     /products/featured/


24. MOST IMPORTANT TEMPLATE
------------------------------------------------------------

# views.py

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=["post"])
    def discount(self, request, pk=None):
        return Response({
            "message": "Discount applied"
        })


# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProductViewSet


router = DefaultRouter()

router.register(
    "products",
    ProductViewSet,
    basename="product"
)

urlpatterns = [
    path("", include(router.urls)),
]


25. INTERVIEW / EXAM QUICK RECALL
------------------------------------------------------------

Q: ViewSet কী?

A:
একটি resource-এর related API actions এক class-এর মধ্যে
organize করার abstraction.


Q: ModelViewSet কী দেয়?

A:
list()
create()
retrieve()
update()
partial_update()
destroy()


Q: Router কী করে?

A:
ViewSet-এর actions-এর জন্য automatically URL routes
generate করে।


Q: register()-এর প্রথম argument কী?

A:
URL prefix.


Q: basename কী?

A:
Generated URL names-এর base name।
এটা URL path নয়।


Q: detail=True কী?

A:
Specific object-এর জন্য action।
সাধারণত URL-এ pk থাকে।


Q: detail=False কী?

A:
Collection-level action।
Specific pk লাগে না।


Q: Custom endpoint কীভাবে বানাবো?

A:

@action(detail=True, methods=["post"])


Q: Create-এর custom save logic কোথায়?

A:

perform_create()


Q: Update-এর custom save logic কোথায়?

A:

perform_update()


Q: Delete-এর custom logic কোথায়?

A:

perform_destroy()


============================================================
                 ONE-LINE MEMORY TRICK
============================================================

ViewSet = WHAT actions

Router  = WHICH URLs

@action  = EXTRA endpoint

ModelViewSet =
list + create + retrieve + update +
partial_update + destroy


============================================================
             FINAL MENTAL MODEL
============================================================

Client
  |
  | GET /products/5/
  v
Router
  |
  | identifies URL + HTTP method
  v
ProductViewSet
  |
  | retrieve()
  v
Serializer
  |
  v
Model / Database
  |
  v
Response


Collection:
GET /products/       -> list()
POST /products/      -> create()

Detail:
GET /products/5/    -> retrieve()
PUT /products/5/    -> update()
PATCH /products/5/  -> partial_update()
DELETE /products/5/ -> destroy()

Custom:
POST /products/5/discount/ -> @action(detail=True)


============================================================
```
