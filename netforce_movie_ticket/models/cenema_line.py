from netforce.model import Model,fields 
class CenemaLine(Model):
    _name = "cenema.line"
    _string = "Cenema"
    _fields = {
        "cenema_id": fields.Many2One("cenema","Cenema ID"),
        "movie_id": fields.Many2One("movie","Movie"),
         }
CenemaLine.register()
