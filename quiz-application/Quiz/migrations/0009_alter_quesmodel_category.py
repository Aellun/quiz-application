# Generated by Django 5.0.4 on 2024-05-11 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0008_alter_quesmodel_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quesmodel',
            name='category',
            field=models.CharField(choices=[('programming', 'programming'), ('communication skills', 'Communication skills'), ('Emotional intelligennce', 'Emotional intelligennce'), ('Ethics', 'Ethics'), ('Customer Service', 'Customer Service')], max_length=100),
        ),
    ]