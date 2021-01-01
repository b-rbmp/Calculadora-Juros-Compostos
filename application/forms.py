from flask_wtf import FlaskForm
from wtforms import DecimalField, IntegerField, SubmitField
from wtforms.validators import DataRequired

class CalcularForm(FlaskForm):
    montante_inicial = IntegerField(
                        'Montante Inicial', 
                        validators= [
                                        DataRequired(message="Preencha este campo")
                                    ],               
    )
    aportes_mensais = IntegerField(
                        'Aportes Mensais', 
                        validators= [
                                        DataRequired(message="Preencha este campo")
                                    ],                 
    )
    taxa_mensal = DecimalField(
                        'Taxa de Juros Mensal', 
                        validators= [
                                        DataRequired(message="Preencha este campo")
                                    ],
                        places=2, 
                        rounding=None                
    )
    tempo_meses = IntegerField(
                        'Meses do Investimento', 
                        validators= [
                                        DataRequired(message="Preencha este campo")
                                    ]                 
    )
    submit = SubmitField('Calcular')