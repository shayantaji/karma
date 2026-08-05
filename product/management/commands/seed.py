from django.core.management.base import BaseCommand
from product.models import Product, ProductCategory, ProductBrand,ProductSpecification


class Command(BaseCommand):
    help = "Seed products database"


    def handle(self, *args, **kwargs):

        # =====================
        # Categories
        # =====================

        categories = {}

        category_data = [
            ("موبایل", "mobile"),
            ("لپ تاپ", "laptop"),
            ("هدفون", "headphone"),
            ("لوازم جانبی", "accessories"),
            ("مانیتور", "monitor"),
        ]


        for title, slug in category_data:

            category, _ = ProductCategory.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title
                }
            )

            categories[slug] = category



        # =====================
        # Brands
        # =====================

        brands = {}

        brand_data = [
            ("Samsung", "samsung"),
            ("Apple", "apple"),
            ("Xiaomi", "xiaomi"),
            ("Asus", "asus"),
            ("Lenovo", "lenovo"),
            ("HP", "hp"),
            ("Dell", "dell"),
            ("Sony", "sony"),
            ("JBL", "jbl"),
            ("Logitech", "logitech"),
        ]


        for title, slug in brand_data:

            brand, _ = ProductBrand.objects.get_or_create(
                slug=slug,
                defaults={
                    "title": title
                }
            )

            brands[slug] = brand



        # =====================
        # Products
        # =====================

        products = [

            # ================= MOBILE =================

            {
                "title": "Samsung Galaxy S25 Ultra",
                "slug": "samsung-galaxy-s25-ultra",
                "category": categories["mobile"],
                "brand": brands["samsung"],
                "short_description": "پرچمدار جدید سامسونگ با دوربین حرفه‌ای",
                "description": "گوشی پرچمدار سامسونگ با پردازنده قدرتمند و دوربین پیشرفته",
                "price": 120000000,
                "discount_percent": 5,
                "inventory": 15,
                "weight": 218,
                "is_special": True,
            },

            {
                "title": "iPhone 16 Pro Max",
                "slug": "iphone-16-pro-max",
                "category": categories["mobile"],
                "brand": brands["apple"],
                "short_description": "پرچمدار اپل",
                "description": "آخرین نسل آیفون با چیپ A18 Pro",
                "price": 150000000,
                "discount_percent": 0,
                "inventory": 10,
                "weight": 227,
                "is_special": True,
            },

            {
                "title": "Xiaomi 15 Ultra",
                "slug": "xiaomi-15-ultra",
                "category": categories["mobile"],
                "brand": brands["xiaomi"],
                "short_description": "گوشی پرچمدار شیائومی",
                "description": "گوشی قدرتمند با دوربین Leica",
                "price": 85000000,
                "discount_percent": 8,
                "inventory": 20,
                "weight": 220,
                "is_special": True,
            },

            {
                "title": "Samsung Galaxy A56",
                "slug": "samsung-galaxy-a56",
                "category": categories["mobile"],
                "brand": brands["samsung"],
                "short_description": "گوشی میان رده سامسونگ",
                "description": "گوشی اقتصادی با باتری قدرتمند",
                "price": 35000000,
                "discount_percent": 5,
                "inventory": 35,
                "weight": 198,
                "is_special": False,
            },

            {
                "title": "Redmi Note 14 Pro",
                "slug": "redmi-note-14-pro",
                "category": categories["mobile"],
                "brand": brands["xiaomi"],
                "short_description": "گوشی اقتصادی شیائومی",
                "description": "گوشی مناسب استفاده روزمره",
                "price": 25000000,
                "discount_percent": 10,
                "inventory": 40,
                "weight": 190,
                "is_special": False,
            },

            # ================= LAPTOP =================

            {
                "title": "Asus ROG Strix G16",
                "slug": "asus-rog-strix-g16",
                "category": categories["laptop"],
                "brand": brands["asus"],
                "short_description": "لپ تاپ گیمینگ ایسوس",
                "description": "مناسب بازی و کارهای سنگین",
                "price": 150000000,
                "discount_percent": 10,
                "inventory": 5,
                "weight": 2500,
                "is_special": True,
            },

            {
                "title": "Lenovo Legion 5",
                "slug": "lenovo-legion-5",
                "category": categories["laptop"],
                "brand": brands["lenovo"],
                "short_description": "لپ تاپ گیمینگ لنوو",
                "description": "قدرت پردازشی بالا",
                "price": 120000000,
                "discount_percent": 7,
                "inventory": 8,
                "weight": 2400,
                "is_special": False,
            },

            {
                "title": "HP Victus 16",
                "slug": "hp-victus-16",
                "category": categories["laptop"],
                "brand": brands["hp"],
                "short_description": "لپ تاپ اقتصادی گیمینگ",
                "description": "مناسب دانشجو و گیمر",
                "price": 90000000,
                "discount_percent": 5,
                "inventory": 12,
                "weight": 2300,
                "is_special": False,
            },

            {
                "title": "Dell XPS 15",
                "slug": "dell-xps-15",
                "category": categories["laptop"],
                "brand": brands["dell"],
                "short_description": "لپ تاپ حرفه ای دل",
                "description": "طراحی زیبا و سخت افزار قدرتمند",
                "price": 130000000,
                "discount_percent": 0,
                "inventory": 6,
                "weight": 1800,
                "is_special": True,
            },

            {
                "title": "MacBook Pro M4",
                "slug": "macbook-pro-m4",
                "category": categories["laptop"],
                "brand": brands["apple"],
                "short_description": "لپ تاپ حرفه ای اپل",
                "description": "مک بوک مجهز به چیپ M4",
                "price": 200000000,
                "discount_percent": 0,
                "inventory": 4,
                "weight": 1600,
                "is_special": True,
            },

            # ================= HEADPHONE =================

            {
                "title": "AirPods Pro 2",
                "slug": "airpods-pro-2",
                "category": categories["headphone"],
                "brand": brands["apple"],
                "short_description": "هندزفری بی سیم اپل",
                "description": "دارای نویز کنسلینگ فعال",
                "price": 18000000,
                "discount_percent": 5,
                "inventory": 25,
                "weight": 50,
                "is_special": True,
            },

            {
                "title": "Sony WH-1000XM5",
                "slug": "sony-wh-1000xm5",
                "category": categories["headphone"],
                "brand": brands["sony"],
                "short_description": "هدفون حرفه ای سونی",
                "description": "کیفیت صدای عالی",
                "price": 30000000,
                "discount_percent": 10,
                "inventory": 10,
                "weight": 250,
                "is_special": True,
            },

            {
                "title": "Galaxy Buds 3 Pro",
                "slug": "galaxy-buds-3-pro",
                "category": categories["headphone"],
                "brand": brands["samsung"],
                "short_description": "هندزفری سامسونگ",
                "description": "مناسب گوشی های گلکسی",
                "price": 12000000,
                "discount_percent": 5,
                "inventory": 30,
                "weight": 60,
                "is_special": False,
            },

            {
                "title": "JBL Tune 760NC",
                "slug": "jbl-tune-760nc",
                "category": categories["headphone"],
                "brand": brands["jbl"],
                "short_description": "هدفون JBL",
                "description": "صدای قدرتمند و باتری خوب",
                "price": 8000000,
                "discount_percent": 5,
                "inventory": 20,
                "weight": 220,
                "is_special": False,
            },

            # ================= accessories =================

            {
                "title": "Logitech MX Master 3S",
                "slug": "logitech-mx-master-3s",
                "category": categories["accessories"],
                "brand": brands["logitech"],
                "short_description": "ماوس حرفه ای",
                "description": "مناسب کارهای طراحی و اداری",
                "price": 9000000,
                "discount_percent": 5,
                "inventory": 15,
                "weight": 140,
                "is_special": False,
            },

            {
                "title": "شارژر GaN 65W",
                "slug": "gan-charger-65w",
                "category": categories["accessories"],
                "brand": None,
                "short_description": "شارژر سریع",
                "description": "شارژر کوچک و قدرتمند",
                "price": 3000000,
                "discount_percent": 0,
                "inventory": 50,
                "weight": 120,
                "is_special": False,
            },

            {
                "title": "کابل Type-C اصلی",
                "slug": "type-c-cable",
                "category": categories["accessories"],
                "brand": None,
                "short_description": "کابل شارژ",
                "description": "کابل مقاوم Type-C",
                "price": 700000,
                "discount_percent": 0,
                "inventory": 100,
                "weight": 80,
                "is_special": False,
            },

            {
                "title": "هاب USB چندکاره",
                "slug": "usb-hub",
                "category": categories["accessories"],
                "brand": None,
                "short_description": "هاب USB",
                "description": "افزایش پورت های لپ تاپ",
                "price": 2500000,
                "discount_percent": 5,
                "inventory": 20,
                "weight": 150,
                "is_special": False,
            },

        ]

        product_specs = {

            "usb-hub": [
                ("تعداد پورت", "4 پورت USB"),
                ("نوع اتصال", "USB 3.0"),
                ("جنس بدنه", "آلومینیوم"),
                ("سازگاری", "Windows / Mac"),
            ],

            "type-c-cable": [
                ("طول کابل", "1 متر"),
                ("نوع کانکتور", "Type-C"),
                ("قابلیت شارژ سریع", "دارد"),
                ("جنس", "روکش مقاوم"),
            ],

            "gan-charger-65w": [
                ("توان خروجی", "65 وات"),
                ("تکنولوژی", "GaN"),
                ("تعداد پورت", "2 پورت"),
                ("قابلیت شارژ سریع", "PD / QC"),
            ],

            "logitech-mx-master-3s": [
                ("نوع اتصال", "Bluetooth"),
                ("DPI", "8000"),
                ("تعداد کلید", "7 عدد"),
                ("باتری", "70 روز"),
            ],

            "jbl-tune-760nc": [
                ("نوع هدفون", "Over Ear"),
                ("حذف نویز", "Active Noise Canceling"),
                ("باتری", "35 ساعت"),
                ("اتصال", "Bluetooth 5.0"),
            ],

            "galaxy-buds-3-pro": [
                ("نوع اتصال", "Bluetooth"),
                ("حذف نویز", "ANC"),
                ("باتری", "30 ساعت"),
                ("مقاومت", "IP57"),
            ],

            "sony-wh-1000xm5": [
                ("نوع هدفون", "Over Ear"),
                ("باتری", "30 ساعت"),
                ("حذف نویز", "فعال"),
                ("وزن", "250 گرم"),
            ],

            "airpods-pro-2": [
                ("نوع اتصال", "Bluetooth"),
                ("تراشه", "Apple H2"),
                ("حذف نویز", "ANC"),
                ("شارژدهی", "6 ساعت"),
            ],

            "macbook-pro-m4": [
                ("پردازنده", "Apple M4"),
                ("رم", "16GB"),
                ("حافظه", "512GB SSD"),
                ("نمایشگر", "14 اینچ Liquid Retina"),
            ],

            "dell-xps-15": [
                ("پردازنده", "Intel Core i7"),
                ("رم", "16GB"),
                ("حافظه", "512GB SSD"),
                ("نمایشگر", "15.6 اینچ"),
            ],

            "hp-victus-16": [
                ("پردازنده", "Intel Core i7"),
                ("رم", "16GB"),
                ("کارت گرافیک", "RTX 4060"),
                ("حافظه", "1TB SSD"),
            ],

            "lenovo-legion-5": [
                ("پردازنده", "Ryzen 7"),
                ("رم", "16GB"),
                ("کارت گرافیک", "RTX 4060"),
                ("نمایشگر", "165Hz"),
            ],

            "asus-rog-strix-g16": [
                ("پردازنده", "Intel Core i9"),
                ("رم", "32GB"),
                ("کارت گرافیک", "RTX 4070"),
                ("حافظه", "1TB SSD"),
            ],

            "redmi-note-14-pro": [
                ("نمایشگر", "AMOLED"),
                ("رم", "12GB"),
                ("حافظه", "512GB"),
                ("باتری", "5500mAh"),
            ],

            "samsung-galaxy-a56": [
                ("نمایشگر", "Super AMOLED"),
                ("رم", "8GB"),
                ("حافظه", "256GB"),
                ("باتری", "5000mAh"),
            ],

            "xiaomi-15-ultra": [
                ("پردازنده", "Snapdragon 8 Elite"),
                ("رم", "16GB"),
                ("دوربین", "200MP"),
                ("باتری", "5410mAh"),
            ],

            "iphone-16-pro-max": [
                ("پردازنده", "Apple A18 Pro"),
                ("رم", "8GB"),
                ("حافظه", "256GB"),
                ("نمایشگر", "6.9 اینچ OLED"),
            ],

            "asus-rog-strix": [
                ("پردازنده", "Intel Core i7"),
                ("رم", "16GB"),
                ("کارت گرافیک", "RTX 4060"),
                ("حافظه", "1TB SSD"),
            ],

            "iphone-16-pro": [
                ("پردازنده", "Apple A18 Pro"),
                ("رم", "8GB"),
                ("حافظه", "256GB"),
                ("نمایشگر", "6.3 اینچ OLED"),
            ],

            "samsung-galaxy-s25-ultra": [
                ("پردازنده", "Snapdragon 8 Elite"),
                ("رم", "12GB"),
                ("حافظه", "512GB"),
                ("باتری", "5000mAh"),
            ],

        }

        for product_slug, specs in product_specs.items():

            try:

                product = Product.objects.get(slug=product_slug)

                for key, value in specs:
                    ProductSpecification.objects.get_or_create(
                        product=product,
                        key=key,
                        defaults={
                            "value": value
                        }
                    )

            except Product.DoesNotExist:

                print(f"Product not found: {product_slug}")



        for item in products:

            Product.objects.get_or_create(
                slug=item["slug"],
                defaults=item
            )


        self.stdout.write(
            self.style.SUCCESS(
                "25 sample products created successfully"
            )
        )