from flask_wtf import FlaskForm
from wtforms import IntegerField, IntegerField, SubmitField, SelectField, StringField
from wtforms.validators import DataRequired, NumberRange

class QueryForm(FlaskForm):
    stock_graph = SubmitField('Get Stock Trends')
    currency_exchange = SubmitField('Get Exchange Rates')

class StockForm(FlaskForm):
    stock_name = StringField('Enter stock name',validators=[DataRequired()])
    intraday = SubmitField('Get Intraday analysis')
    daily = SubmitField('Get Daily analysis')
    monthly = SubmitField('Get Monthly analysis')
    weekly = SubmitField('Get Weekly analysis')

class CurrencyForm(FlaskForm):
    cur1 = StringField('Enter first currency')
    cur2 = StringField('Enter second currency')
    get_exchange_rate = SubmitField('Get exchange rates!')




