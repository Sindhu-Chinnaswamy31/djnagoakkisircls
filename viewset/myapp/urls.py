from django.urls import path, include
from myapp import views

app_name="myapp"
from rest_framework import routers

router=routers.DefaultRouter()
router.register('helloviewset',views.HelloViewset,basename="Hello Viewset")

urlpatterns = [
    path('sample/',views.SampleApiView.as_view(),name="Sample API View"),
    path('',include(router.urls)),
]