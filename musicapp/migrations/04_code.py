
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '03_django'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='song_id',
            new_name='song',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='artiste_id',
            new_name='artiste',
        ),
    ]