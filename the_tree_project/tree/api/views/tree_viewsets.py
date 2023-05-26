from django.shortcuts import render

from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from tree.api.serializers.tree_serializers import TrunkSerializer
from tree.models import Trunk


class TrunkViewSet(viewsets.ModelViewSet):
    serializer_class = TrunkSerializer
    model_to_format = "Trunk"

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects

    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({'message': '[+] {} created successfully.'.format(self.model_to_format)}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message':'[*] {} deleted successfully.'.format(self.model_to_format)}, status=status.HTTP_200_OK)
