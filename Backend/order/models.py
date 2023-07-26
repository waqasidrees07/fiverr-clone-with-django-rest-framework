from django.db import models
from authentication.models import MyUser
from gigs.models import Gig, BasicPackage, StandardPackage, PremiumPackage

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    gig = models.ForeignKey(Gig, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    @property
    def package_choices(self):
        available_packages = []
        basic_packages = BasicPackage.objects.filter(gig=self.gig).values_list('name', 'name')
        standard_packages = StandardPackage.objects.filter(gig=self.gig).values_list('name', 'name')
        premium_packages = PremiumPackage.objects.filter(gig=self.gig).values_list('name', 'name')

        available_packages.extend(basic_packages)
        available_packages.extend(standard_packages)
        available_packages.extend(premium_packages)

        return [(package[0], package[1]) for package in available_packages]

    package = models.CharField(max_length=1000, choices=())
    price = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self._meta.get_field('package').choices = self.package_choices

# ... other fields ...

    def __str__(self):
        return f"Order ID: {self.id} - User: {self.user} - Gig: {self.gig} - Package: {self.get_package_display()} - Quantity: {self.quantity}"
