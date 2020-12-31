from flask import (
    current_app as app,
    url_for,
    render_template,
    redirect,
    request
)
from .forms import CalcularForm
from .calculos import calculo_juros_compostos
from .plotly_wrapper import create_plot_calculos
import pandas as pd

@app.route("/", methods=['GET', 'POST'])
def calcular():
    calcularForm = CalcularForm()
        
    if calcularForm.validate_on_submit():
        montante_inicial = calcularForm.montante_inicial.data
        aportes_mensais = calcularForm.aportes_mensais.data
        taxa_mensal = calcularForm.taxa_mensal.data
        tempo_meses = calcularForm.tempo_meses.data

        return redirect(url_for('resultado', montante=montante_inicial,aportes=aportes_mensais, taxa=taxa_mensal, tempo=tempo_meses))
    return render_template(
        'index.html',
        form=calcularForm
    )

@app.route("/resultado")

def resultado():
    capital_mensal = calculo_juros_compostos(
        montante_inicial=float(request.args['montante']), 
        aportes_mensais=float(request.args['aportes']),
        taxa_mensal=float(request.args['taxa']),
        tempo_meses=int(request.args['tempo'])
    )
    plot = create_plot_calculos(round(capital_mensal, 2))
    return render_template(
        "resultado.html",
        montante_inicial=round(float(request.args['montante']), 2),
        capital_final=round(capital_mensal['Capital'].iloc[-1], 2), 
        juros_acumulados=round(capital_mensal['Juros Acumulados'].iloc[-1], 2), 
        total_aportado=round(capital_mensal['Valor Aportado'].iloc[-1], 2),
        plot=plot
    )

@app.route("/favicon.ico")
def favicon():
    return app.send_static_file('favicon.ico')