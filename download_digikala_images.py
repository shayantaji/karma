import os
import django
import requests

from io import BytesIO
from django.core.files import File


os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "Karma.settings"
)

django.setup()


from product.models import Product, ProductImage


headers = {
    "User-Agent": "Mozilla/5.0"
}


def get_digikala_product(title):

    url = (
        "https://api.digikala.com/v1/search/"
        f"?q={title}"
    )

    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )

    if response.status_code != 200:
        return None


    data = response.json()


    products = data["data"]["products"]


    if not products:
        return None


    return products[0]["id"]


def get_images(product_id):

    url = (
        f"https://api.digikala.com/v2/product/{product_id}/"
    )


    response = requests.get(
        url,
        headers=headers,
        timeout=15
    )


    if response.status_code != 200:
        return []


    data = response.json()


    images = data["data"]["product"]["images"]


    result = []


    main = images["main"]["url"]

    if main:
        result.append(main[0])


    for item in images["list"]:

        if len(result) >= 3:
            break

        result.append(
            item["url"][0]
        )


    return result


def download_image(url):

    response = requests.get(
        url,
        headers=headers,
        timeout=20
    )


    if response.status_code == 200:
        return BytesIO(response.content)

    return None



products = Product.objects.all()


for product in products:

    print(
        "\nProcessing:",
        product.title
    )


    if product.images.exists():

        print("Already has images")
        continue



    digikala_id = get_digikala_product(
        product.title
    )


    if not digikala_id:

        print("Not found")
        continue



    images = get_images(
        digikala_id
    )


    print(
        "Images found:",
        len(images)
    )



    for index, image_url in enumerate(images):


        file = download_image(
            image_url
        )


        if not file:
            continue



        image = ProductImage(
            product=product,
            is_main=(index == 0)
        )


        image.image.save(
            f"{product.slug}-{index}.jpg",
            File(file),
            save=True
        )


        print(
            "Saved image",
            index + 1
        )



print("\nDONE")