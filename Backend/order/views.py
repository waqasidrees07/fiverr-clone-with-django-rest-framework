# order/views.py
from rest_framework import generics
from .models import Order
from .serializers import OrderSerializer
from gigs.models import Gig, BasicPackage, StandardPackage, PremiumPackage
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated


class OrderCreateView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer(self, *args, **kwargs):
        serializer = super(OrderCreateView, self).get_serializer(*args, **kwargs)
        gig_id = self.request.data.get('gig')
        if gig_id:
            gig = Gig.objects.filter(pk=gig_id).first()
            if gig:
                serializer.fields['package'].choices = self.get_available_packages(gig)
        return serializer

    def get_available_packages(self, gig):
        packages = []
        basic_packages = BasicPackage.objects.filter(gig=gig).values_list('name', 'name')
        standard_packages = StandardPackage.objects.filter(gig=gig).values_list('name', 'name')
        premium_packages = PremiumPackage.objects.filter(gig=gig).values_list('name', 'name')

        packages.extend(basic_packages)
        packages.extend(standard_packages)
        packages.extend(premium_packages)

        return [(package) for package in packages]

    def perform_create(self, serializer):
        gig_id = self.request.data.get('gig')
        gig = Gig.objects.filter(pk=gig_id).first()
        requested_user = self.request.user
        pkg_name = serializer.validated_data.get('package')
        quantity = serializer.validated_data.get('quantity')

        def get_package_by_name(name):
            try:
                pkg = BasicPackage.objects.get(name=pkg_name, gig=gig)
            except BasicPackage.DoesNotExist:
                try:
                    pkg = StandardPackage.objects.get(name=pkg_name, gig=gig)
                except StandardPackage.DoesNotExist:
                    try:
                        pkg = PremiumPackage.objects.get(name=pkg_name, gig=gig)
                    except PremiumPackage.DoesNotExist:
                        pkg = None

            return pkg
        pkg_price = get_package_by_name(pkg_name).price
        price = pkg_price * quantity

        serializer.save(user=requested_user, gig=gig, price=price)
