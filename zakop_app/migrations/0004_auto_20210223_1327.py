# Generated by Django 3.1.3 on 2021-02-23 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zakop_app', '0003_auto_20210223_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finding',
            name='tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='zakop_app.tag'),
        ),
    ]
