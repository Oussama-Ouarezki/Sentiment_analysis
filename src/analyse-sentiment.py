import pandas as pd
from transformers import pipeline
from tqdm import tqdm
import torch

# --- CONFIGURATION (Modèle Spécial Dialecte Arabe/Algérien) ---
INPUT_FILE = 'Comments.xlsx'
OUTPUT_FILE = 'Comments_Analyzed_Algeria.xlsx'


MODEL_NAME = "CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment"

def main():
    print("=== DÉMARRAGE : ANALYSE DARIJA / ARABE ===")
    
    # 1. CHARGEMENT
    try:
        df = pd.read_excel(INPUT_FILE)
    except FileNotFoundError:
        print(f"ERREUR : {INPUT_FILE} introuvable.")
        return

    df_clean = df.dropna(subset=['Comments']).copy()
    df_clean['Comments'] = df_clean['Comments'].astype(str)
    print(f"Commentaires à analyser : {len(df_clean)}")

    # 2. INITIALISATION IA
    print(f"\nChargement du modèle Arabe Dialectal : {MODEL_NAME}")
    
    try:
        sentiment_analyzer = pipeline(
            "text-classification", 
            model=MODEL_NAME, 
            tokenizer=MODEL_NAME,
            max_length=512, 
            truncation=True,
            top_k=None # Important pour avoir les scores précis
        )
    except Exception as e:
        print(f"ERREUR CHARGEMENT : {e}")
        return

    # 3. FONCTION D'ANALYSE (Labels spécifiques à ce modèle)
    def analyze_algerian_comment(text):
        try:
            # Ce modèle retourne 3 labels : 'positive', 'negative', 'neutral'
            results = sentiment_analyzer(text[:512])[0]
            
            # On cherche le label avec le plus haut score
            best_res = max(results, key=lambda x: x['score'])
            label = best_res['label'] # 'positive', 'negative', 'neutral'
            score = best_res['score']

            # Traduction simple pour votre fichier Excel
            if label == 'positive':
                return "Positif", score
            elif label == 'negative':
                return "Négatif", score
            else:
                return "Neutre", score

        except Exception as e:
            return "Erreur", 0.0

    # 4. EXÉCUTION
    print("\nAnalyse en cours (Supporte Darija & Emojis)...")
    tqdm.pandas(desc="Progression")
    results = df_clean['Comments'].progress_apply(lambda x: pd.Series(analyze_algerian_comment(x)))
    
    df_clean['AI_Sentiment'] = results[0]
    df_clean['Confidence'] = results[1]

    # 5. SAUVEGARDE
    print(f"\nSauvegarde dans {OUTPUT_FILE}...")
    df_clean.to_excel(OUTPUT_FILE, index=False)
    
    print("\n=== EXEMPLE DE RÉSULTATS ATTENDUS ===")
    print(df_clean[['Comments', 'AI_Sentiment']].head(10))

if __name__ == "__main__":
    main()
