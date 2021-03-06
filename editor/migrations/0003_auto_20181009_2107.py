# Generated by Django 2.1.2 on 2018-10-09 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0002_auto_20181009_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinet',
            name='brightness',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='color_temp_max',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='color_temp_min',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='fob_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='frame_frequency',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='greyscale',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='height',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='lifespan',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='module_h',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='module_res_h',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='module_res_w',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='module_w',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='pixel_pitch',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='power_max',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='power_typical',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='refresh_rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='resolution_h',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='resolution_w',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='view_angle_hor',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='view_angle_vert',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='weight',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='cabinet',
            name='width',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
