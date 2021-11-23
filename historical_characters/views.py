from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Character
from .permissions import IsAuthorOrReadOnly
from .serializer import CharacterSerializer

class CharacterList(ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer

class CharacterDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer