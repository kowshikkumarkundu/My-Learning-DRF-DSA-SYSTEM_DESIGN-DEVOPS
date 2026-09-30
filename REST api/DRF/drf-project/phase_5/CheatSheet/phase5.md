# DRF PHASE 5 — VIEWSETS & ROUTERS CHEATSHEET


1. VIEWSET


ViewSet = একটি resource-এর related API actions এক class-এর
মধ্যে organize করার abstraction।

Basic ModelViewSet:

from rest_framework.viewsets import ModelViewSet

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer



2. ModelViewSet ACTIONS


GET     /products/       -> list()
POST    /products/       -> create()

GET     /products/5/     -> retrieve()
PUT     /products/5/     -> update()
PATCH   /products/5/     -> partial_update()
DELETE  /products/5/     -> destroy()


ModelViewSet provides:

list()
create()
retrieve()
update()
partial_update()
destroy()



3. ROUTER


Router ViewSet-এর জন্য automatically URL routes generate করে।

Example:

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    "products",
    ProductViewSet,
    basename="product"
)


URL include করতে হবে:

from django.urls import path, include

urlpatterns = [
    path("", include(router.urls)),
]



4. COMPLETE VIEWSET + ROUTER


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



5. router.register()


router.register(
    "products",
    ProductViewSet,
    basename="product"
)


"products"
    -> URL prefix

ProductViewSet
    -> কোন ViewSet route handle করবে

basename="product"
    -> generated URL names-এর base


IMPORTANT:

"products" model name থেকেই আসতে হবে এমন নয়।

Example:

router.register(
    "items",
    ProductViewSet,
    basename="product"
)

URLs:

/items/
/items/5/



6. basename


basename URL path নয়।

Example:

router.register(
    "kowshik",
    ProductViewSet,
    basename="product"
)


Result:

URL prefix = kowshik
basename   = product

URLs:

/kowshik/
/kowshik/5/


basename মূলত generated URL names-এর জন্য ব্যবহৃত হয়।



7. DefaultRouter


from rest_framework.routers import DefaultRouter

router = DefaultRouter()


DefaultRouter:

- automatically routes generate করে
- API root তৈরি করে
- standard DRF API-এর জন্য convenient



8. SimpleRouter


from rest_framework.routers import SimpleRouter

router = SimpleRouter()


SimpleRouter basic routes generate করে।

DefaultRouter-এর API root থাকে,
SimpleRouter-এর API root থাকে না।


Easy memory:

DefaultRouter = routes + API root
SimpleRouter  = routes



9. ReadOnlyModelViewSet


শুধু read operation দরকার হলে:

from rest_framework.viewsets import ReadOnlyModelViewSet

class ProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


Provides:

list()
retrieve()


Allowed:

GET /products/
GET /products/5/


Not provided:

POST
PUT
PATCH
DELETE



10. ModelViewSet vs ReadOnlyModelViewSet


ModelViewSet:

list
create
retrieve
update
partial_update
destroy


ReadOnlyModelViewSet:

list
retrieve



11. @action


Standard CRUD-এর বাইরে custom endpoint তৈরি করতে
@action ব্যবহার করা হয়।

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



12. detail=True


detail=True = specific object-এর জন্য action।

Example:

@action(detail=True, methods=["post"])
def discount(self, request, pk=None):
    ...


URL:

/products/5/discount/


এখানে pk পাওয়া যাবে।


Mental model:

products
    |
    v
specific product
    |
    v
pk = 5



13. detail=False


detail=False = collection-level action।

Example:

@action(detail=False, methods=["get"])
def featured(self, request):
    return Response(...)


URL:

GET /products/featured/


এখানে specific pk নেই।



14. Multiple HTTP Methods in @action


@action(
    detail=True,
    methods=["get", "post"]
)
def something(self, request, pk=None):
    ...


Routes:

GET  /products/5/something/
POST /products/5/something/



15. url_path


Defaultভাবে method name URL path হিসেবে ব্যবহৃত হয়।

