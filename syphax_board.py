##importation des bibliotheques
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd

# charge  fichier CSV
df = pd.read_csv('/home/ec2-user/Project_Linux/prix.csv', names=['date', 'prix'])


# convertit colonne 'date'de notre csv  en datetime
df['date'] = pd.to_datetime(df['date'], format='%a %b %d %H:%M:%S %Z %Y')

df['jour'] = df['date'].dt.strftime('%Y-%m-%d') # extraire le jour de la colonne 'date'

df_grouped = df.groupby('jour').agg({'prix': ['mean', 'first', 'last']}) #regroupe les données de prix par jour

df_grouped.columns = ['prix_moyen', 'prix_ouverture', 'prix_cloture'] # renomme  les colonnes pour avoir des noms plus clairs

def lire_dernier_prix(csv_file): #fonction qui retourne le dernier prix de notre CSV
    dernier_prix = df.iloc[-1]['prix']
    return dernier_prix

###  graphique d'évolution du prix pour chaque jour
   #de telle sorte afin d'avoir un graphique pas condensée ou chaque date figure en abscisse ce qui rendrait le graph illisible 

fig = go.Figure()
for jour in df_grouped.index: #on parcourt chaque jour du datafram
    data = df.loc[df['jour'] == jour]
    fig.add_trace(go.Scatter(x=data['date'], y=data['prix'], mode='lines', name=jour)) #on affiche les données de chaque jour sur le meme graphique

fig.update_layout(title='Evolution du Solana ', xaxis_title='Heure et jour', yaxis_title='Prix')

#N.b : restez appuyez sur l'axe des abscisses et faites glisser pour visualiser l'ensemble des dates et heures des jours


## metriques calculées

# calcule  le prix mini et le prix maxi
prix_min = df['prix'].min()
prix_max = df['prix'].max()

rendement = (df_grouped.iloc[-1]['prix_ouverture'] - df_grouped.iloc[-1]['prix_cloture']) / df_grouped.iloc[-1]['prix_ouverture']
 #calcule rendement journalier  avec  (le prix d'ouverture - le dernier prix) / (prix d'ouverture)


volatilite = (prix_max - prix_min) / prix_max # calcule volatilite journaliere avec (le prix max - le prix min) / (prix max)

# le tableau  afficher les differents prix, rendements journalier et volatilité journaliere
table = html.Table([
    html.Tr([html.Th('Tableau de mesures récapitulatives', colSpan='4')]),
    html.Tr([html.Th('Prix minimum'), html.Td(f'{prix_min}')]),
    html.Tr([html.Th('Prix maximum'), html.Td(f'{prix_max}')]),
    html.Tr([html.Th('Prix douverture'), html.Td(f'{df_grouped.iloc[-1]["prix_ouverture"]}')]),
    html.Tr([html.Th('Prix de cloture'), html.Td(f'{df_grouped.iloc[-1]["prix_cloture"]}')]),
    html.Tr([html.Th('Rendement'), html.Td(f'{rendement*100:.1f}%')]), #rendement exprimé en % avec une decimale
    html.Tr([html.Th('Volatilité'), html.Td(f'{volatilite*100:.1f}%')]) #volatilité exprime de la meme facon avec une decimale
])

# pour application Dash
app = dash.Dash(__name__)


# dispositon  de notre app
app.layout = html.Div([
    html.H1("Cours du Solana",style={'text-align': 'center'}), 
    html.Div(id="output-dernier-prix", children=f"Le dernier prix est : {lire_dernier_prix('prix.csv')}",style={'text-align': 'center'}), 
    dcc.Graph(id='price-graph', figure=fig),
    html.Div(table, style={'display': 'flex', 'justify-content': 'center', 'margin': '20px auto'})
])




if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=8050)

