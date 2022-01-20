from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('packages', '0009_auto_20220112_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='company_colors',
            field=models.CharField(default='Company Colors required', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='company_description',
            field=models.CharField(default='Company Description required', max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='company_look',
            field=models.CharField(default='Company Look required', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='company_name',
            field=models.CharField(default='Company Name required', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='package',
            name='company_slogan',
            field=models.CharField(default='Company Slogan required', max_length=200, null=True),
        ),
    ]
