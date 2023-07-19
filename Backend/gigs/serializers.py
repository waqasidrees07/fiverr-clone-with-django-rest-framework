from rest_framework import serializers
from .models import Gig, BasicPackage, StandardPackage, PremiumPackage


class BasicPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasicPackage
        exclude = ["gig"]


class StandardPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StandardPackage
        exclude = ["gig"]


class PremiumPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumPackage
        exclude = ["gig"]


class GigSerializer(serializers.ModelSerializer):
    basic_package = BasicPackageSerializer(required=False)
    standard_package = StandardPackageSerializer(required=False)
    premium_package = PremiumPackageSerializer(required=False)

    class Meta:
        model = Gig
        fields = (
            'title',
            'description',
            'images',
            'video',
            'document',
            'category',
            'sub_category',
            'service_type',
            'search_tags',
            'basic_package',
            'standard_package',
            'premium_package',
        )

    def create(self, validated_data):
        basic_package_data = validated_data.pop('basic_package', {})
        standard_package_data = validated_data.pop('standard_package', {})
        premium_package_data = validated_data.pop('premium_package', {})

        gig = Gig.objects.create(**validated_data)

        BasicPackage.objects.create(gig=gig, **basic_package_data)
        StandardPackage.objects.create(gig=gig, **standard_package_data)
        PremiumPackage.objects.create(gig=gig, **premium_package_data)

        return gig
