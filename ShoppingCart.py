class ShoppingCart(object):
  
  def __init__(self):
    self.total = 0
    self.items = {}
    
  def add_item(self, item_name, quantity, price):
    """Add product to the cart."""
    if not item_name in self.items:
      self.items[item_name] = quantity
      self.total = self.total + price * quantity
    else:
      self.items[item_name] = self.items[item_name] + quantity
      self.total = self.total + price * quantity
    
  def remove_item(self, item_name, quantity, price):
    """Remove product from the cart."""
    if item_name in self.items:
      if quantity > self.items[item_name]:
        del self.items[item_name]
      else:
        self.items[item_name] = self.items[item_name] - quantity
        self.total = self.total - price * quantity
    else:
      print 'Item not in the cart'
    
  def checkout(self, cash_paid):
    if cash_paid < self.total:
      return "Cash paid not enough"
    else:
      return cash_paid - self.total
        
class Shop(ShoppingCart):
  def __init__(self):
    self.quantity = 100    
    
  def remove_item(self):
    self.quantity = self.quantity - 1
    return self.quantity