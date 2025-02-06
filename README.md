****Spam Detection App****
This is a Spam Detection App built with Logistic Regression for classifying text messages as spam or ham (legitimate). 
The app uses Natural Language Processing (NLP) techniques, implemented through the NLTK library, to preprocess the text and perform the classification.

****Features***
Text Preprocessing: Tokenization, stopword removal, lemmatization, and TF-IDF vectorization.
Spam Classification: Uses a trained Logistic Regression model to predict whether a message is spam or ham.
Streamlit Interface: User-friendly interface for real-time classification.
Custom Training: Ability to fine-tune the model with new datasets.
Technologies Used
****Python****
NLTK (Natural Language Toolkit)
scikit-learn (for Logistic Regression)
Streamlit (for creating the web app)

****File Structure****
spam_classifier.py: Contains the Logistic Regression model used for spam classification.
tfidf_vectorizer.pkl: The serialized TF-IDF vectorizer used to convert text into numerical form.
streamlit_app.py: The main Streamlit app to interact with the model.
spam_data.csv: Example dataset for training (if included in your project).

Setup Instructions:
1. Clone the repository
   git clone https://github.com/Asmae-Bouhadioui/Spam-Detection.git
   cd Spam-Detection
2. Install the required dependencies:
   python3 -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   pip install -r requirements.txt

3. Run the Streamlit app
   streamlit run app.py

