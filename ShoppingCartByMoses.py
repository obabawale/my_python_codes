class ShoppingCart(object):  
  def __init__(self):
    self.total = 0
    self.items = {}
    
  def add_item(self, item_name, quantity, price):
    if item_name not in self.items:
      self.items[item_name] = quantity
    else:
      self.items[item_name] += quantity
    self.total += price * quantity
    
  def remove_item(self, item_name, quantity, price):

    if quantity > self.items[item_name]:
      self.total -= price * self.items[item_name]
      self.items.pop(item_name)
    else:
      self.items[item_name] -=  quantity
      self.total -= price * quantity

    
  def checkout(self, cash_paid):
    if cash_paid < self.total:
      return "Cash paid not enough"
    else:
      return cash_paid - self.total
        
class Shop(ShoppingCart):
  def __init__(self):
    super(Shop, self).__init__()
    self.quantity = 100    
    
  def remove_item(self, item_name=None, quantity=0, price=0):
    self.quantity -= 1