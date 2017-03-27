from netforce.model import Model,fields
class Seat(Model):
    _name = "seat"
    _string = "Seat"
    _name_field = "seat"
    _fields = {
        "seat" : fields.Char("Seat",required=True,search=True),
        "price" : fields.Decimal("Price",required=True,search=True),
        #"lines" : fields.One2Many("movie.line","seat_id","Lines",required=True,search=True),
        #"seat" : fields.Selection([["a","A"],["b","B"],["c","C"],["e","E"],["f","F"]],"Seat",required=True,search=True),
    }
Seat.register()
