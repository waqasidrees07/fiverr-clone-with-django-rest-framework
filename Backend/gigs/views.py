from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from .models import Gig, BasicPackage, StandardPackage, PremiumPackage
from .serializers import GigSerializer, BasicPackageSerializer, StandardPackageSerializer, PremiumPackageSerializer
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


class GigCreateView(generics.CreateAPIView):
    queryset = Gig.objects.all()
    serializer_class = GigSerializer
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        gig_serializer = self.get_serializer(data=request.data)
        gig_serializer.is_valid(raise_exception=True)

        try:
            self.perform_create(gig_serializer)
        except ValidationError as e:
            return self.handle_exception(e)

        headers = self.get_success_headers(gig_serializer.data)
        return Response(gig_serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, gig_serializer):
        gig_serializer.save(user=self.request.user)
        gig = gig_serializer.save()

        basic_package_serializer = BasicPackageSerializer(data=self.request.data.get('basic_package', {}))
        if basic_package_serializer.is_valid():
            BasicPackage.objects.create(gig=gig, **basic_package_serializer.validated_data)

        standard_package_serializer = StandardPackageSerializer(data=self.request.data.get('standard_package', {}))
        if standard_package_serializer.is_valid():
            StandardPackage.objects.create(gig=gig, **standard_package_serializer.validated_data)

        premium_package_serializer = PremiumPackageSerializer(data=self.request.data.get('premium_package', {}))
        if premium_package_serializer.is_valid():
            PremiumPackage.objects.create(gig=gig, **premium_package_serializer.validated_data)