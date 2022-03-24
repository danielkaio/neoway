

from flask import Flask, render_template
import pandas as pd


app = Flask(__name__)


@app.route('/')
def index():
   return render_template('index.html')

@app.route('/leitura')
def leitura():
   pd.options.display.max_rows = 12000
   tabela = pd.read_csv('arquivo.csv', on_bad_lines='skip')
   
   return str(tabela)
 





if __name__ == "__main__":
  app.run(host='0.0.0.0')