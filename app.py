from flask import Flask, render_template
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import base64
from bs4 import BeautifulSoup 
import requests

#don't change this
matplotlib.use('Agg')
app = Flask(__name__) #do not change this

#insert the scrapping here
url_get = requests.get('https://www.coingecko.com/en/coins/ethereum/historical_data/usd?start_date=2020-01-01&end_date=2021-07-01#panel')
soup = BeautifulSoup(url_get.content,"html.parser")

#find your right key here
table = soup.find('tbody')
row = table.find_all('th', attrs={'class':'font-semibold text-center'})

row_length = len(row)

temp = [] #initiating a list 

for i in range(1, row_length):
#insert the scrapping process here
    
    #get Date
    Date = table.find_all('th', attrs={'class':'font-semibold text-center'})[i].text
    
    #get Market Cap
    Market_Cap = table.find_all('td', attrs={'class':'text-center'})[(4*i)].text.strip()
    
    #get Volume
    Volume = table.find_all('td', attrs={'class':'text-center'})[(4*i)+1].text.strip()
    
    #get Open
    Open = table.find_all('td', attrs={'class':'text-center'})[(4*i)+2].text.strip()
    
    #get Close
    Close = table.find_all('td', attrs={'class':'text-center'})[(4*i)+3].text.strip()
    
    temp.append((Date,Market_Cap,Volume,Open,Close))
    
temp = temp[::-1]

#change into dataframe
df = pd.DataFrame(temp, columns = ('Date','Market Cap','Volume','Open','Close'))

#insert data wrangling here
df2 = df.set_index("Date")
df2.plot()

#end of data wranggling 

@app.route("/")
def index(): 
	
	card_data = f'{data["____"].mean().round(2)}' #be careful with the " and ' 

	# generate plot
	ax = ____.plot(figsize = (20,9)) 
	
	# Rendering plot
	# Do not change this
	figfile = BytesIO()
	plt.savefig(figfile, format='png', transparent=True)
	figfile.seek(0)
	figdata_png = base64.b64encode(figfile.getvalue())
	plot_result = str(figdata_png)[2:-1]

	# render to html
	return render_template('index.html',
		card_data = card_data, 
		plot_result=plot_result
		)


if __name__ == "__main__": 
    app.run(debug=True)