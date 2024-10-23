# Painel de Análise de Ataques com Mísseis

Este projeto apresenta um painel interativo, criado utilizando Streamlit e Plotly, para analisar dados sobre ataques com mísseis na Ucrânia. O painel exibe visualizações detalhadas sobre o número de mísseis lançados e destruídos, bem como a taxa de interceptação mensal ao longo do tempo. Um dos principais destaques deste projeto é sua **integração direta com a API do Kaggle**, permitindo o download automático dos dados necessários para a análise.

## Funcionalidades

- **Download de Dados**: O painel permite o download automático dos dados diretamente do Kaggle utilizando a API do Kaggle. Isso facilita o acesso a dados atualizados e relevantes.
- **Visualização Interativa**: Três tipos de gráficos são gerados:
  - **Gráfico de Barras**: Mostra a comparação entre mísseis lançados e destruídos ao longo do tempo.
  - **Gráfico de Pizza**: Exibe a proporção total de mísseis lançados versus destruídos.
  - **Gráfico de Linha**: Apresenta a taxa de interceptação mensal de mísseis ao longo do tempo.

## Estrutura do Projeto

- `usa_token.py`: Arquivo de configuração para autenticação com a API do Kaggle, que possibilita a conexão segura e a realização de downloads.
- `app.py`: Arquivo principal contendo o código para baixar, processar e visualizar os dados.
- `dados/`: Diretório onde os dados baixados são armazenados.

## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. **Configuração da API do Kaggle**: Adicione suas credenciais do Kaggle no arquivo `usa_token.py`:
    ```python
    configuracoes = {
        'kaggle_username': 'seu_usuario',
        'kaggle_key': 'sua_chave_api'
    }
    ```
   Essa configuração é essencial para autenticar e acessar os dados diretamente do Kaggle.

## Como Executar

1. Execute o aplicativo Streamlit:
    ```bash
    streamlit run app.py
    ```

2. Na barra lateral, clique no botão "Download dos dados" para baixar os dados diretamente do Kaggle e processá-los.

3. Explore as visualizações interativas no painel.

## Dataset

O dataset utilizado no projeto pode ser encontrado no Kaggle:  
[Massive Missile Attacks on Ukraine](https://www.kaggle.com/datasets/piterfm/massive-missile-attacks-on-ukraine)

A conexão com o Kaggle é fundamental para garantir que estamos utilizando dados atualizados e relevantes para nossas análises.

## Resultado final

![Ukraine - Missile Interception - Dashboard](https://github.com/user-attachments/assets/75a129a4-fa23-416a-8445-d5bb57087cca)
