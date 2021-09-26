# Generated by Django 3.2.6 on 2021-09-26 04:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_Event', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('NONE', 'None')], default='NONE', max_length=20)),
                ('phone_no', models.CharField(blank=True, max_length=20)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_volunteer', to='App_Event.event')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='volunteer_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
