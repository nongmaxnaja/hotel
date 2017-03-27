from netforce.model import Model,fields
class Ticket(Model):
    _name = "movie.ticket"
    _fields = {
        "cenema" : fields.Selection([["majorceneplex lotus","Majorceneplex Lotus"],["majorceneplex ramkhamhaeng","Majorceneplex Ramkhamhaeng"],["paragon ceneplex","Paragon Ceneplex"]],"Cenema",required=True,search=True),
        "seat" : fields.Selection([["a","A"],["b","B"],["c","C"],["d","D"],["e","E"],["f","F"],["g","G"]],"Seat",required=True,search=True),
        #"level" : fields.Selection([["vip 280","VIP 280"],["120","120"]],"Level",required=True,search=True),
        "price" : fields.Decimal("Price"),
        "time" : fields.DateTime("Date/Time"),
        "movie" : fields.Selection([["beauty and the beast","Beauty and the Beast"],["avenger","Avenger"],["logan","Logan"]],"Movie",required=True,search=True),
         }
Ticket.register()
