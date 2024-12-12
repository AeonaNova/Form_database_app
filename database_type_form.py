from tinydb import TinyDB, Query
from schema import Date, Email, Phone

db = TinyDB('.db.json')

FormDB = Query()


class WriteToDb:
    _name: str

    def __init__(self, function):
        self.function = function
        self.gather = {}
        self.fields = str(self.function).split(' ')
        self.undefined_fields = function.__pydantic_extra__

    def write(self):
        pass

    def __str__(self):
        print(self._name)
        return str(self._name)


class SeparateForms(WriteToDb):

    def __init__(self, function):
        super().__init__(function)
        self.gather = {}

    def define(self):
        if self.function.origin_email and self.function.origin_date and self.function.origin_description and self.function.origin_phone_number:
            self._name = 'Form_all_known_fields_'
        elif self.function.origin_email and self.function.origin_date:
            self._name = 'Form_messaging_purpose'
        elif self.function.origin_phone_number and self.function.origin_description:
            self._name = 'Form_calling_purpose'
        elif self.function.origin_phone_number and self.function.origin_date:
            self._name = 'Form_connection_purpose'
        elif self.function.origin_phone_number:
            self._name = 'Form_registration_purpose'
        elif self.function.origin_date:
            self._name = 'Form_comments_purpose'
        elif self.function.origin_email:
            self._name = 'Form_help_purpose'
        else:
            self._name = 'Undefined_form'
        return self._name

    def check_in_existed(self):
        self.is_found = db.search(FormDB.name == self._name)
        return self.is_found

    def write(self):
        if not self.is_found and self._name != 'Undefined_form':
            db.insert({'name': self._name,
                       'fields': {field.split("=")[0]: field.split("=")[1] for field in list(self.fields)}
                       })
        return self._name

    def is_unknown(self):
        if self._name == 'Undefined_form':
            if not any([self.function.origin_email, self.function.origin_date, self.function.origin_description,
                        self.function.origin_phone_number]):
                self._gather = Undefined(self.function).parse()
            form_output = {'form_input_type': str(self._gather)}
        else:
            form_output = {'form_input_type': str(self._name)}
        return form_output


class Undefined(SeparateForms):

    def __init__(self, function):
        super().__init__(function)
        self._gather = {}
        self._name = 'Undefined_form'

    def parse(self):
        if self.undefined_fields.items:
            for field, value in self.undefined_fields.items():
                try:
                    Date.validate(str(value))
                    Email.validate(str(value))
                    Phone.validate(str(value))
                except Exception as e:
                    print(e, 'Type is not valid according applying schema')
                    unknown = {
                        f'{field}': str(type(value))
                    }
                    self._gather.update(unknown)
                    continue
        else:
            self._gather = type(self.undefined_fields)
        return self._gather


def get_from_db():
    all_form_types = db.all()
    return all_form_types
