from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sms_web", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sendsms",
            options={"ordering": ["-timestamp"], "verbose_name_plural": "sms"},
        ),
    ]
