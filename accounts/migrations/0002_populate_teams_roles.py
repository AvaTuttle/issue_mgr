from django.db import migrations

def populate_teams_and_roles(apps):
    Team = apps.get_model('accounts', 'Team')
    Role = apps.get_model('accounts', 'Role')


    Team.objects.get_or_create(name="Alpha", description="The A team")
    Team.objects.get_or_create(name="Bravo", description="The B team")
    Team.objects.get_or_create(name="Charlie", description="The C team")


    Role.objects.get_or_create(name="developer")
    Role.objects.get_or_create(name="scrum master")
    Role.objects.get_or_create(name="product owner")

class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(populate_teams_and_roles),
    ]
