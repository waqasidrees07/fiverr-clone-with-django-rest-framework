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
    basic_package = BasicPackageSerializer()
    standard_package = StandardPackageSerializer()
    premium_package = PremiumPackageSerializer()

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

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.images = validated_data.get('images', instance.images)
        instance.video = validated_data.get('video', instance.video)
        instance.document = validated_data.get('document', instance.document)
        instance.category = validated_data.get('category', instance.category)
        instance.sub_category = validated_data.get('sub_category', instance.sub_category)
        instance.service_type = validated_data.get('service_type', instance.service_type)
        instance.search_tags = validated_data.get('search_tags', instance.search_tags)

        basic_package_data = validated_data.get('basic_package', {})
        basic_package = instance.basic_package
        basic_package.name = basic_package_data.get('name', basic_package.name)
        basic_package.description = basic_package_data.get('description', basic_package.description)
        basic_package.delivery = basic_package_data.get('delivery', basic_package.delivery)
        basic_package.pages = basic_package_data.get('pages', basic_package.pages)
        basic_package.revisions = basic_package_data.get('revisions', basic_package.revisions)
        basic_package.content_upload = basic_package_data.get('content_upload', basic_package.content_upload)
        basic_package.price = basic_package_data.get('price', basic_package.price)

        standard_package_data = validated_data.get('standard_package', {})
        standard_package = instance.standard_package
        standard_package.name = standard_package_data.get('name', standard_package.name)
        standard_package.description = standard_package_data.get('description', standard_package.description)
        standard_package.delivery = standard_package_data.get('delivery', standard_package.delivery)
        standard_package.pages = standard_package_data.get('pages', standard_package.pages)
        standard_package.revisions = standard_package_data.get('revisions', standard_package.revisions)
        standard_package.content_upload = standard_package_data.get('content_upload', standard_package.content_upload)
        standard_package.price = standard_package_data.get('price', standard_package.price)

        premium_package_data = validated_data.get('premium_package', {})
        premium_package = instance.premium_package
        premium_package.name = premium_package_data.get('name', premium_package.name)
        premium_package.description = premium_package_data.get('description', premium_package.description)
        premium_package.delivery = premium_package_data.get('delivery', premium_package.delivery)
        premium_package.pages = premium_package_data.get('pages', premium_package.pages)
        premium_package.revisions = premium_package_data.get('revisions', premium_package.revisions)
        premium_package.content_upload = premium_package_data.get('content_upload', premium_package.content_upload)
        premium_package.price = premium_package_data.get('price', premium_package.price)

        instance.save()
        basic_package.save()
        standard_package.save()
        premium_package.save()

        return instance


class GetGigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gig
        fields = '__all__'

    basic_package = BasicPackageSerializer()
    standard_package = StandardPackageSerializer()
    premium_package = PremiumPackageSerializer()
