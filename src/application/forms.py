from flask.ext.wtf import Form
from wtforms import TextField, validators

class EnterDBInfo(Form):
    dbNotes = TextField(label='Add entries to DB', description="db_enter", validators=[validators.required(), validators.Length(min=0, max=128, message=u'Enter 128 characters or less')])    

class RetrieveDBInfo(Form):
    numRetrieve = TextField(label='Input Number of DB entries to fetch', description="db_get", validators=[validators.required(), validators.Regexp('^\d{1}$',message=u'Enter a number between 1 and 10')])
