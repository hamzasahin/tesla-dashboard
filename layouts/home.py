from dash import dcc, html

def get_home_layout():
    layout = html.Div(children=[
        html.H1(children='Tesla Driving Dashboard', style={'textAlign': 'center', 'marginTop': '20px', 'marginBottom': '20px'}),

        html.Div([
            dcc.Dropdown(
                id='data-type-dropdown',
                options=[
                         {'label': 'Driving Duration Over Time', 'value': 'DURATION'},
                            {'label': 'Distribution of Driving Times of Day', 'value': 'TIME_OF_DAY'},
                            {'label': 'Mileage Over Time', 'value': 'MILEAGE_OVER_TIME'},
                            {'label': 'Energy Consumption Over Trips', 'value': 'ENERGY_CONSUMPTION'},
                            {'label': 'Drive Efficiency', 'value': 'DRIVE_EFFICIENCY'}
                ],
                value='DURATION',
                style={'width': '48%', 'margin': '0 auto'}
            )
        ], style={'marginBottom': '20px'}),

        html.Div(id='graph-container', style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'})
    ])
    return layout