from . import views
from django.urls import path, include 

urlpatterns = [
    path('',views.PersonList.as_view(),name='listPerson'),
    path('api/persona/lista/',views.PersonListApiView.as_view(),),
    path('lista/',views.PersonView.as_view(),name='lista'),
    path('api/persona/search/<kword>/',views.PersonSearchApiView.as_view(),),
    path('api/persona/create/',views.PersonCreateView.as_view(),),
    path('api/persona/detail/<pk>/',views.PersonDetailView.as_view(),name='detail'),
    path('api/persona/delete/<pk>/',views.PersonDestroyView.as_view(),),
    path('api/persona/update/<pk>/',views.PersonUpdateView.as_view(),),
    #to interact
    path('api/personas/',views.PersonApiList.as_view(),),
    #reunion
    path('api/reunions/',views.ReunionApiList.as_view(),),
    #with link
    path('api/reunions/link',views.ReunionApiListLink.as_view(),),
    #paginated path
    path('api/person/paginated/',views.PersonApiListPaginated.as_view(),),
    #using manager
    path('api/reunion/jobs/',views.ReunionByJobs.as_view(),),



]