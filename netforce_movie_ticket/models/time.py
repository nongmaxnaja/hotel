from netforce.model import Model,fields
class Time(Model):
    _name = "time"
    _string = "Time"
    _fields = {
        "time" : fields.DateTime("Date/Time",required=True,search=True),
         }
Time.register()
