from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from FetchGGSheet import getGsheetPData
import plotly.graph_objects as go
import numpy as np
import random
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
LBResumodata=getGsheetPData('LBResumo')
LBResumodata=getGsheetPData('LBResumo')

LBResumodata=LBResumodata[LBResumodata.Exercise=='ISOBulgSquat']
LBResumodatISOBulgSq=LBResumodata.loc[:,['Unnamed: 2','Unnamed: 8']]
xdata=LBResumodatISOBulgSq.loc[:,'Unnamed: 2']
ydata=LBResumodatISOBulgSq.loc[:,'Unnamed: 8']
## https://github.com/andrevsl/SoCieForParaOPlayAndroidApp AppWeb para Android usando Webview to facilitate at first
## my workout management/organization/control/analysis as test
## Dash Firebase Deploy study https://github.com/andrevsl/DashDeployFirebase
## Science VbT app using AI for Strength/Power Measurements, Bar Velocity, New Sensors


fig = px.line(LBResumodatISOBulgSq, x="Unnamed: 2", y="Unnamed: 8")
fig.update_layout(plot_bgcolor='#010103',paper_bgcolor='#010103',width=790, height=400,
                  xaxis_visible=True, yaxis_visible=True, showlegend=True, margin=dict(l=0,r=0,t=4,b=0),title=dict(
        text="Plot Title"
    ))

app.layout = dbc.Container([
    html.Div([
        html.Div([
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
        html.Div([
            html.Div(
                dbc.RadioItems(
                    className='btn-group',
                    inputClassName='btn-check',
                    labelClassName="btn btn-outline-light",
                    labelCheckedClassName="btn btn-light",
                    options=[
                        {"label": "Graph", "value": 1},
                        {"label": "Table", "value": 2}
                    ],
                    value=1,
                    style={'width': '100%'}
                ), style={'width': 206}
            ),
            html.Div(
                dbc.Button(
                    "About",
                    className="btn btn-info",
                    n_clicks=0
                ), style={'width': 104})
        ], style={'margin-left': 15, 'margin-right': 15, 'display': 'flex'}),
        html.Div([
            html.Div([
                html.H2('Unclearable Dropdown:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Option A', 'value': 1},
                        {'label': 'Option B', 'value': 2},
                        {'label': 'Option C', 'value': 3}
                    ],
                    value=1,
                    clearable=False,
                    optionHeight=40,
                    className='customDropdown'
                )
            ]),
            html.Div([
                html.H2('Unclearable Dropdown:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Option A', 'value': 1},
                        {'label': 'Option B', 'value': 2},
                        {'label': 'Option C', 'value': 3}
                    ],
                    value=2,
                    clearable=False,
                    optionHeight=40,
                    className='customDropdown'
                )
            ]),
            html.Div([
                html.H2('Clearable Dropdown:'),
                dcc.Dropdown(
                    options=[
                        {'label': 'Option A', 'value': 1},
                        {'label': 'Option B', 'value': 2},
                        {'label': 'Option C', 'value': 3}
                    ],
                    clearable=True,
                    optionHeight=40,
                    className='customDropdown'
                )
            ])
        ], style={'margin-left': 15, 'margin-right': 15, 'margin-top': 30}),
        html.Div(
            html.Img(src='assets/image.svg',
                     style={'margin-left': 15, 'margin-right': 15, 'margin-top': 30, 'width': 310})
        )
    ], style={
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
            'margin-bottom': 35,
            'display': 'flex'
        })
],
                           fluid=True,
                           style={'display': 'flex'},
                           className='dashboard-container')
if __name__ == "__main__":
    app.run_server(debug=True)