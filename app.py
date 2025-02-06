import streamlit as st
import joblib
import os

if not os.path.exists("tfidf_vectorizer.joblib"):
    st.error("❌ Le fichier 'tfidf_vectorizer.joblib' est introuvable ! Vérifiez son emplacement.")
if not os.path.exists("spam_classifier.joblib"):
    st.error("❌ Le fichier 'spam_classifier.joblib' est introuvable ! Vérifiez son emplacement.")


vectorizer = joblib.load('tfidf_vectorizer.joblib')  # Chargement du vectorizer ajusté
model = joblib.load('spam_classifier.joblib')  # Chargement du modèle

st.title("📩 Détection de Spam avec Régression Logistique")

# Fonction pour prédire si un message est spam ou non
def predict_spam(message):
    message_vec = vectorizer.transform([message])  # Transformer le message avant de prédire
    prediction = model.predict(message_vec)
    return "🚨 Spam" if prediction == 1 else "✅ Non-Spam"

# Champ de saisie
user_input = st.text_area("✏️ Entrez un message texte pour tester :")

if st.button("🔍 Vérifier le message"):
    if user_input:
        result = predict_spam(user_input)
        st.write(result)  # Affichage du résultat dans Streamlit
    else:
        st.warning("⚠️ Veuillez entrer un message avant de tester.")
