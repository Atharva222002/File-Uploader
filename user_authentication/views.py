from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


@api_view(['POST'])
def obtain_token(request):
    '''
        `Description`: Authenticates the user with the provided credentials and returns a token
        that can be used for subsequent API requests. If the user does not exist,
        a new user is created with the provided username and password.

        `Method`: POST

        `Parameters`:
            - request (HttpRequest): The HTTP request object containing the user credentials.

        `Returns`:
            Response: A JSON response containing the authentication token.

        `Example`:
            {
                "token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
            }
    '''
    username = request.data.get('username')
    password = request.data.get('password')

    user, created = User.objects.get_or_create(username=username)

    if created:
        user.set_password(password)
        user.save()

    user = authenticate(username=username, password=password)

    if user is not None:
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})

    return Response({'error': 'Invalid credentials'}, status=400)