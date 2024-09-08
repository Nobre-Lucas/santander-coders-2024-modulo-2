# Pesquisa de Mobilidade Urbana no Distrito Federal (Brasil) - Documentação do Projeto

![image](https://github.com/user-attachments/assets/88b7d5bc-7805-4623-a184-9403eef8cf0f)


## Visão Geral
Este projeto tem como objetivo analisar dados de mobilidade urbana do Distrito Federal, Brasil. O conjunto de dados foi obtido por meio da API do Kaggle, transformado utilizando Python (seguindo os princípios da Programação Orientada a Objetos) e carregado no data warehouse Snowflake. Um aplicativo Streamlit foi criado para visualizar os dados diretamente do Snowflake, proporcionando uma interface amigável e facilitando a análise.

### Componentes Principais:
- **Fonte de Dados**: API Kaggle (Pesquisa de Mobilidade Urbana - Distrito Federal, Brasil).
- **Armazenamento de Dados**: Data warehouse Snowflake.
- **Ferramenta de Visualização**: Streamlit.
- **Paradigma de Programação**: Programação Orientada a Objetos (POO).

---

## Índice
1. [Visão Geral do Conjunto de Dados](#visão-geral-do-conjunto-de-dados)
2. [Arquitetura do Projeto](#arquitetura-do-projeto)
3. [Instalação e Configuração](#instalação-e-configuração)
4. [Como Usar](#como-usar)
5. [Definições Importantes](#definições-importantes)
6. [Estrutura do Código](#estrutura-do-código)
7. [Contribuindo](#contribuindo)
8. [Licença](#licença)

---

## Visão Geral do Conjunto de Dados
O conjunto de dados utilizado neste projeto faz parte da **Pesquisa de Mobilidade Urbana no Distrito Federal**, Brasil, obtido através da API do Kaggle. O dataset contém quatro tabelas:

1. **Household**: Informações relacionadas ao domicílio dos entrevistados.
2. **Person**: Informações demográficas sobre as pessoas entrevistadas.
3. **Stage**: Detalhes de cada etapa do transporte durante uma viagem.
4. **Trip**: Informações sobre as viagens realizadas pelos entrevistados.

![image](https://github.com/user-attachments/assets/9c6b80d1-113d-4c87-a0cd-11d09690137c)


Os dados brutos foram baixados e processados em notebooks Python, e posteriormente transformados e carregados no Snowflake.

Link da API Kaggle:
[Pesquisa de Mobilidade Urbana - Distrito Federal](https://www.kaggle.com/api/v1/datasets/download/danielefm/urban-mobility-survey-federal-district-brazil?datasetVersionNumber=1)

---

## Arquitetura do Projeto

1. **API Kaggle**: 
   - Os dados foram baixados usando a API do Kaggle, no formato CSV, que foi extraído e processado com Python.

2. **Transformação dos Dados**:
   - Os dados foram transformados e processados utilizando práticas de Programação Orientada a Objetos (POO).

3. **Carregamento dos Dados**:
   - Os datasets brutos e transformados foram carregados no Snowflake, um data warehouse na nuvem.

4. **Visualização com Streamlit**:
   - O Streamlit foi integrado para construir um dashboard para visualizar os dados diretamente do Snowflake. Este app permite aos usuários interagir com os dados e obter insights de maneira prática.

---

## Instalação e Configuração

### Pré-requisitos:
- **Python 3.8+**
- **Conta no Snowflake Trial**
- **Streamlit**

### Passos:

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/Nobre-Lucas/santander-coders-2024-modulo-2.git
   cd santander-coders-2024-modulo-2
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configuração do Snowflake**:
   - Configure uma conta e banco de dados no Snowflake. As credenciais serão necessárias em um arquivo de variáveis de ambiente (`.env`).

4. **Execute o projeto**:
   ```bash
   streamlit run app.py
   ```

---

## Definições Importantes

### Programação Orientada a Objetos (POO)
A POO é um paradigma de programação centrado em objetos, que podem conter dados (atributos) e métodos (funções). Os principais conceitos incluem:
- **Classe**: Um modelo ou "plano" para criar objetos.
- **Objeto**: Uma instância de uma classe.
- **Encapsulamento**: Mecanismo de agrupar dados e métodos que operam sobre eles em uma única unidade (classe).
- **Herança**: Capacidade de uma classe herdar atributos e métodos de outra classe.
- **Polimorfismo**: A capacidade de usar uma interface comum para diferentes tipos de dados.

Neste projeto, a POO foi utilizada para criar classes que gerenciam o processo de ETL, tornando o código modular, reutilizável e fácil de manter.

### Snowflake (Data Warehouse)
Snowflake é um data warehouse baseado na nuvem que permite o armazenamento e a consulta de dados de maneira escalável. Ele é otimizado para armazenamento de dados, *data lakes* e análises.
- **Vantagens**: Escalabilidade, concorrência, custo-benefício e integração com diversos serviços de dados.
- **Uso no Projeto**: O Snowflake foi utilizado para armazenar tanto os dados brutos quanto os processados, que são acessados pelo aplicativo Streamlit para visualização.

### Streamlit
Streamlit é um framework de código aberto para construção de aplicações web em Python, focado em projetos de ciência de dados e machine learning.
- **Vantagens**: Fácil de usar, integra-se perfeitamente ao Python e cria dashboards interativos e atraentes.
- **Uso no Projeto**: O app Streamlit foi utilizado para visualizar os dados de mobilidade armazenados no Snowflake, permitindo que os usuários obtenham insights por meio de gráficos interativos.

### APIs
Uma API (Interface de Programação de Aplicações) permite que dois sistemas se comuniquem. Neste projeto, a API do Kaggle foi utilizada para baixar o conjunto de dados programaticamente.
- **API do Kaggle**: Permite que os usuários interajam com os serviços do Kaggle (datasets, competições, etc.) via código, sem necessidade de download manual.

---

## Estrutura do Código

```
/urban-mobility-survey
│
├── notebooks/
│   └── main.ipynb                       # Notebook Jupyter para extração e chamada das outras classes
│   └── logging.ipynb                    # Notebook Jupyter para printar as mensagens de logs
│   └── snowflake_connection.ipynb       # Notebook Jupyter para estabelecer a conexão com o Snowflake
│   └── create_table.ipynb               # Notebook Jupyter para criar as tabelas, caso não existam, no snowflake
│   └── load_raw_table.ipynb             # Notebook Jupyter para carregamento dos dados brutos no Snowflake
|
├── .env_example                         # Exemplo das variáveis de ambiente a serem salvas no arquivo .env
|
├── .gitignore                           # Arquivos e pastas não salvas no GitHub
|
├── schema.py                            # Schema das tableas a serem criadas no Snowflake
│
├── app.py                               # Aplicativo Streamlit para visualização
│
├── requirements.txt                     # Dependências Python
│
└── README.md                            # Documentação do projeto
```

---

## Contribuindo
Contribuições são bem-vindas! Se você tem sugestões para melhorias ou novas funcionalidades, sinta-se à vontade para enviar um pull request ou abrir uma issue.

---

## Licença
Este projeto é licenciado sob a Licença MIT.
