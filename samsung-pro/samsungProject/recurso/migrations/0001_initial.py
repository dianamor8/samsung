# Generated by Django 4.1.1 on 2022-09-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_grade', models.CharField(choices=[('1EGB', '1ro. EGB'), ('2EGB', '2do. EGB'), ('3EGB', '3ro. EGB'), ('4EGB', '4to. EGB'), ('5EGB', '5to. EGB'), ('6EGB', '6to. EGB'), ('7EGB', '7mo. EGB')], max_length=100, verbose_name='schoolgrade')),
            ],
            options={
                'verbose_name': 'Grade',
                'verbose_name_plural': 'Grades',
            },
        ),
        migrations.CreateModel(
            name='LearningArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('MAT', 'Matemáticas'), ('LEN', 'Lenguaje'), ('ING', 'Inglés')], max_length=100, verbose_name='area')),
            ],
            options={
                'verbose_name': 'LearningArea',
                'verbose_name_plural': 'LearningAreas',
            },
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('description', models.CharField(max_length=250, verbose_name='description')),
                ('instruction', models.CharField(max_length=250, verbose_name='instruction')),
                ('pub_date', models.DateTimeField(auto_now=True, verbose_name='date_published')),
                ('link', models.CharField(max_length=250)),
                ('learning_areas', models.ManyToManyField(to='recurso.learningarea', verbose_name='areas')),
                ('school_grades', models.ManyToManyField(to='recurso.grade', verbose_name='grades')),
            ],
            options={
                'verbose_name': 'Resource',
                'verbose_name_plural': 'Resources',
            },
        ),
    ]
