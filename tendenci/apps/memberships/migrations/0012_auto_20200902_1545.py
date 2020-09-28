# Generated by Django 2.2.16 on 2020-09-02 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0011_membershipdefault_reminder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membershipapp',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='membershipapp',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='membershipdefault',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='membershipdefault',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='membershiptype',
            name='creator_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='membershiptype',
            name='owner_username',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='notice',
            name='creator_username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='owner_username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]