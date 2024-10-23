from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
import plotly.express as px
from usa_token import configuracoes
import os
import streamlit as st


def download_dataset():
    # Kaggle API client
    api = KaggleApi()
    
    # Autenticar utilizando token
    api.set_config_value(name='username', value=configuracoes.kaggle_username)
    api.set_config_value(name='key', value=configuracoes.kaggle_key)

    api.authenticate()
    
    # Definir um dataset e um caminho de onde baixar os dados
    # dataset = 'piterfm/massive-missile-attacks-on-ukraine'
    dataset = 'piterfm/massive-missile-attacks-on-ukraine'
    path = './dados'

    # Download the dataset
    api.dataset_download_files(dataset, path=path, unzip=True)
    print(f"Dataset {dataset} baixado com sucesso!")


def process_dataset(data):
    # Drop unnecessary columns including the original 'time_end'
    data.drop(columns=['time_end', 'model', 'launch_place', 'target', 'destroyed_details', 'carrier', 'source'], inplace=True)
    # Ensure that time is removed and only the date is kept
    data['time_start'] = data['time_start'].astype(str).apply(lambda x: x.split(' ')[0])
    
    # Rename 'time_start' to 'date'
    data.rename(columns={'time_start': 'date'}, inplace=True)

    # Convert 'date' to datetime object and extract the date part
    data['date'] = pd.to_datetime(data['date']).dt.date

    return data
 

def remove_time(data):
    # Ensure that time is removed and only the date is kept
    data['time_start'] = data['time_start'].astype(str).apply(lambda x: x.split(' ')[0])
    return data


def monthly_interception_rate(data):
    # Convert 'date' to datetime object for proper resampling
    data['date'] = pd.to_datetime(data['date'])
    # Group by month and sum the values of 'launched' and 'destroyed'
    monthly_data = data.resample('M', on='date').sum().reset_index()
    # Calculate the interception rate based on monthly sums, round, and convert to string with '%'
    monthly_data['interception_rate'] = (monthly_data['destroyed'] / monthly_data['launched'] * 100).fillna(0).round(0).astype(int)
    monthly_data['interception_rate'] = monthly_data['interception_rate'].astype(str) + '%'
    # Format date to show only year and month for readability in the chart
    monthly_data['date'] = monthly_data['date'].dt.strftime('%Y-%m')
    return monthly_data

def plot_data_bar(data):
    fig = px.bar(data, x='date', y=['launched', 'destroyed'],
                 labels={'value': 'Count', 'variable': 'Category'},
                 color_discrete_map={'launched': 'darkblue', 'destroyed': 'darkgray'},
                 barmode='group')
    fig.update_traces(marker_line_width=0)
    fig.update_layout(
        title='Mísseis Lançados vs Destruídos ao Longo do Tempo',
        xaxis_title='Data',
        yaxis_title='Número de Mísseis',
        xaxis=dict(
            title_font=dict(size=18, color='black'),
            tickfont=dict(size=16, color='black'),
            rangeslider=dict(visible=True),  # Enable the range slider
            type='date'  # Ensure the x-axis is treated as date
        ),
        yaxis=dict(
            title_font=dict(size=20, color='black'),
            tickfont=dict(size=18, color='black'),
            range=[0, 110]
        )
    )
    return fig

def plot_data_pizza(data):
    # Summing the total values of launched and destroyed missiles
    total_data = data[['launched', 'destroyed']].sum().reset_index()
    total_data.columns = ['Categoria', 'Contagem']

    # Changing to pie chart
    fig = px.pie(total_data, names='Categoria', values='Contagem',
                 title='Proporção Total de Mísseis Lançados vs Destruídos',
                 color_discrete_map={'launched': 'darkblue', 'destroyed': 'darkgray'})
    
    fig.update_traces(textinfo='percent+label')
    fig.update_layout(
        title_font=dict(size=20),
        legend=dict(
            title="Categoria",
            font=dict(size=14)
        )
    )
    return fig

def plot_interception_rate(data):
    fig = px.line(data, x='date', y='interception_rate', color_discrete_sequence=['darkblue'])
    fig.update_traces(line=dict(width=4))
    fig.update_layout(
        title='Taxa de Interceptação Média Mensal ao Longo do Tempo',
        xaxis_title='Mês',
        yaxis_title='Taxa de Interceptação (%)',
        xaxis=dict(
            title_font=dict(size=18, color='black'),
            tickfont=dict(size=16, color='black'),
            tickangle=-90,
            tickmode='linear',
            dtick='M1',
            rangeslider=dict(visible=True),  # Enable the range slider
            type='date'  # Ensure the x-axis is treated as date
        ),
        yaxis=dict(
            title_font=dict(size=20, color='black'),
            tickfont=dict(size=18, color='black'),
            range=[50, 100]
        )
    )
    return fig


root = os.getcwd()
dados_dir = f'{root}/dados'

st.set_page_config(
    page_title="Ukraine - Missile Interception",
    layout="wide"
)

if st.sidebar.button('Download dos dados', type="primary"):
    download_dataset()

    data = pd.read_csv(f"{root}/dados/missile_attacks_daily.csv")
    data_processed = process_dataset(data.copy())
    
    st.header("Painel de Análise de Ataques com Mísseis")

    st.subheader("Dados processados")
    st.write(data_processed)

    col1, col2 = st.columns(2)
    
    with col1:
        subcol1, subcol2 = st.columns([3, 1])
        with subcol1:
            st.plotly_chart(plot_data_bar(data_processed))
        with subcol2:
            st.write("Este gráfico de barras mostra a quantidade de mísseis lançados em comparação aos destruídos ao longo do tempo. Os dados são agrupados por data, permitindo uma visualização clara das diferenças entre os dois grupos em cada período. O formato agrupado exibe os mísseis lançados e destruídos lado a lado para facilitar a comparação ao longo do tempo.")
    
    with col2:
        subcol1, subcol2 = st.columns([3, 1])
        with subcol1:
            st.plotly_chart(plot_data_pizza(data_processed))
        with subcol2:
            st.write("Este gráfico de pizza representa a proporção geral de mísseis lançados em relação aos destruídos. Ele oferece uma visão rápida da distribuição total, mostrando o percentual de mísseis lançados que foram destruídos. Isso é útil para entender a tendência mais ampla de interceptação de mísseis, sem focar em datas específicas.")
    
    subcol1, subcol2 = st.columns([3, 1])
    
    with subcol1:
        st.plotly_chart(plot_interception_rate(monthly_interception_rate(data_processed)))
    with subcol2:
        st.write("Este gráfico de linha exibe a taxa média mensal de interceptação de mísseis ao longo do tempo. Ele acompanha a evolução da taxa de interceptação, que é a proporção de mísseis destruídos em relação aos lançados, mês a mês. O gráfico fornece insights sobre a eficácia dos esforços de interceptação de mísseis em diferentes períodos, com um controle deslizante para explorar os detalhes.")
