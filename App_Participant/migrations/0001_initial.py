# Generated by Django 3.2.6 on 2021-10-07 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App_Event', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_reg_id', models.CharField(max_length=20)),
                ('participant_name', models.CharField(max_length=20)),
                ('participant_email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=20)),
                ('guests', models.IntegerField(blank=True, default=0, null=True)),
                ('fee_amount', models.FloatField(default=0.0)),
                ('payment_status', models.BooleanField(default=False)),
                ('transaction_id', models.CharField(blank=True, max_length=20, null=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_participant', to='App_Event.event')),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendence', models.BooleanField(default=False)),
                ('payment_status', models.BooleanField(default=False)),
                ('payment_amount', models.FloatField(default=0.0)),
                ('transaction_id', models.CharField(blank=True, max_length=20)),
                ('kit_token', models.BooleanField(default=False)),
                ('breakfast_token', models.BooleanField(default=False)),
                ('lunch_token', models.BooleanField(default=False)),
                ('snacks_token', models.BooleanField(default=False)),
                ('misc_token', models.BooleanField(default=False)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_participantstatus', to='App_Event.event')),
                ('participant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='participant_status', to='App_Participant.participant')),
            ],
            options={
                'verbose_name_plural': 'Participant Status',
            },
        ),
    ]
