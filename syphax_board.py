import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import pandas as pd

# Charger le fichier CSV
df = pd.read_csv('/home/ec2-user/Project_Linux/prix.csv', names=['prix'])

# Initialiser l'application Dash
app = dash.Dash(__name__)

# Définir le layout
app.layout = html.Div(children=[
    html.H1(children='Dernier prix du fichier CSV'),

    html.Div(id='price-div')
])

# Définir une callback pour renvoyer le dernier prix
@app.callback(Output('price-div', 'children'),
              [Input('interval-component', 'n_intervals')])
def display_price(n):
    last_price = df['prix'].iloc[-1]
    return f'Le dernier prix est {last_price}'

if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)
