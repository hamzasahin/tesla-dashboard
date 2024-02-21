import plotly.express as px


def create_fig_line(data):
    fig_line = px.line(data, x='Started At (PST)', y='Duration (Minutes)', title='Driving Duration Over Time')
    fig_line.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    fig_line.update_xaxes(title_text='Date')
    fig_line.update_yaxes(title_text='Duration (Minutes)')
    return fig_line


def create_fig_pie(data):
    fig_pie = px.pie(data, names='Time of Day', title='Distribution of Driving Times of Day')
    fig_pie.update_traces(textinfo='percent+label')
    fig_pie.update_layout(showlegend=True)
    return fig_pie


def create_mileage_over_time_graph(data):
    # Correct column names are used here
    fig_distance_over_time = px.line(data, x='Started At (PST)', y='Ending Odometer (mi)', title='Mileage Over Time')
    fig_distance_over_time.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig_distance_over_time


def create_energy_consumption_graph(data):
    # Correct column names are used here
    fig_energy_consumption = px.bar(data, x='Started At (PST)', y='Total Energy Used (kWh)',
                                    title='Energy Consumption Over Trips')
    fig_energy_consumption.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig_energy_consumption


def create_drive_efficiency_graph(data):
    # Correct column names are used here
    fig_drive_efficiency = px.scatter(data, x='Distance (mi)', y='Total Energy Used (kWh)',
                                      title='Drive Efficiency',
                                      trendline='ols')  # Ordinary Least Squares regression line
    fig_drive_efficiency.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
    return fig_drive_efficiency


# def create_drive_efficiency_graph(data):
#     # First, filter out trips with distances less than 0.3 miles
#     filtered_data = data[data['Distance (mi)'] > 0.2]
#
#     # Then, calculate 'Actual Miles per kWh' for each remaining trip
#     filtered_data['Actual Miles per kWh'] = filtered_data['Distance (mi)'] / filtered_data['Total Energy Used (kWh)']
#
#     # Calculate 'Efficiency (%)' as a function of Tesla's miles_per_kWh
#     filtered_data['Efficiency (%)'] = (filtered_data['Actual Miles per kWh'] / 3.57)
#
#     # Generate the scatter plot
#     fig_drive_efficiency = px.scatter(filtered_data, x='Distance (mi)', y='Efficiency (%)',
#                                       title='Drive Efficiency as Percentage of Official Mileage',
#                                       trendline='ols',  # Ordinary Least Squares regression line
#                                       labels={'Distance (mi)': 'Distance (Miles)',
#                                               'Efficiency (%)': 'Efficiency (%)'})
#
#     # Update layout for better readability and format y-axis as percentage
#     fig_drive_efficiency.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
#     fig_drive_efficiency.update_yaxes(tickformat=".0%")
#
#     return fig_drive_efficiency