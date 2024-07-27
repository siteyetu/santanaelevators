from application import db

class ProductTable(db.Document):
    product_id = db.SequenceField(primary_key=True)
    product_name = db.StringField(required=True)
    product_description = db.StringField(required=True)
    product_price = db.FloatField(required=True)
    product_category = db.StringField(required=True)
    product_image = db.URLField()
    product_quantity = db.IntField(required=True)
    created_at = db.DateTimeField()
    updated_at = db.DateTimeField()

class WishlistTable(db.Document):
    wishlist_id = db.SequenceField(primary_key=True)
    user_id = db.ReferenceField('UserTable', required=True)
    product_id = db.ReferenceField('ProductTable', required=True)
    created_at = db.DateTimeField()

class ShoppingCartTable(db.Document):
    cart_id = db.SequenceField(primary_key=True)
    user_id = db.ReferenceField('UserTable', required=True)
    product_id = db.ReferenceField('ProductTable', required=True)
    quantity = db.IntField(required=True)
    created_at = db.DateTimeField()
    updated_at = db.DateTimeField()

class CheckoutTable(db.Document):
    checkout_id = db.SequenceField(primary_key=True)
    user_id = db.ReferenceField('UserTable', required=True)
    cart_id = db.ReferenceField('ShoppingCartTable', required=True)
    shipping_address = db.StringField(required=True)
    payment_method = db.StringField(required=True)
    total_amount = db.FloatField(required=True)
    created_at = db.DateTimeField()

class InvoiceTable(db.Document):
    invoice_id = db.SequenceField(primary_key=True)
    checkout_id = db.ReferenceField('CheckoutTable', required=True)
    user_id = db.ReferenceField('UserTable', required=True)
    invoice_date = db.DateTimeField(required=True)
    invoice_amount = db.FloatField(required=True)
    payment_status = db.StringField(required=True)