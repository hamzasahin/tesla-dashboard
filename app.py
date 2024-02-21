# Import necessary libraries
import dash
from dash.dependencies import Input, Output
from dash import dcc, html
import pandas as pd

from callbacks.general_callbacks import register_callbacks

from layouts.home import get_home_layout
from utils.constants import EXTERNAL_STYLESHEETS, DATA_PATH

data = pd.read_csv(DATA_PATH)

# Convert 'Started At (PST)' to datetime and create a 'Time of Day' category
data['Started At (PST)'] = pd.to_datetime(data['Started At (PST)'])
data['Time of Day'] = pd.cut(data['Started At (PST)'].dt.hour,
                             bins=[0, 6, 12, 18, 24],
                             labels=['Night', 'Morning', 'Afternoon', 'Evening'],
                             right=False)

# Initialize your Dash app
app = dash.Dash(__name__, external_stylesheets=EXTERNAL_STYLESHEETS)

# Define the layout of the dashboard
app.layout = get_home_layout()

register_callbacks(app, data)

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
