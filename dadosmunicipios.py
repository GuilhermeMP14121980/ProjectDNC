import dash
from dash import dcc, html  # Importando componentes essenciais
import pandas as pd

# Inicializando a aplicação Dash
app = dash.Dash(__name__)

# Dados de exemplo (pode ser substituído por dados reais)
dados = {
    'Município': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte'],
    'População': [12300000, 6700000, 2600000],
    'Renda Per Capita': [3500, 4000, 3200]
}
df = pd.DataFrame(dados)

# Layout do dashboard
app.layout = html.Div([
    html.H1("Dashboard de Dados do Município", style={'textAlign': 'center'}),

    # Dropdown para selecionar o município
    html.Label("Selecione o município:"),
    dcc.Dropdown(
        id='dropdown-municipio',
        options=[{'label': municipio, 'value': municipio} for municipio in df['Município']],
        value='São Paulo'  # Valor inicial
    ),

    # Exibição de dados selecionados
    html.Div(id='output-dados', style={'marginTop': '20px'}),

    # Gráfico de exemplo
    dcc.Graph(
        id='grafico-populacao',
        figure={
            'data': [
                {'x': df['Município'], 'y': df['População'], 'type': 'bar', 'name': 'População'}
            ],
            'layout': {
                'title': 'População por Município',
                'xaxis': {'title': 'Município'},
                'yaxis': {'title': 'População'}
            }
        }
    )
])

# Callback para atualizar os dados do município selecionado
@app.callback(
    dash.dependencies.Output('output-dados', 'children'),
    [dash.dependencies.Input('dropdown-municipio', 'value')]
)
def atualizar_dados(municipio_selecionado):
    """
    Atualiza os dados exibidos com base no município selecionado.
    """
    if municipio_selecionado:
        dados_municipio = df[df['Município'] == municipio_selecionado].iloc[0]
        return html.Div([
            html.P(f"Município: {dados_municipio['Município']}"),
            html.P(f"População: {dados_municipio['População']}"),
            html.P(f"Renda Per Capita: R$ {dados_municipio['Renda Per Capita']}")
        ])
    return "Nenhum município selecionado."

# Inicializando o servidor
if __name__ == '__main__':
    app.run(debug=True)