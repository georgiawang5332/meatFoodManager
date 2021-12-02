# Generated by Django 3.2.5 on 2021-10-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mass_mer', '0004_auto_20211027_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_vendor',
            name='approved_date',
            field=models.DateTimeField(auto_now_add=True, help_text='', verbose_name='核准設立日期'),
        ),
        migrations.AlterField(
            model_name='food_vendor',
            name='cooperate_businmen',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='合作的中游商'),
        ),
        migrations.AlterField(
            model_name='food_vendor_person',
            name='address',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='food_vendor_person',
            name='vendors_stand_principal',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='攤位負責人'),
        ),
        migrations.AlterField(
            model_name='mass_mer',
            name='approved_date',
            field=models.DateTimeField(auto_now_add=True, help_text='', verbose_name='核准設立日期'),
        ),
        migrations.AlterField(
            model_name='mass_mer',
            name='cooperate_businmen',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='合作的中游商'),
        ),
        migrations.AlterField(
            model_name='mass_mer_person',
            name='address',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='mass_mer_person',
            name='mass_mer_principal',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='量販店負責人'),
        ),
        migrations.AlterField(
            model_name='other',
            name='approved_date',
            field=models.DateTimeField(auto_now_add=True, help_text='', verbose_name='核准設立日期'),
        ),
        migrations.AlterField(
            model_name='other',
            name='cooperate_businmen',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='合作的中游商'),
        ),
        migrations.AlterField(
            model_name='other_person',
            name='address',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='other_person',
            name='other_principal',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='其他負責人'),
        ),
        migrations.AlterField(
            model_name='retail_factory',
            name='approved_date',
            field=models.DateTimeField(auto_now_add=True, help_text='', verbose_name='核准設立日期'),
        ),
        migrations.AlterField(
            model_name='retail_factory',
            name='cooperate_businmen',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='合作的中游商'),
        ),
        migrations.AlterField(
            model_name='retail_factory_person',
            name='address',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='retail_factory_person',
            name='retail_factory_principal',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='工廠負責人'),
        ),
        migrations.AlterField(
            model_name='storefront',
            name='approved_date',
            field=models.DateTimeField(auto_now_add=True, help_text='', verbose_name='核准設立日期'),
        ),
        migrations.AlterField(
            model_name='storefront',
            name='cooperate_businmen',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='合作的中游商'),
        ),
        migrations.AlterField(
            model_name='storefront_person',
            name='address',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='地址'),
        ),
        migrations.AlterField(
            model_name='storefront_person',
            name='storefront_principal',
            field=models.CharField(blank=True, help_text='', max_length=255, verbose_name='店面負責人'),
        ),
    ]
