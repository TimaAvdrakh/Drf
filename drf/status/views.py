from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import Status
from .serializers import StatusSerializer

# Create your views here.
class StatusListSearchAPIView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get(self, request, format=None):
        queryset = Status.objects.all()
        serializer = StatusSerializer(queryset, many=   True)
        return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     data = request.data
    #     serializer = StatusSerializer(data, many = True)
    #     if serializer.is_valid():
    #         serializer.save()

class StatusApiView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]
    serializer_class = StatusSerializer

    def get_queryset(self):
        print(self.request.user)
        qs = Status.objects.all()
        # query = self.request.GET.get('q')
        # if query is not None:
        #     qs = qs.filter(content__icontains=query)
        return qs

    def perform_create(self, serializer):
        serializer.save(user = self.request.user)

class StatusDetailAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = []
    authentication_classes = []
    serializer_class = StatusSerializer
    lookup_field = 'id'
    # queryset = Status.objects.all()

    def get_queryset(self):
        object = Status.objects.all()
        return object