# Generated by Django 4.2.8 on 2024-02-11 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResetButton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wing_name', models.CharField(max_length=255)),
                ('squad_name', models.CharField(max_length=255)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.AddConstraint(
            model_name='resetbutton',
            constraint=models.UniqueConstraint(fields=('wing_name', 'squad_name'), name='unique_wing_squad'),
        ),
    ]
