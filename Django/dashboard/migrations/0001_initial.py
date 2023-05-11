# Generated by Django 4.2 on 2023-05-09 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("userapp", "0002_alter_user_first_name_alter_user_last_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("category_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                ("product_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=255, unique=True)),
                ("description", models.TextField(null=True)),
                ("price", models.FloatField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SellOrder",
            fields=[
                ("sellsorder_id", models.AutoField(primary_key=True, serialize=False)),
                ("purchase_date", models.DateField(auto_now_add=True)),
                ("purchase_time", models.TimeField(auto_now_add=True)),
                ("total_price", models.FloatField()),
                ("total_qt", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.product",
                    ),
                ),
                (
                    "supplier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userapp.user"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="PurchaseOrder",
            fields=[
                (
                    "purchaseorder_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("purchase_date", models.DateField(auto_now_add=True)),
                ("purchase_time", models.TimeField(auto_now_add=True)),
                ("total_price", models.FloatField()),
                ("total_qt", models.IntegerField()),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="userapp.user"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="dashboard.product",
                    ),
                ),
            ],
        ),
    ]