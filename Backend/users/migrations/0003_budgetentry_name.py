# Generated by Django 4.2.5 on 2023-10-11 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_budget_budgetentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='budgetentry',
            name='name',
            field=models.CharField(default='gay', max_length=100),
            preserve_default=False,
        ),
    ]