from django.core.management.base import BaseCommand
from store.models import Category, Product


class Command(BaseCommand):
    help = 'Populates the database with sample products'

    def handle(self, *args, **options):
        self.stdout.write('Creating sample data...')
        
        # Create Categories
        categories_data = [
            {'name': 'Electronics', 'description': 'Gadgets, devices, and electronic accessories'},
            {'name': 'Clothing', 'description': 'Fashion apparel for all occasions'},
            {'name': 'Home & Garden', 'description': 'Everything for your home and garden'},
            {'name': 'Sports', 'description': 'Sports equipment and outdoor gear'},
            {'name': 'Books', 'description': 'Books, magazines, and educational materials'},
        ]
        
        categories = {}
        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'description': cat_data['description']}
            )
            categories[cat_data['name']] = category
            if created:
                self.stdout.write(f'  Created category: {category.name}')
        
        # Create Products
        products_data = [
            # Electronics
            {
                'name': 'Wireless Bluetooth Headphones',
                'description': 'Premium noise-cancelling wireless headphones with 30-hour battery life. Features include active noise cancellation, comfortable over-ear design, and crystal-clear audio quality.',
                'price': 149.99,
                'category': 'Electronics',
                'stock': 50,
                'image_url': 'https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=400'
            },
            {
                'name': 'Smart Watch Pro',
                'description': 'Advanced fitness tracking smartwatch with heart rate monitor, GPS, and water resistance up to 50 meters. Compatible with iOS and Android.',
                'price': 299.99,
                'category': 'Electronics',
                'stock': 30,
                'image_url': 'https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=400'
            },
            {
                'name': 'Portable Bluetooth Speaker',
                'description': 'Compact and powerful portable speaker with 360-degree sound and 12-hour battery life. Perfect for outdoor adventures.',
                'price': 79.99,
                'category': 'Electronics',
                'stock': 100,
                'image_url': 'https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=400'
            },
            {
                'name': 'USB-C Fast Charger',
                'description': '65W USB-C power adapter with fast charging capability. Compatible with laptops, tablets, and smartphones.',
                'price': 39.99,
                'category': 'Electronics',
                'stock': 200,
                'image_url': 'https://images.unsplash.com/photo-1583394838336-acd977736f90?w=400'
            },
            
            # Clothing
            {
                'name': 'Classic Cotton T-Shirt',
                'description': 'Comfortable 100% cotton t-shirt available in multiple colors. Perfect for everyday casual wear.',
                'price': 24.99,
                'category': 'Clothing',
                'stock': 150,
                'image_url': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400'
            },
            {
                'name': 'Slim Fit Jeans',
                'description': 'Modern slim fit denim jeans with stretch comfort technology. Classic 5-pocket design.',
                'price': 59.99,
                'category': 'Clothing',
                'stock': 80,
                'image_url': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400'
            },
            {
                'name': 'Winter Jacket',
                'description': 'Warm and stylish winter jacket with down insulation. Water-resistant and windproof.',
                'price': 189.99,
                'category': 'Clothing',
                'stock': 40,
                'image_url': 'https://images.unsplash.com/photo-1544923246-77307dd628b7?w=400'
            },
            
            # Home & Garden
            {
                'name': 'Indoor Plant Set',
                'description': 'Set of 3 beautiful indoor plants in decorative ceramic pots. Low maintenance and air-purifying.',
                'price': 45.99,
                'category': 'Home & Garden',
                'stock': 60,
                'image_url': 'https://images.unsplash.com/photo-1485955900006-10f4d324d411?w=400'
            },
            {
                'name': 'LED Desk Lamp',
                'description': 'Adjustable LED desk lamp with multiple brightness levels and color temperatures. USB charging port included.',
                'price': 34.99,
                'category': 'Home & Garden',
                'stock': 90,
                'image_url': 'https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=400'
            },
            {
                'name': 'Cozy Throw Blanket',
                'description': 'Ultra-soft fleece throw blanket. Perfect for chilly evenings on the couch.',
                'price': 29.99,
                'category': 'Home & Garden',
                'stock': 120,
                'image_url': 'https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=400'
            },
            
            # Sports
            {
                'name': 'Yoga Mat Premium',
                'description': 'Extra thick non-slip yoga mat with carrying strap. Perfect for yoga, pilates, and floor exercises.',
                'price': 39.99,
                'category': 'Sports',
                'stock': 75,
                'image_url': 'https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?w=400'
            },
            {
                'name': 'Running Shoes',
                'description': 'Lightweight running shoes with responsive cushioning and breathable mesh upper.',
                'price': 119.99,
                'category': 'Sports',
                'stock': 55,
                'image_url': 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400'
            },
            {
                'name': 'Resistance Bands Set',
                'description': 'Set of 5 resistance bands with different tension levels. Perfect for home workouts.',
                'price': 19.99,
                'category': 'Sports',
                'stock': 200,
                'image_url': 'https://images.unsplash.com/photo-1598289431512-b97b0917affc?w=400'
            },
            
            # Books
            {
                'name': 'Python Programming Guide',
                'description': 'Comprehensive guide to Python programming for beginners and intermediate developers.',
                'price': 34.99,
                'category': 'Books',
                'stock': 100,
                'image_url': 'https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=400'
            },
            {
                'name': 'The Art of Web Design',
                'description': 'Modern web design principles and best practices. Includes real-world case studies.',
                'price': 44.99,
                'category': 'Books',
                'stock': 65,
                'image_url': 'https://images.unsplash.com/photo-1532012197267-da84d127e765?w=400'
            },
        ]
        
        for prod_data in products_data:
            category = categories[prod_data['category']]
            product, created = Product.objects.get_or_create(
                name=prod_data['name'],
                defaults={
                    'description': prod_data['description'],
                    'price': prod_data['price'],
                    'category': category,
                    'stock': prod_data['stock'],
                    'image_url': prod_data['image_url'],
                }
            )
            if created:
                self.stdout.write(f'  Created product: {product.name}')
        
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
