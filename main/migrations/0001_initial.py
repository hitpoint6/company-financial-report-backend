# Generated by Django 4.2 on 2023-08-14 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("name", models.CharField(max_length=100)),
                ("industry", models.CharField(max_length=100)),
                ("business_model", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("founder_quality", models.TextField()),
                ("feature_set", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Report",
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
                (
                    "revenue",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=10, null=True
                    ),
                ),
                (
                    "cash_burn",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=10, null=True
                    ),
                ),
                (
                    "gross_profit",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=10, null=True
                    ),
                ),
                (
                    "ebitda",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=10, null=True
                    ),
                ),
                (
                    "cash_on_hand",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=10, null=True
                    ),
                ),
                (
                    "cac",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=10, null=True
                    ),
                ),
                (
                    "ltv",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=10, null=True
                    ),
                ),
                (
                    "lacvtv",
                    models.DecimalField(
                        blank=True, decimal_places=1, max_digits=10, null=True
                    ),
                ),
                ("customer_count", models.IntegerField(blank=True, null=True)),
                ("next_fundraising", models.DateTimeField(blank=True, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.company"
                    ),
                ),
            ],
        ),
    ]