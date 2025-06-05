import streamlit as st  # type: ignore
import time
import matplotlib.pyplot as plt
 
st.set_page_config(page_title="RunSmart", page_icon="🏃🏻‍♀️‍➡️", layout="centered")

st.title("🏃🏻‍♀️‍➡️RunSmart  - Seu Assistente de corrida ao Ar livre")
st.markdown("Organize seu treini baseado no clima do dia e registro o tempo por km!")

clima = st.selectbox("Como está o clima agora?", ["Selecione", "Ensolarado", "Nublado", "Chuvoso"])

if clima == "Ensolarado":
    st.sucess("ótimo! Dia perfeito para correr ao ar livre!")
    
    km_total = st.slider("Quantos km você quer correr hoje?", 1, 10, 3)
    
    if st.buttun("Iniciar Treino"):
        tempos_km = []
        st.write("Preparando corrida...")
        
        for km in range(1, km_total + 1):
            st.write(f" Corra o km {km}!")
            tempo = st.number_input(f"Digite o tempo (minutos) para o km {km}:", min_value=1.0, max_value=60.0, value=5.0, step=0.1, key=f"tempo_{km}")
            
            progress_bar = st.progress(0)
            for pct in range(101):
                time.sleep(0.05)
                progress_bar.progress(pct)
            st.sucess(f" km {km} Completo em {tempo} minutos!")
            tempos_km.append(tempo)
            st.write("--")
            
    total_tempo = sum(tempo_km)
    media_tempo = total_tempo / km_total
    
    st.balloons()
    st.markdowm(f" **Parabéns! Você completou {km_total} km em {total_tempo: 2f} minutos!**")
    st.markdown(f"Média por km: {media_tempo: 2f} minutos!")        
            
    # Gráfico de barras do desempenho
    fig. ax = plt.subplots()
    ax.bar(range(1, km_total + 1), tempos_km, color='skyblue')
    ax.set_xlabel("KM")
    ax.set_ylabel("Tempo (minutos)")
    ax.set_title("Tempo por km")
    ax.set_xticks(range(1, km_total + 1))
    st.pyplot(fig) 
    
elif clima in ["Nublado", "Chuvoso"]:
    st.warning("Hoje não é ideal para correr ao ar livre. Que tal um treino em casa ou descanso ativo?")
    
elif clima == "Selecione":
    st.info("Por favor, selecione o clima para começar")  
 
    