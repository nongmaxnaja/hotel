from netforce.model import Model,fields
class Cenema(Model):
    _name = "cenema"
    _string = "Cenema"
    _name_field = "cenema"
    _fields = {
        "cenema" : fields.Char("Cenema",required=True,search=True),
        "price" : fields.Decimal("Price",required=True,search=True),
        "lines"  : fields.One2Many("cenema.line","cenema_id","Lines"), 
         }
Cenema.register()
