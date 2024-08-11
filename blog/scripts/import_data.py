from blog.models import Article
from decimal import Decimal

def run():
    for i in range(5,6):
        article = Article()
        article.title = f"Article N° #{i}"
        article.desc = f"Description Article N° #{i}"
        article.image = "http://default"
        article.price = Decimal("10.99")  # Set the price as a Decimal
     #   article.save()

    print("Opération réussie")
run()