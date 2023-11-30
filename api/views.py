from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework import serializers 
from .serializers import ProfileSerializer
from .models import Profile
from rest_framework.parsers import MultiPartParser, FormParser

from django.core.files.uploadedfile import InMemoryUploadedFile, TemporaryUploadedFile
from django.core.files.storage import FileSystemStorage




class ProfileViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    parser_classes = (MultiPartParser, FormParser)

    def list(self, request):
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, pk=None):
        profile = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(profile)
        return Response(serializer.data)

    # def update(self, request, pk=None):
    #     profile = get_object_or_404(self.queryset, pk=pk)
    #     old_picture = profile.picture  # Save reference to old picture
    #     print(request.data)
    #     serializer = self.serializer_class(profile, data=request.data)

    #     try:
    #         serializer.is_valid(raise_exception=True)

    #         # Delete old picture if it exists
    #         if old_picture:
    #             old_picture.delete()

    #         serializer.save()
    #         return Response(serializer.data)
    #     except serializers.ValidationError as e:
    #         print(e.detail)  # Print validation errors to console
    #         return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
    #     except Exception as e:
    #         return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
   
  
    def update(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)
        old_picture = profile.picture
        picture_value = request.data['picture']

        # if isinstance(picture_value, str) and (picture_value.startswith('http://') or picture_value.startswith('https://')):
        
        # Check if 'picture' is a file object
        if 'picture' in request.data and isinstance(request.data['picture'], ( InMemoryUploadedFile, TemporaryUploadedFile)):
            if old_picture:
                old_picture.delete()
            # Update 'picture' field with the new file
            profile.picture = picture_value
            picture_changed = True
            serializer = self.serializer_class(profile, data=request.data)
            picture_changed = True
        else:
            print(request.data)
            #  Manually filter out the 'picture' field from request.data
            filtered_data = {k: v for k, v in request.data.items() if k != 'picture'}
            serializer = ProfileSerializer(profile, data=filtered_data, partial=True)
                
       


        try:
            serializer.is_valid(raise_exception=True)

            if serializer.validated_data or picture_changed:
                serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)
        except serializers.ValidationError as e:
            return Response({"errors": e.detail}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


        
 

    def destroy(self, request, pk=None):
        profile = get_object_or_404(Profile, pk=pk)

        # Delete the media file associated with the profile
        fs = FileSystemStorage()
        fs.delete(profile.picture.name)
        # Delete the Profile instance
        profile.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)