import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from faker import Faker
from store.models import Category, Product, Banner
from scheduling.models import ServiceType, Service

class Command(BaseCommand):
    help = 'Seeds the database with initial data.'

    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting existing data...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        Banner.objects.all().delete()
        Service.objects.all().delete()
        ServiceType.objects.all().delete()

        self.stdout.write('Creating categories...')
        fake = Faker('pt_BR')
        categories = ['Ração', 'Brinquedos', 'Higiene', 'Acessórios', 'Farmácia']
        created_categories = []
        for category_name in categories:
            category, created = Category.objects.get_or_create(
                name=category_name,
                slug=slugify(category_name)
            )
            created_categories.append(category)

        self.stdout.write('Creating products...')
        for _ in range(25):
            product_name = fake.unique.word().capitalize() + ' ' + random.choice(categories)
            Product.objects.create(
                category=random.choice(created_categories),
                name=product_name,
                slug=slugify(product_name),
                description=fake.paragraph(nb_sentences=5),
                price=round(random.uniform(15.00, 350.00), 2),
                stock=random.randint(10, 100),
                is_featured=random.random() < 0.2, # 20% chance
                image='products/placeholder.png'
            )

        self.stdout.write('Creating banners...')
        # CORRECTION: Banners now correctly link to a random existing category.
        if created_categories: # Ensure categories exist before creating banners
            for i in range(3):
                Banner.objects.create(
                    title=f'Banner Promocional {i+1}',
                    image=f'banners/banner_{i+1}.png',
                    target_category=random.choice(created_categories), # Correct field
                    is_active=True
                )

        self.stdout.write('Creating service types...')
        grooming = ServiceType.objects.create(name='Grooming')
        vet = ServiceType.objects.create(name='Veterinary')

        self.stdout.write('Creating services...')
        Service.objects.create(
            service_type=grooming,
            name='Bath',
            description='A refreshing bath for your pet.',
            duration=30,
            price=50.00
        )
        Service.objects.create(
            service_type=grooming,
            name='Bath and Groom',
            description='A full grooming session for your pet.',
            duration=45,
            price=80.00
        )
        Service.objects.create(
            service_type=vet,
            name='Veterinary Consultation',
            description='A consultation with our expert veterinarians.',
            duration=30,
            price=120.00
        )

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database.'))