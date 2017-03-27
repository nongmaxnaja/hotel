from netforce.model import Model,fields
class Level(Model):
    _name = "level"
    _string = "Level"
    _fields = {
        "price" : fields.Decimal("Price"),
         }
Level.register()
