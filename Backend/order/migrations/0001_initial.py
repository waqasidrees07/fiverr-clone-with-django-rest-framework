# Generated by Django 4.2.3 on 2023-07-25 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("gigs", "0002_alter_basicpackage_gig_alter_premiumpackage_gig_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quantity", models.PositiveIntegerField()),
                ("package", models.CharField(choices=[], max_length=1000)),
                ("price", models.DecimalField(decimal_places=2, max_digits=15)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "gig",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="gigs.gig"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]