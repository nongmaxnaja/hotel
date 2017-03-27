from netforce.model import Model,fields,get_model
class MovieTicket(Model):
    _name = "movie.ticket"
    _string = "MovieTicket"
    _fields = {
        "cenema_id" : fields.Many2One("cenema","Cenema ID", required=True,search=True),
        "movie_id" : fields.Many2One("movie","Movie",required=True,search=True),
        "seat_id" : fields.Many2One("seat","Seat",required=True,search=True),
        "price" : fields.Decimal("Price"),
        "count" : fields.Integer("Count",required=True),
        "amount" : fields.Decimal("Amount"),
        "contact_id" : fields.Many2One("contact","Contact",required=True),
        }


    def update_price(self,context={}):
        data = context['data']
        price = 0
        result = 0
        if data.get('cenema_id'):
            cenema = get_model("cenema").browse(data['cenema_id'])
            price += cenema.price or 0
        if data.get('movie_id'):
            movie = get_model("movie").browse(data['movie_id'])
            price += movie.price or 0
        if data.get('seat_id'):
            seat = get_model("seat").browse(data['seat_id'])
            price += seat.price or 0
        data['price'] = price
        if data.get('count'):
            result = price*data['count']
        data["amount"] = result
        return data

MovieTicket.register()
