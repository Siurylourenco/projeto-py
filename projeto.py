import streamlit as st  # type: ignore
import time
import matplotlib.pyplot as plt

st.set_page_config(page_title="RunSmart", page_icon="🏃🏻‍♀️‍➡️", layout="centered")

st.title("🏃🏻‍♀️‍➡️RunSmart - Seu Assistente de Corrida ao Ar Livre")
st.markdown("Organize seu treino baseado no clima do dia e registre o tempo por km!")

clima = st.selectbox("Como está o clima agora?", ["Selecione", "Ensolarado", "Nublado", "Chuvoso"])

if clima == "Ensolarado":
    st.success("Ótimo! Dia perfeito para correr ao ar livre!")

    km_total = st.slider("Quantos km você quer correr hoje?", 1, 10, 3)

    # Inicializa os tempos se ainda não estiverem definidos
    if "tempos_km" not in st.session_state or len(st.session_state.tempos_km) != km_total:
        st.session_state.tempos_km = [5.0] * km_total

    st.markdown("### ⏱️ Registre o tempo de cada quilômetro:")
    for km in range(km_total):
        st.session_state.tempos_km[km] = st.number_input(
            f"Tempo do KM {km + 1} (minutos):",
            min_value=1.0,
            max_value=60.0,
            value=st.session_state.tempos_km[km],
            step=0.1,
            key=f"tempo_{km}"
        )

    if st.button("🏁 Finalizar Corrida"):
        total_tempo = sum(st.session_state.tempos_km)
        media_tempo = total_tempo / km_total

        st.balloons()
        st.markdown(f"**Parabéns! Você completou {km_total} km em {total_tempo:.2f} minutos!**")
        st.markdown(f"Média por km: **{media_tempo:.2f} minutos**")

        # Gráfico
        fig, ax = plt.subplots()
        ax.bar(range(1, km_total + 1), st.session_state.tempos_km, color='skyblue')
        ax.set_xlabel("KM")
        ax.set_ylabel("Tempo (minutos)")
        ax.set_title("Tempo por KM")
        ax.set_xticks(range(1, km_total + 1))
        st.pyplot(fig)

elif clima in ["Nublado", "Chuvoso"]:
    st.warning("Hoje não é ideal para correr ao ar livre. Que tal um treino em casa ou descanso ativo?")

elif clima == "Selecione":
    st.info("Por favor, selecione o clima para começar.")
