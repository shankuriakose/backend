#   def create(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=201, headers=headers)

# from django.shortcuts import render,get_object_or_404
# from django.http import HttpResponse
# from rest_framework import viewsets, permissions, status
# from .serializers import ProfileSerializer
# from rest_framework.response import Response
# from .models import Profile
# from rest_framework.parsers import MultiPartParser, FormParser

# class ProfileViewset(viewsets.ModelViewSet):     
#     permission_classes = [permissions.AllowAny]
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     parser_classes = (MultiPartParser, FormParser)