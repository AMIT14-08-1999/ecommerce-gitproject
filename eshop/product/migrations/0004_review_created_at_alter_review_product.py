# Generated by Django 4.1.7 on 2023-12-09 05:12

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product'),
        ),
    ]