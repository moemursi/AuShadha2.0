# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-25 14:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_no', models.CharField(default='Tamil Nadu', max_length=200)),
                ('street_name', models.TextField()),
                ('city_or_town', models.CharField(default='Coimbatore', max_length=200)),
                ('district', models.CharField(default='Coimbatore', max_length=200)),
                ('state', models.CharField(default='Tamil Nadu', max_length=200)),
                ('country', models.CharField(default='India', max_length=200)),
                ('postal_code', models.CharField(max_length=200, verbose_name='Postal Code')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Clinic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_clinic', models.CharField(max_length=200)),
                ('nature_of_clinic', models.CharField(choices=[('primary_health_centre', 'Primary Health Centre'), ('community_health_centre', 'Community Health Centre'), ('poly_clinic', 'Poly Clinic'), ('speciality_clinic', 'Speciality Clinic'), ('district_hospital', 'District Hospital'), ('tertiary_referral_centre', 'Tertiary Referral Centre')], max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_department', models.CharField(max_length=100, unique=True)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(max_length=200)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Fax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fax_number', models.CharField(max_length=200)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.PositiveIntegerField(default=91)),
                ('area_code', models.PositiveIntegerField(default=422)),
                ('phone_number', models.PositiveIntegerField()),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clinic_staff_role', models.CharField(choices=[('non_clinical_staff', 'Non Clinical Staff'), ('secretary', 'Secretary'), ('clinic_admin', 'Clinic Administrator'), ('clinical_staff', 'Clinical Staff'), ('nurse', 'Nurse'), ('physio', 'Physiotherapist'), ('doctor', 'Doctor')], help_text=' This is the Role of the Staff in the Clinic', max_length=100, verbose_name='Staff Role')),
                ('aushadha_user_role', models.CharField(choices=[('audhadha_admin', 'AuShadha Admin'), ('aushadha_user', 'AuShadha User'), ('aushadha_staff', 'AuShadha Staff '), ('aushadha_developer', 'AuShadha Developer')], default='aushadha_user', help_text=' Users Role in AuShadha Software.\n                                                           This is different from the role in the Clinic', max_length=30, verbose_name='AuShadha User Role')),
                ('is_staff_hod', models.BooleanField(default=None, verbose_name='Is Staff Head of the Department')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Department')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website_address', models.CharField(max_length=200)),
                ('clinic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='address',
            name='clinic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinic.Clinic'),
        ),
    ]