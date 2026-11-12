from datetime import datetime, timedelta
from time import sleep

# * instanse method
# * @classmethod
# * static method




class Product:

    def __init__(self, product_name, price, off):
        self.product_name = product_name
        self.price = price
        self.off = off

    def __str__(self):
        return self.product_name



class Comment:
    # ? class method
    website_name = "lord.com"
    
    # ? instanse method
    def __init__(self, product, name, description, like, dislike):
        self.product = product
        self.name = name
        self.description = description
        self.date = datetime.now()
        self.like = like
        self.dislike = dislike

    def show(self):
        print("-^-"*15)
        print(f"product: {self.product}\n"
                f"name: {self.name}\n"
                f"description: {self.description}\n"
                f"date: {self.date}\n"
                f"👍: {self.like} 👎: {self.dislike}")
        print("---"*15)

    @classmethod
    def info(cls):
        print(cls.website_name)

    @classmethod
    def censorship(cls, product, name, description, like, dislike):
        print("the comment was censored!")
        description_edited = description.replace("fuck", "f**k")
        return cls(product, name, description_edited, like, dislike)

    @staticmethod
    def elapsed_time(time):
        sleep(3)
        print(datetime.now() - time)


dtf_print = Product("dtf", 0, 0)

c = Comment(dtf_print, "amir", "fuck you are a stupide", "2", "3")

Comment.info()
print()
c.show()
c2 = Comment.censorship(dtf_print, "amir", "fuck you are a stupide", "2", "3")
c2.show()

print(c2.date)

Comment.elapsed_time(c2.date - timedelta(days=2, hours=2))
