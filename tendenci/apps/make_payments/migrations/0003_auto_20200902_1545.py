# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_payments', '0002_makepayment_reference_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='makepayment',
            name='creator_username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='makepayment',
            name='owner_username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]