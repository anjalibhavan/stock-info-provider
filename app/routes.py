from app import app
from flask import render_template,redirect,url_for
from app.forms import QueryForm, StockForm, CurrencyForm
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange 
import matplotlib.pyplot as plt
from io import BytesIO
import base64


APIKEY = 'JMW57D7IC9KO8SRP'
@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    myForm = QueryForm()
    if myForm.validate_on_submit():
        if myForm.stock_graph.data:
            return redirect(url_for('stockinfo'))
        elif myForm.currency_exchange.data:
            return redirect(url_for('exchange'))
    return render_template('base.html',form=myForm)


@app.route('/stockinfo', methods=['GET', 'POST'])
def stockinfo():
    stock_form = StockForm()
    if stock_form.validate_on_submit():
        if stock_form.daily.data:
            ts = TimeSeries(key=APIKEY, output_format='pandas')
            data, meta_data = ts.get_daily(symbol=stock_form.stock_name.data)
            sunalt = data['4. close'].plot().get_figure()
            buf = BytesIO()
            sunalt.savefig(buf, format='png')
            buf.seek(0)
            buffer = b''.join(buf)
            b2 = base64.b64encode(buffer)
            sunalt2=b2.decode('utf-8')
            return render_template('plotresults.html', sunalt=sunalt2)
            

        elif stock_form.intraday.data:
            ts = TimeSeries(key=APIKEY, output_format='pandas')
            data, meta_data = ts.get_intraday(symbol=stock_form.stock_name.data)
            sunalt = data['4. close'].plot().get_figure()
            buf = BytesIO()
            sunalt.savefig(buf, format='png')
            buf.seek(0)
            buffer = b''.join(buf)
            b2 = base64.b64encode(buffer)
            sunalt2=b2.decode('utf-8')
            return render_template('plotresults.html', sunalt=sunalt2)


        elif stock_form.weekly.data:
            ts = TimeSeries(key=APIKEY, output_format='pandas')
            data, meta_data = ts.get_weekly(symbol=stock_form.stock_name.data)
            sunalt = data['4. close'].plot().get_figure()
            buf = BytesIO()
            sunalt.savefig(buf, format='png')
            buf.seek(0)
            buffer = b''.join(buf)
            b2 = base64.b64encode(buffer)
            sunalt2=b2.decode('utf-8')
            return render_template('plotresults.html', sunalt=sunalt2)


        elif stock_form.monthly.data:
            ts = TimeSeries(key=APIKEY, output_format='pandas')
            data, meta_data = ts.get_monthly(symbol=stock_form.stock_name.data)
            sunalt = data['4. close'].plot().get_figure()
            buf = BytesIO()
            sunalt.savefig(buf, format='png')
            buf.seek(0)
            buffer = b''.join(buf)
            b2 = base64.b64encode(buffer)
            sunalt2=b2.decode('utf-8')
            return render_template('plotresults.html', sunalt=sunalt2)
            
    return render_template('stockinfo.html',form=stock_form)
    
@app.route('/exchange', methods=['GET', 'POST'])
def exchange():
    currency_form = CurrencyForm()
    if currency_form.validate_on_submit():
        cc = ForeignExchange(key=APIKEY)
        data, _ = cc.get_currency_exchange_rate(from_currency=currency_form.cur1.data,to_currency=currency_form.cur2.data)
        return render_template('curresults.html',res=data)
    return render_template('exchange.html',form=currency_form)
