from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name ='URL',
            fields =[
                ('id',
                  models.AutoField(
                  auto_created = True,
                  primary_key = True,
                  serialize = False,
                  verbose_name ='ID'
                )),
                ('full_url',
                  models.URLField(
                  max_length = 200,
                )),
                ('url_hash',
                  models.URLField(
                  max_length = 200,
                )),
            ],
        ),
    ]
