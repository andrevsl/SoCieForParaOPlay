from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

#app = Dash(__name__)
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
app.layout = html.Div()

app.layout = dbc.Container([
    html.Div(style={
        'width': 340,
        'margin-left': 35,
        'margin-top': 35,
        'margin-bottom': 35,
        'background-color': '#36f70f',
    }),
    html.Div(
        style={
            'width': 990,
            'margin-top': 35,
            'margin-right': 35,
            'margin-bottom': 35,
            'background-color': '#36f70f',
        })
],
    fluid=True,
    style={'display': 'flex'},
    className='dashboard-container')


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)