Example:

@action(detail=True, methods=["post"])
def apply_discount(self, request, pk=None):
    ...


URL:

/products/5/apply_discount/


Custom path:

@action(
    detail=True,
    methods=["post"],
    url_path="discount"
)
def apply_discount(self, request, pk=None):
    ...


URL:

/products/5/discount/



16. url_name


Generated URL name customize করা যায়।

Example:

@action(
    detail=True,
    methods=["post"],
    url_path="discount",
    url_name="product-discount"
)
def apply_discount(self, request, pk=None):
    ...


url_name মূলত URL reversing/naming-এর জন্য।



17. self.action


ViewSet-এর current action জানতে:

self.action


Possible values:

list
create
retrieve
update
partial_update
destroy
custom_action_name


Example:

def get_queryset(self):

    if self.action == "list":
        return Product.objects.all()

    return Product.objects.filter(
        owner=self.request.user
    )



18. get_queryset()


Dynamic queryset-এর জন্য ব্যবহার করা হয়।

Example:

def get_queryset(self):
    return Product.objects.filter(
        owner=self.request.user
    )


Static:

queryset = Product.objects.all()


Dynamic:

def get_queryset(self):
    ...


Use case:

User A
    -> নিজের products

User B
    -> নিজের products



19. get_serializer_class()


Different action-এর জন্য different serializer ব্যবহার করা যায়।

Example:

def get_serializer_class(self):

    if self.action == "discount":
        return DiscountSerializer

    return ProductSerializer


Result:

/products/
    -> ProductSerializer

/products/5/discount/
    -> DiscountSerializer



20. get_object()


Specific object retrieve করতে:

product = self.get_object()


Example:

@action(
    detail=True,
    methods=["post"]
)
def discount(self, request, pk=None):

    product = self.get_object()

    product.discount = 100
    product.save()

    return Response({
        "message": "Discount applied"
    })


detail=True action-এ self.get_object()
current object retrieve করতে পারে।



21. perform_create()


Create-এর সময় custom save logic।

Example:

def perform_create(self, serializer):
    serializer.save(
        owner=self.request.user
    )


Flow:

POST
  |
  v
create()
  |
  v
serializer validation
  |
  v
perform_create()
  |
  v
serializer.save()
  |
  v
Database



22. perform_update()


Update-এর সময় custom save logic।

Example:

def perform_update(self, serializer):
    serializer.save(
        updated_by=self.request.user
    )



23. perform_destroy()


Delete-এর সময় custom logic।

Example:

def perform_destroy(self, instance):
    instance.delete()


Custom delete logic থাকলে এখানে করা যায়।



24. CUSTOM ACTION + DIFFERENT SERIALIZER


Example serializer:

class DiscountSerializer(serializers.Serializer):
    discount = serializers.IntegerField(min_value=0)


ViewSet:

class ProductViewSet(ModelViewSet):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_serializer_class(self):

        if self.action == "discount":
            return DiscountSerializer

        return ProductSerializer

    @action(
        detail=True,
        methods=["post"]
    )
    def discount(self, request, pk=None):

        serializer = self.get_serializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        return Response(
            serializer.validated_data
        )



25. REALISTIC VIEWSET


class ProductViewSet(ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(
            owner=self.request.user
        )

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )

    @action(
        detail=True,
        methods=["post"]
    )
    def discount(self, request, pk=None):

        product = self.get_object()

        product.discount = 100
        product.save()

        return Response({
            "message": "Discount applied"
        })


এখানে একসাথে ব্যবহার হয়েছে:

ModelViewSet
get_queryset()
perform_create()
@action
get_object()



26. ViewSet vs Generic Views


APIView:

Maximum manual control।

Example:

class ProductView(APIView):

    def get(self, request):
        ...

    def post(self, request):
        ...


Generic Views:

Standard CRUD + customization।

Examples:

ListCreateAPIView
RetrieveUpdateDestroyAPIView


ViewSet:

Resource-based CRUD।

Example:

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


Router automatically URLs generate করে।



