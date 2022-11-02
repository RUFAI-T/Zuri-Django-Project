
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', 'initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='artist',
            new_name='artiste',
        ),
    ]