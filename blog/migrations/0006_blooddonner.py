# Generated by Django 4.2.2 on 2023-06-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('gender', models.BooleanField()),
                ('bloodgroup', models.CharField(max_length=32)),
                ('phone', models.BigIntegerField()),
            ],
        ),
    ]