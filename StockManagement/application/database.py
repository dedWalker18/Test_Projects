from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import PrimaryKeyConstraint

# Creating a database variable to communicate with the database file! Using SQLAlchemy ORM for it
db = SQLAlchemy()

    
class Items(db.Model):
    __tablename__ = "Items"
    ItemId =  db.Column(db.Integer, primary_key = True, autoincrement = True)
    ItemName = db.Column(db.String, nullable = False)
    CostPerUnit = db.Column(db.Integer, nullable = False)
    Quantity =  db.Column(db.Integer, nullable = False)
        
class PurchaseOrders(db.Model):
    __tablename__ = "PurchaseOrders"
    OrderId = db.Column(db.Integer, primary_key = True, autoincrement = True)
    OrderDate = db.Column(db.Date, nullable = False)
    RecievedDate =  db.Column(db.Date)
    OrderDesc = db.Column(db.String)
    OrderInvoice = db.Column(db.String)
    TotalCost = db.Column(db.Integer, nullable = False)
    
class PurchaseLogs(db.Model):
    __tablename__ = "PurchaseLogs"
    LogId = db.Column(db.Integer, primary_key = True, autoincrement = True)
    ItemName = db.Column(db.String, db.ForeignKey(Items.ItemName), nullable = False)
    ItemQuantity = db.Column(db.Integer, nullable = False)
    Cost = db.Column(db.Integer, nullable = False)
    OrderId = db.Column(db.Integer, db.ForeignKey(PurchaseOrders.OrderId), nullable=False)
    
class SalesOrders(db.Model):
    __tablename__ = "SalesOrders"
    OrderId = db.Column(db.Integer, primary_key = True, autoincrement = True)
    OrderDate = db.Column(db.Date, nullable = False)
    DelieveryDate =  db.Column(db.Date)
    OrderDesc = db.Column(db.String)
    OrderInvoice = db.Column(db.String)
    TotalCost = db.Column(db.Integer, nullable = False)
    
class SalesLogs(db.Model):
    __tablename__ = "SalesLogs"
    LogId = db.Column(db.Integer, primary_key = True, autoincrement = True)
    ItemName = db.Column(db.String, db.ForeignKey(Items.ItemName), nullable = False)
    ItemQuantity = db.Column(db.Integer, nullable = False)
    Cost = db.Column(db.Integer, nullable = False)
    OrderId = db.Column(db.Integer, db.ForeignKey(SalesOrders.OrderId), nullable=False)