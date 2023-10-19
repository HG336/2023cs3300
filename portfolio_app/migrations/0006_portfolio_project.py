# Generated by Django 4.2.5 on 2023-10-03 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio_app', '0005_remove_project_portfolio_delete_portfolio_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portfolio_app.student')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('portfolio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portfolio_app.portfolio')),
            ],
        ),
    ]
