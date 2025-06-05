# 🏃‍♀️ RunSmart – Assistente de Corrida ao Ar Livre

Este é um projeto simples criado com **Python e Streamlit** para treinar os fundamentos da lógica de programação, com foco em **condicionais (`if/else`)** e **estruturas repetitivas (`for`)**. O aplicativo simula uma assistente virtual de corrida que se adapta ao clima e ajuda a registrar o desempenho da corrida por quilômetro.

> 🎯 **Objetivo do projeto:** aplicar, de forma prática e visual, os conceitos básicos de lógica em Python usando uma interface web acessível e interativa.

---

## 🚀 Funcionalidades

- O usuário informa o clima do dia (ensolarado, nublado ou chuvoso).
- Com base no clima, o app decide se o treino pode ou não ser feito ao ar livre.
- O usuário informa quantos km pretende correr e registra o tempo (em minutos) de cada trecho.
- O sistema calcula e mostra:
  - O tempo total da corrida
  - A média de minutos por km
  - Um gráfico simples com o tempo gasto em cada km
- Utiliza emojis e uma apresentação amigável para facilitar a experiência.

---

## 🧩 O que são Condicionais e Estruturas Repetitivas?

### ✅ Condicionais (`if / elif / else`)

Condicionais são blocos de código que **tomam decisões** com base em uma condição. Elas respondem perguntas como:  
> "Se o clima está bom, devo correr?"

 
### 🔁 Estruturas Repetitivas (for / loop)
Estruturas repetitivas são usadas quando precisamos repetir uma ação várias vezes. No projeto, usamos para:

Coletar os tempos de corrida a cada km informado pelo usuário.

Gerar listas de dados para análise posterior.



## 🛠️ Tecnologias

- **Python 3.8+**
- **[Streamlit](https://streamlit.io/)** – criação da interface web
- **[Matplotlib](https://matplotlib.org/)** – criação do gráfico de desempenho
- 

---

## 📁 Estrutura do projeto

📦 RunSmart
┣ 📄 app.py # Código principal do app
┣ 📄 requirements.txt # Bibliotecas necessárias para o deploy
┗ 📄 README.md # Descrição do projeto


---

## 🌐 Como fazer o deploy com o Streamlit Cloud

1. Acesse [https://streamlit.io/cloud](https://streamlit.io/cloud)
2. Faça login com sua conta GitHub.
3. Crie um novo app e selecione o repositório deste projeto.
4. Verifique se o arquivo `requirements.txt` contém:
streamlit
matplotlib


5. Clique em "Deploy". Seu app será publicado gratuitamente!

---

## 📝 Aprendizados

Este projeto foi desenvolvido com o intuito de:

- Aprender e praticar **condicionais** e **estruturas repetitivas**
- Criar interfaces com **Streamlit**
- Organizar um projeto real com Python
- Publicar um app funcional de forma simples e gratuita

---

## ✅ Status do projeto

✔️ Finalizado – em uso para aprendizado e demonstração de lógica de programação com Python.

---

> Projeto desenvolvido por Siury Lourenco, com fins educacionais.
