
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '02_Rename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lyric',
            old_name='song',
            new_name='song_id',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='artiste',
            new_name='artiste_id',
        ),
    ]