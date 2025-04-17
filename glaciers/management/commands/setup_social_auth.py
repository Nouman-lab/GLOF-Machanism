from django.core.management.base import BaseCommand
from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp

class Command(BaseCommand):
    help = 'Sets up social authentication'

    def handle(self, *args, **kwargs):
        # Create or update the site
        site, _ = Site.objects.get_or_create(
            id=1,
            defaults={
                'domain': '127.0.0.1:8000',
                'name': 'localhost'
            }
        )
        
        if site.domain != '127.0.0.1:8000':
            site.domain = '127.0.0.1:8000'
            site.name = 'localhost'
            site.save()

        # Create or update the social application
        social_app, created = SocialApp.objects.get_or_create(
            provider='google',
            name='Google',
            defaults={
                'client_id': '777783424102-5c5vo08ics35fhisrfief46mlouaingj.apps.googleusercontent.com',
                'secret': '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',
            }
        )

        # Make sure the site is in the social app's sites
        social_app.sites.add(site)

        self.stdout.write(self.style.SUCCESS('Successfully set up social authentication')) 