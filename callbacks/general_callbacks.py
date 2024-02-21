from dash.dependencies import Input, Output
from dash import dcc
import plotly.express as px
from utils.graphs import *


def register_callbacks(app, data):
    @app.callback(
        Output('graph-container', 'children'),
        [Input('data-type-dropdown', 'value')]
    )
    def update_graph(selected_value):
        # Assuming 'selected_value' is updated to include the new graph options
        if selected_value == 'MILEAGE_OVER_TIME':
            return dcc.Graph(id='line-chart-distance-overtime', figure=create_mileage_over_time_graph(data))
        elif selected_value == 'ENERGY_CONSUMPTION':
            return dcc.Graph(id='bar-chart-energy-consumption', figure=create_energy_consumption_graph(data))
        elif selected_value == 'DRIVE_EFFICIENCY':
            return dcc.Graph(id='scatter-chart-drive-efficiency', figure=create_drive_efficiency_graph(data))
        elif selected_value == 'TIME_OF_DAY':
            return dcc.Graph(id='pie-chart-time-of-day', figure=create_fig_pie(data))
        elif selected_value == 'DURATION':
            return dcc.Graph(id='line-chart-driving-duration', figure=create_fig_line(data))
