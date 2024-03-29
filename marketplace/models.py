from django.db import models

# Create your models here.
class ItemManager(models.Manager):
    def validate(self, postData):
        errors = {}
        if len(postData['item_name']) < 2:
            errors['item_name'] = "New item name must be at least 2 characters."
        for item in Item.objects.all():
            if postData['item_name'] == item.name:
                errors['unique_item_name'] = "An item with this name has already been created."
        if len(postData['item_description']) < 2:
            errors['item_description'] = "New item description must be at least 2 characters."
        return errors
    def validate_edit(self, postData):
        errors = {}
        if len(postData['item_name']) < 2:
            errors['item_name'] = "New item name must be at least 2 characters."
        if len(postData['item_description']) < 2:
            errors['item_description'] = "New item description must be at least 2 characters."
        return errors

class Cart(models.Model):
    user = models.ForeignKey('login_app.User', on_delete=models.CASCADE, related_name="cart")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self) -> str:
        return f"<Cart object: {self.user.first_name} ({self.id})>"

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    carbon_offset_in_trees = models.IntegerField()
    cost = models.DecimalField(max_digits=5, decimal_places=2)
    purchases = models.ManyToManyField('login_app.User', through="User_Item_Count")
    carts = models.ManyToManyField(Cart, through="Cart_Item_Count")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ItemManager()
    def __repr__(self) -> str:
        return f"<Item object: {self.name} ({self.id})>"

class User_Item_Count(models.Model):
    user = models.ForeignKey('login_app.User', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    orders = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self) -> str:
        return f"<User_Item_Count object: {self.user.first_name} {self.item.name} {self.orders} ({self.id})>"

class Cart_Item_Count(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, default=None)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __repr__(self) -> str:
        return f"<Cart Item object: {self.cart.user.first_name} {self.item.name} {self.quantity} ({self.id})>"

# class CategoryManager(models.Manager):
#     def validate(self, postData):
#         errors = {}
#         if len(postData['category_name']) < 2:
#             errors['category_name'] = "New category name must be at least 2 characters."
#         for category in Category.objects.all():
#             if postData['category_name'] == category.name:
#                 errors['unique_category_name'] = "A category with this name has already been created."
#         if len(postData['category_description']) < 2:
#             errors['category_description'] = "New category description must be at least 2 characters."
#         return errors
#     def validate_edit(self, postData):
#         errors = {}
#         if len(postData['category_name']) < 2:
#             errors['category_name'] = "New category name must be at least 2 characters."
#         if len(postData['category_description']) < 2:
#             errors['category_description'] = "New category description must be at least 2 characters."
#         return errors

# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     items = models.ManyToManyField(Item, related_name="categories")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     objects = CategoryManager()
#     def __repr__(self) -> str:
#         return f"<Category object: {self.name} {self.items} ({self.id})>"
