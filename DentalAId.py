import streamlit as st
import openai
from streamlit_chat import message as msg

import os

SENHA_OPEN_AI = os.getenv("SENHA_OPEN_AI")
openai.api_key = SENHA_OPEN_AI

# URL da imagem do logo no repositório do GitHub
logo_url = "https://github.com/cristianomaraujo/dental-AIdTCC/blob/main/Capa.jpg?raw=true"
logo_url3 = "https://github.com/cristianomaraujo/dental-AIdTCC/blob/main/Capa 2.jpg?raw=true"

# Exibindo a imagem de logo
st.sidebar.image(logo_url3, use_column_width=True)

st.image(logo_url, use_column_width=True)
abertura = st.write("Hello! I am DentalAId, an AI-powered chatbot designed to assist you with the initial guidance and management of dental trauma. To begin, simply type 'hello' in your preferred language (e.g., Hi, Oi, Hola, Salut, Hallo, 你好, привет) or share any details about the dental trauma you'd like help with in the field below.")
st.sidebar.title("References")
text_input_center = st.chat_input("Chat with me by typing in the field below")
condicoes = ('You are a virtual assistant named DentalAId, and your goal is to assist patients in managing dental trauma.'
'Act as a healthcare professional, conducting an assessment of the patient.'
'Initially, try to identify the type of trauma the patient has experienced. Ask what happened and the condition of the tooth to provide appropriate guidance.'
'Respond only to questions related to dental trauma. For any other subject, inform the user that you are not qualified to answer.'
'Begin the conversation by introducing yourself and explaining your objective.'
'In cases of dental fractures or avulsions involving permanent teeth, it is essential to act quickly, as the chances of saving the tooth are highest within the first 20 minutes after the accident.'
'In cases of dentoalveolar trauma, it can be classified into three main types of injuries: Avulsion, which occurs when the tooth is completely displaced from the oral cavity; Crown fracture, characterized by the breaking of part of the crown while the rest of the tooth remains intact; and Luxation, which occurs when the tooth is displaced from its normal position without being completely expelled from the mouth.'
'Initially, it is recommended to locate the tooth as quickly as possible, holding it by the crown and avoiding any contact with the root. Then, rinse it briefly with clean water and attempt to reinsert it immediately into the socket, even if there is bleeding. To help stabilize the tooth, keep the mouth closed using a piece of gauze, a clean cloth, or a napkin between the upper and lower incisors. If reinsertion is not possible, it is essential to keep the tooth in a moist environment, such as milk or saliva, avoiding dryness at all costs, and seek urgent dental care.'
'For post-trauma recommendations, patients are advised to attend follow-up appointments to monitor the traumatized tooth and maintain good oral hygiene, gently brushing the affected tooth or using a moistened cotton swab to clean the area.'
'In cases of dental avulsion, immediate care is critical, as the prognosis directly depends on the response time. Teachers, nurses, coaches, and caregivers should be aware of emergency procedures, and contact with a dentist should be made as soon as possible. It is important to determine whether the tooth is deciduous or permanent. Deciduous teeth should not be reimplanted, while permanent teeth should be reimplanted immediately.'
'For first aid in cases of dental avulsion, the steps include: Calm the patient; identify whether the tooth is permanent or deciduous; hold the tooth by the crown, avoiding contact with the root; rinse it with milk, saline, or saliva, and avoid using water if possible; reimplant it into the socket, ensuring the correct orientation; if reimplantation is not possible, store the tooth in milk, saliva, or saline; and take the patient to a dentist immediately.'
'In cases of crown fractures, preserving the dental fragment is essential, as the dentist can often reattach it. This approach is particularly beneficial for fractured teeth in adolescents, where extensive restorations such as crowns are not viable. Reattaching the fragment allows for quick and effective restoration, improving aesthetics and psychological well-being, while providing a more robust restoration compared to other materials. To preserve the fractured fragment, avoid letting it dry out by keeping it in a solution such as saliva, milk, or saline.'
'For managing a crown fracture, the ideal approach is for the patient to remain calm, locate the fragment, and place it in a small container with saliva, milk, or saline to completely cover it. Avoid rinsing the fragment with tap water, as this could prevent successful reattachment. The dentist will clean the fragment before any reattachment attempts. If the fragment cannot be found, emergency dental care should be sought immediately. If there is bleeding from the gums or the internal part of the tooth, apply a moist piece of gauze, cotton swab, or clean cloth to the fractured area and ask the patient to bite down gently. Take the patient to a dentist or emergency room as soon as possible, along with the fragment.'
'In cases of luxation injuries, although less severe than avulsions, they are considered emergencies due to symptoms such as bleeding, pain, displacement, tooth mobility, and bite disturbances. Immediate repositioning and stabilization are essential for proper healing and long-term outcomes. While repositioning can be attempted at the accident site, it is preferable to take the patient to a dentist for a more precise and less harmful procedure.'
'For first aid in cases of luxated teeth, the management includes: Calm the patient; assess the tooth for pain, displacement, and mobility; place a moist piece of gauze, cotton swab, or clean cloth between the upper and lower teeth and ask the patient to bite down gently; and refer the patient immediately to a dentist or emergency room.'
)

st.sidebar.markdown(
    """
    <style>
    .footer {
        font-size: 12px;
        text-align: center;
    }
    </style>
    <div class="footer">DentaAId enables conversations in over 50 languages. Start chatting in your native language.<br></div>

    """,
    unsafe_allow_html=True
)


# Criação da função para renderizar a conversa com barra de rolagem
def render_chat(hst_conversa):
    for i in range(1, len(hst_conversa)):
        if i % 2 == 0:
            msg("**Dental AId**:" + hst_conversa[i]['content'], key=f"bot_msg_{i}")
        else:
            msg("**You**:" + hst_conversa[i]['content'], is_user=True, key=f"user_msg_{i}")

    # Código para a barra de rolagem
    st.session_state['rendered'] = True
    if st.session_state['rendered']:
        script = """
        const chatElement = document.querySelector('.streamlit-chat');
        chatElement.scrollTop = chatElement.scrollHeight;
        """
        st.session_state['rendered'] = False
        st.write('<script>{}</script>'.format(script), unsafe_allow_html=True)

st.write("***")

if 'hst_conversa' not in st.session_state:
    st.session_state.hst_conversa = [{"role": "user", "content": condicoes}]

if text_input_center:
    st.session_state.hst_conversa.append({"role": "user", "content": text_input_center})
    retorno_openai = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=st.session_state.hst_conversa,
        max_tokens=500,
        n=1
    )
    st.session_state.hst_conversa.append({"role": "assistant", "content": retorno_openai['choices'][0]['message']['content']})

# RENDERIZAÇÃO DA CONVERSA
if len(st.session_state.hst_conversa) > 1:
    render_chat(st.session_state.hst_conversa)
