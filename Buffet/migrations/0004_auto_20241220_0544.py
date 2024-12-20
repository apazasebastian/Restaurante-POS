# Generated by Django 2.2 on 2024-12-20 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buffet', '0003_auto_20201201_1917'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Acompaniante',
        ),
        migrations.DeleteModel(
            name='Bebida',
        ),
        migrations.RemoveField(
            model_name='pago',
            name='cliente',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='cliente',
        ),
        migrations.DeleteModel(
            name='Platillo',
        ),
        migrations.DeleteModel(
            name='Website',
        ),
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.CharField(choices=[('CR', 'Carne Roja'), ('CB', 'Carne Blanca'), ('P', 'Pasta'), ('G', 'Gaseosa'), ('CH', 'Con Alcohol'), ('SG', 'Sin Gas')], max_length=2),
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
        migrations.DeleteModel(
            name='Pago',
        ),
        migrations.DeleteModel(
            name='Pedido',
        ),
    ]
