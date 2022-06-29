from rest_framework import serializers, pagination
#model
from .models import Person, Reunion, Hobby

#hobby 
class HobbiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobby
        fields = ('__all__')

class PersonSerializer(serializers.ModelSerializer): #HyperlinkedModelSerializer
    """
    We do the same
    """
    hobbies = HobbiesSerializer(many=True)
    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
        )

#how to create a serializers that is not linked
class PersonaSerializer(serializers.Serializer):
    id = serializers.CharField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.EmailField()

#reunion
class ReunionSerializer(serializers.ModelSerializer):
    """
    This work only with foreing key ->
    when we use relationships in models the normal response will be the numer of the 
    relation, but if we want to show the fields of each relation we need to linked an exist
    serializer of that model to the serializers who have the relations
    "In this case we linked PersonaSerializer to the reunion to show all fields of person"
    """
    person = PersonaSerializer()
    #we can made methods to work with the fields declared
    date_time = serializers.SerializerMethodField()
    #class metta
    class Meta:
        model = Reunion
        fields = (
            'id',
            'date',
            'time',
            'affair',
            'person',
            'date_time',
        )
    def get_date_time(self,obj):
        return str(obj.date) + ' - ' + str(obj.time)

#with link -> Instead of making more longer the JSON we can redirect to an existing link of that model 
class ReunionSerializerLink(serializers.HyperlinkedModelSerializer):

    #class metta
    class Meta:
        model = Reunion
        fields = (
            'id',
            'date',
            'time',
            'affair',
            'person',
        )
        extra_kwargs  = {
            'person':{'view_name':'detail','lookup_field':'pk'}
        }

#with pagination
class PersonPagination(pagination.PageNumberPagination):
    page_size = 3
    max_page_size = 100
    

class CountReunionSerializer(serializers.Serializer):
    person__job = serializers.CharField()
    cantidad = serializers.IntegerField()