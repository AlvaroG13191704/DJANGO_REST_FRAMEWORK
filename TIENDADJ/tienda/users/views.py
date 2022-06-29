#firebase
from firebase_admin import auth

#import views
from django.views.generic import TemplateView
#rest
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
#serializers
from .serializers import loginSocialSerializer
#users
from .models import User

# Create your views here.

class LoginUser(TemplateView):
    template_name = "users/login.html"

#using hte api
class GoogleLoginView(APIView):
    #serializers the token
    serializer_class = loginSocialSerializer
    #decode the token
    """
    If the request is right we can work, but if isn't we won't work
    """
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        #get the token from the frontend
        id_token = serializer.data.get('token_id')
        #decode
        decode_token = auth.verify_id_token(id_token)
        #now we can use the decode_token
        email = decode_token['email']
        name = decode_token['name']
        avatar = decode_token['picture']
        verified = decode_token['email_verified']
        #create the user
        user,created = User.objects.get_or_create(
            email = email,
            defaults= {
                'full_name':name,
                'email':email,
                'is_active':True
            }
        )
        #create own token 
        if created:
            token = Token.objects.create(user=user)
        else:
            token = Token.objects.get(user=user)
        #return the user
        userGet = {
            'id':user.pk,
            'email':user.email,
            'full_name':user.full_name,
            'genero':user.genero,
            'date_birth':user.date_birth,
            'city':user.city
        }
        return Response({
            'token':token.key,
            'user':userGet
        })