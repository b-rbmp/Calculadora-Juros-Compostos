from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length

class CalcularForm(FlaskForm):
    montante_inicial = IntegerField(
                        'Montante Inicial', 
                        validators= [
                                        DataRequired()
                                    ],               
    )
    aportes_mensais = IntegerField(
                        'Aportes Mensais', 
                        validators= [
                                        DataRequired()
                                    ],                 
    )
    taxa_mensal = IntegerField(
                        'Taxa de Juros Mensal', 
                        validators= [
                                        DataRequired()
                                    ],                
    )
    tempo_meses = IntegerField(
                        'Meses do Investimento', 
                        validators= [
                                        DataRequired()
                                    ]                 
    )
    submit = SubmitField('Calcular')