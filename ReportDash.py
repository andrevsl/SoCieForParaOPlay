from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__)
app.layout = html.Div()
app.layout = dbc.Container(html.P("My awesome dashboard will be here."),
                           fluid=True,
                           className='dashboard-container')

if __name__ == "__main__":
    app.run_server(debug=True, port=8050)