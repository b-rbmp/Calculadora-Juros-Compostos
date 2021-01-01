import plotly
import plotly.graph_objs as go

import pandas as pd
import json

def create_plot_calculos(capital_vector):

    x_axis = capital_vector.index.values
    fig = go.Figure(data=[
        go.Scatter(
            name='Juros',
            x=x_axis,
            y=capital_vector['Juros Acumulados'].values
        ),
        go.Scatter(
            name='Aportes',
            x=x_axis,
            y=capital_vector['Valor Aportado'].values
        ),
        go.Scatter(
            name='Capital',
            x=x_axis,
            y=capital_vector['Capital'].values
        )
    ])
    # Change the bar mode
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            zeroline=True,
            zerolinecolor='rgb(204, 204, 204)',
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            ticks='outside',
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
            gridwidth=1, 
            gridcolor='rgb(204, 204, 204)',
            tickmode = 'linear',
            tick0 = 0,
            dtick = 1,
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=True,
            zerolinecolor='rgb(204, 204, 204)',
            showline=True,
            showticklabels=True,
            ticks='outside',
            linecolor='rgb(204, 204, 204)',
            linewidth=2,
            tickfont=dict(
                family='Arial',
                size=12,
                color='rgb(82, 82, 82)',
            ),
            gridwidth=1, 
            gridcolor='rgb(204, 204, 204)',
            tickprefix = 'R$ ',
            tickformat = '.2f',
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.05,
            xanchor="right",
            x=1
        ),
        autosize=True,
        showlegend=True,
        plot_bgcolor='white',
        hovermode="x unified",
    )


    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON