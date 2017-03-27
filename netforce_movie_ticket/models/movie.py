from netforce.model import Model,fields
class Movie(Model):
    _name = "movie"
    _string = "Movie"
    _name_field = "movie"
    _fields = {
        "movie" : fields.Char("Movie",required=True,search=True),
        "price" : fields.Decimal("Price",required=True,search=True),
        #"movie" : fields.Selection([["beauty and the beast","Beauty and the Beast"],["avenger","Avenger"],["logan","Logan"]],"Movie",required=True,search=True),
         }
Movie.register()
