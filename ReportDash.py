from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import numpy as np
import random
#app = Dash(__name__)
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
fig = go.Figure(
    go.Scattergl(
        x = np.random.randn(1000),
        y = np.random.randn(1000),
        mode='markers',
        marker=dict(color=random.sample(['#ecf0f1']*500 + ["#3498db"]*500, 1000), line_width=1)
    )
)
fig.update_layout(plot_bgcolor='#010103', width=790, height=730,
                  xaxis_visible=False, yaxis_visible=False, showlegend=False, margin=dict(l=0,r=0,t=0,b=0))

app.layout = dbc.Container([
    html.Div(html.Div([
            html.H1([
                html.Span("Welcome"),
                html.Br(),
                html.Span("to my beautiful dashboard!")
            ]),
            html.
            P("This dashboard prototype shows how to create an effective layout."
              )
        ],
                 style={"vertical-alignment": "top", "height": 260}),
        
        style={
        'width': 340,
        'margin-left': 35,
        'margin-top': 35,
        'margin-bottom': 35
    }),
    html.Div(
           [
            html.Div(
                dcc.Graph(
                    figure=fig
                ),
                     style={'width': 790}),
            html.Div([
                html.H2('Output 1:'),
                html.Div(className='Output'),
                html.H2('Output 2:'),
                html.Div(html.H3("Selected Value"), className='Output')
            ], style={'width': 198})
        ],
        style={
            'width': 990,
            'margin-top': 35,
            'margin-right': 35,
            'margin-bottom': 35
        })
],
    fluid=True,
    style={'display': 'flex'},
    className='dashboard-container')


if __name__ == "__main__":
    app.run_server(debug=True, port=8050)