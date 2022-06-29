from django.shortcuts import render
#views
from django.views.generic import ListView, TemplateView
#REST
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView, DestroyAPIView, UpdateAPIView, RetrieveUpdateAPIView
#serializer
from .serealizers import PersonSerializer, PersonaSerializer, ReunionSerializer,ReunionSerializerLink,PersonPagination,CountReunionSerializer
#models
from .models import Person, Reunion


# Create your views here.

class PersonList(ListView):
    model = Person
    template_name = "person/people.html"
    context_object_name = 'people'

    def get_queryset(self):
        return Person.objects.all()

#using rest
class PersonListApiView(ListAPIView):
    #serealizers
    serializer_class = PersonSerializer
    #def
    def get_queryset(self):
        return Person.objects.all()

#example

class PersonView(TemplateView):
    template_name = "person/lista.html"

#another way
class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        #filter data
        kword = self.kwards['kword']
        return Person.objects.filter(
            full_name__icontains = kword
        )

#create
class PersonCreateView(CreateAPIView):
    #this recive a JSON and the is converted to python language
    serializer_class = PersonSerializer

#Equal to detail view
class PersonDetailView(RetrieveAPIView):
    #always serializers
    serializer_class = PersonSerializer
    #this views don't work with model, instead use queryset
    queryset = Person.objects.filter()

#delete
class PersonDestroyView(DestroyAPIView):

    serializer_class = PersonSerializer
    
    queryset = Person.objects.filter()

#update
class PersonUpdateView(RetrieveUpdateAPIView):

    serializer_class = PersonSerializer

    queryset = Person.objects.filter()

#with a not linked serializers
class PersonApiList(ListAPIView):
    #to interact
    serializer_class = PersonaSerializer
    def get_queryset(self):
        return Person.objects.all()

#reunion api
#with a not linked serializers
class ReunionApiList(ListAPIView):
    #to interact
    serializer_class = ReunionSerializer
    def get_queryset(self):
        return Reunion.objects.all()

#using the link
class ReunionApiListLink(ListAPIView):
    #to interact
    serializer_class = ReunionSerializerLink
    def get_queryset(self):
        return Reunion.objects.all()

#a list with pagination
class PersonApiListPaginated(ListAPIView):
    #to interact
    serializer_class = PersonSerializer
    pagination_class  = PersonPagination
    def get_queryset(self):
        return Person.objects.all()

class ReunionByJobs(ListAPIView):
    serializer_class = CountReunionSerializer

    def get_queryset(self):
        return Reunion.objects.cantidad_reunions_job()