27. ABSTRACTION LADDER


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
Maximum control


GenericAPIView + Mixins:
Reusable CRUD building blocks


Concrete Generic Views:
Standard CRUD-এর ready-made views


ViewSet + Router:
Resource-based API-এর compact abstraction



28. কখন কোনটা ব্যবহার করব?


APIView:

Highly custom API flow হলে।


Generic Views:

Standard CRUD দরকার কিন্তু কিছু custom control দরকার হলে।


ViewSet:

Resource-based standard CRUD API হলে এবং
router দিয়ে standard REST routes generate করতে চাইলে।


Examples:

Product
Order
Category
User



29. REQUEST FLOW


Example:

GET /products/5/

Client
  |
  v
Router
  |
  | URL + HTTP Method identify করে
  v
ProductViewSet
  |
  | retrieve()
  v
get_queryset()
  |
  v
get_object()
  |
  v
Serializer
  |
  v
Database
  |
  v
Response



30. VIEWSET + ROUTER MENTAL MODEL


                    Router
                       |
                       | URL + HTTP Method
                       v
                  ViewSet Action
                       |
          +------------+------------+
          |            |            |
          v            v            v
       list()       create()    retrieve()
          |            |            |
         GET          POST       GET /pk


Detail actions:

PUT    -> update()
PATCH  -> partial_update()
DELETE -> destroy()


Custom:

@action -> custom endpoint



31. MOST IMPORTANT ROUTE MAPPING


GET     /products/       -> list()
POST    /products/       -> create()

GET     /products/5/     -> retrieve()
PUT     /products/5/     -> update()
PATCH   /products/5/     -> partial_update()
DELETE  /products/5/     -> destroy()

POST    /products/5/discount/
        -> custom @action



32. QUICK RECALL


ViewSet কী?

Resource-এর related API actions এক class-এ organize
করার abstraction।


ModelViewSet কী দেয়?

list
create
retrieve
update
partial_update
destroy


ReadOnlyModelViewSet কী দেয়?

list
retrieve


Router কী করে?

ViewSet-এর actions-এর জন্য automatically URL routes
generate করে।


register()-এর first argument?

URL prefix।


basename?

Generated URL names-এর base name।


detail=True?

Specific object।


detail=False?

Collection-level।


Custom endpoint?

@action(...)


Dynamic queryset?

get_queryset()


Different serializer?

get_serializer_class()


Create customization?

perform_create()


Update customization?

perform_update()


Delete customization?

perform_destroy()


Current ViewSet action?

self.action


Current object?

self.get_object()



33. ONE-LINE MEMORY TRICK


ViewSet = WHAT actions

Router = WHICH URLs

@action = EXTRA endpoint

get_queryset() = WHICH objects

get_serializer_class() = WHICH serializer

perform_create() = CREATE customization

perform_update() = UPDATE customization

perform_destroy() = DELETE customization



34. PHASE 5 COMPLETION CHECKLIST


[✓] ViewSet
[✓] ModelViewSet
[✓] ReadOnlyModelViewSet
[✓] DefaultRouter
[✓] SimpleRouter
[✓] router.register()
[✓] basename
[✓] @action
[✓] detail=True
[✓] detail=False
[✓] url_path
[✓] url_name
[✓] self.action
[✓] get_queryset()
[✓] get_serializer_class()
[✓] get_object()
[✓] perform_create()
[✓] perform_update()
[✓] perform_destroy()
[✓] ViewSet vs Generic Views
[✓] Abstraction choice
[✓] Request -> Router -> ViewSet -> Serializer -> DB -> Response



PHASE 5 COMPLETE


NEXT:
PHASE 6 — AUTHENTICATION & PERMISSIONS

Topics:

- Authentication vs Authorization
- Session Authentication
- Basic Authentication
- Token Authentication
- JWT
- Access Token
- Refresh Token
- Token Expiry
- Authentication Flow
- AllowAny
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly
- Custom Permissions
- Object-level Permissions
- Roles & Permission Design