from netforce.model import Model,fields

class Contact(Model):
    _inherit = "contact"
    _fields = {
        "code" : fields.Char("ID Card",search=True),
        "title" : fields.Selection([["Mr","Mr."],["Mrs","Mrs."],["Miss","Miss."]],"Title", required=True, search=True),
        }

    def name_get(self, ids, context={}):
        vals = []
        for obj in self.browse(ids):
            if obj.title:
                name = "[%s] %s" % (obj.title, obj.name)
            else:
                name = obj.name
            vals.append((obj.id, name, obj.image))
        return vals

Contact.register()
