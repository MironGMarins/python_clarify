from flask import Flask, render_template_string
import plotly.express as px
import pandas as pd

# inicia o flask
app = Flask(__name__)

# criar nosso dataframe
df_consolidado = pd.DataFrame({
    'Status': ['Ativo','Inativo','Ativo','Inativo','Cancelado','Cancelado','Ativo']
})

#rota do grafico de pizza usando o plotly
@app.route('/')
def grafico_pizza():
    # primero vamos contar os valores?
    status_dist = df_consolidado['Status'].value_counts().reset_index()
    status_dist.columns=['Status', 'Quantidade']

    #criar o grafico do ploty!!!
    fig = px.pie(
        status_dist,
        values ='Quantidade',
        names = 'Status',
        title = 'Distribuição do Status'    
    )
    # converter para html
    grafico_html = fig.to_html(full_html=False)

    #html simple com o grafico embutido
    html=f'''
    <html>
        
            <head>
            <meta charset="UTF-8">
                <title>
                Feito por Miron
                </title>
            </head>
         <body>
            <h2>Grafico com plotly</h2>
            {grafico_html}
         </body>

    </html>

    '''
    #renderiza a string de html usando o render_template
    #sem isso o html não é manipulado corretamente
    return render_template_string(html)
    

if __name__ == "__main__":
    app.run(debug=True)