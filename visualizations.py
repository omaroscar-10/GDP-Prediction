import dash
from dash import dcc, html,  Input, Output
from dash.dependencies import Input, Output, State
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler

# Sample data 
raw_data = pd.read_csv(r'data\final_data_subset.csv')
#Subsaharan_GDP_LE
#final_data_subset
data = raw_data[raw_data['Years'] == max(raw_data['Years'])]

app = dash.Dash(__name__)

# Red to Green color scale
color_scale = px.colors.diverging.RdYlGn

# Define layout
app.layout = html.Div([
     dcc.Slider(
        id='year-slider',
        min=int(raw_data['Years'].min()),
        max=int(raw_data['Years'].max()),
        marks={year: str(year) for year in range(int(raw_data['Years'].min()), int(raw_data['Years'].max()) + 1)},
        step=1,
        value=int(raw_data['Years'].max())
    ),
    dcc.Graph(
        id='choropleth-map'
    ),
    html.Div(
        id='chart-container',
        children=[
            dcc.Graph(id='box-plot', style={'display': 'none'}),
        ]
    )
])
@app.callback(
    
     Output('choropleth-map', 'figure'),
    [Input('year-slider', 'value')]
)

def update_choropleth_map(selected_year):
    filtered_df = raw_data[raw_data['Years'] == selected_year]

    fig = px.choropleth(filtered_df, 
                        locations='Country', 
                        locationmode='country names',
                        color='Life expectancy at birth, total (years)',
                        color_continuous_scale=color_scale,
            range_color=[min(filtered_df['Life expectancy at birth, total (years)']), 70, max(filtered_df['Life expectancy at birth, total (years)'])],
            custom_data=['Country', 'Life expectancy at birth, total (years)', 'GDP per capita (current US$)']
        ).update_geos(
            center=dict(lon=20, lat=0),
            visible=True
        ).update_layout(
            geo=dict(
                showframe=False,
                showcoastlines=False,
                projection_scale=2.5
            ),
            margin=dict(l=0, r=0, t=50, b=0),
            height=600,
            title={
                'text': f'<b>Life Expectancy in Sub-Saharan Africa for Year {selected_year}</b>',
                'x': 0.5,
                'font': {'size': 18, 'color': 'black', 'family': 'Arial'}
            }
        )

    fig.update_traces(
        hovertemplate='<b>%{customdata[0]}</b><br>' +
                      'Life Expectancy (years): %{customdata[1]:.2f}<br>' +
                      'GDP per capita ($USD): %{customdata[2]:,.2f}<br>'
    )

    return fig

@app.callback(
    [
     Output('box-plot', 'figure'),
     Output('box-plot', 'style')
    #,Output('year-slider', 'value')
    ],
    [Input('choropleth-map', 'clickData')],
    [State('year-slider', 'value')] 
)
def update_charts(click_data,selected_year):
    
    #If click data is None, or clicks on an invalid country
    if click_data is None:
        return  px.scatter(), {'display': 'none'}

    selected_country = click_data['points'][0]['location']
    #print(selected_year) 
    filtered_df = raw_data[raw_data['Years'] == selected_year]    
    country_data = pd.DataFrame(filtered_df).iloc[:,2:]

    scaler = MinMaxScaler()

    pre_scaler = scaler.fit_transform(filtered_df.iloc[:,2:])
    normal_data = pd.DataFrame(pre_scaler, columns = list(country_data.columns))

    # Create a box plot for each variable
    box_plot = px.box(
        normal_data.iloc[:,2:],
        y=list(normal_data.columns)[2:],
        title=f'{selected_country} compared to all of Sub-Saharan Africa for year {selected_year} - Normalized',
        labels={'Value': 'Box Plot'}
    )

    for trace in box_plot['data']:
        trace.update(opacity=0.5)

        
        
    normal_with_country = normal_data.copy()
    normal_with_country['Country'] = filtered_df['Country'].reset_index(drop=True)

    # Overlay a red dot for the selected country's data on the box plot
    for variable in list(country_data.keys())[2:]:
        color_index = int(round(len(color_scale)*float(normal_with_country[variable][normal_with_country['Country'] == selected_country])))-1
        #print(color_index)
        scatter_color = color_scale[color_index]
        box_plot.add_trace(go.Scatter(
            x=[variable],
            y=normal_with_country[variable][normal_with_country['Country'] == selected_country],
            mode='markers',
            marker=dict(color=scatter_color, size=10),
            name=variable
        ))


    # Change visibility of the boxplot
    style = {'display': 'block'}

    return   box_plot, style

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)