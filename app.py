

from flask import Flask
import pandas as pd


app = Flask(__name__)


@app.route('/')
def leitura():
   pd.options.display.max_rows = 12000
   tabela = pd.read_csv('arquivo.csv', on_bad_lines='skip')
   
   return str(tabela)
 





if __name__ == "__main__":
  app.run(host='0.0.0.0')