# Generated by Django 4.0.6 on 2022-12-24 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Signup', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='registration_detail',
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('O1', models.CharField(max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Signup.questions')),
            ],
        ),
    ]
