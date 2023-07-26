from rest_framework import serializers
from .models import Order
from gigs.models import Gig, BasicPackage, StandardPackage, PremiumPackage


class OrderSerializer(serializers.ModelSerializer):
    gig = serializers.PrimaryKeyRelatedField(queryset=Gig.objects.all())
    package = serializers.ChoiceField(choices=[])

    class Meta:
        model = Order
        exclude = ['user', 'created_at', 'price']

    def get_package_choices(self, gig):
        packages = []
        basic_packages = BasicPackage.objects.filter(gig=gig).values_list('name', 'name')
        standard_packages = StandardPackage.objects.filter(gig=gig).values_list('name', 'name')
        premium_packages = PremiumPackage.objects.filter(gig=gig).values_list('name', 'name')

        packages.extend(basic_packages)
        packages.extend(standard_packages)
        packages.extend(premium_packages)

        return [(package) for package in packages]

    def to_representation(self, instance):
        gig = instance.gig
        self.fields['package'].choices = self.get_package_choices(gig)
        return super(OrderSerializer, self).to_representation(instance)
