from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.sequence import pad_sequences
import pickle
import numpy as np
import os

# Load model dan tokenizer
model = tf.keras.models.load_model("MT.h5")

# Load tokenizer
with open("input_tokenizer.pkl", "rb") as f:
    input_tokenizer = pickle.load(f)
with open("output_tokenizer.pkl", "rb") as f:
    output_tokenizer = pickle.load(f)

# Parameter global
max_length = 50

# Flask app
app = Flask(__name__)

def translate_sentence(input_sentence, model, input_tokenizer, output_tokenizer, max_length):
    # Preprocess input sentence
    input_sentence = '<start> ' + input_sentence.strip().lower() + ' <end>'
    input_sequence = input_tokenizer.texts_to_sequences([input_sentence])
    input_sequence = pad_sequences(input_sequence, maxlen=max_length, padding='post')
    
    # Initialize the decoder input with <start> token
    start_token = output_tokenizer.word_index['<start>']
    end_token = output_tokenizer.word_index['<end>']
    target_sequence = np.zeros((1, max_length))
    target_sequence[0, 0] = start_token
    print("Start Token:", output_tokenizer.word_index.get('<start>'))
    print("End Token:", output_tokenizer.word_index.get('<end>'))

    translated_sentence = []
    for i in range(1, max_length):
        # Predict next token
        predictions = model.predict([input_sequence, target_sequence], verbose=0)
        predicted_id = np.argmax(predictions[0, i - 1])
        print(f"Step {i}: Predicted ID = {predicted_id}, Word = {output_tokenizer.index_word.get(predicted_id, '')}")

        # Stop if <end> token is predicted
        if predicted_id == end_token:
            break
        
        # Append the predicted word
        translated_sentence.append(output_tokenizer.index_word.get(predicted_id, ''))
        target_sequence[0, i] = predicted_id
        
    print("Final Translated Sentence:", ' '.join(translated_sentence))
    return ' '.join(translated_sentence)


@app.route('/translate', methods=['GET'])
def translate():
    # Get text from query parameters
    input_text = request.args.get('text', default='', type=str)
    if not input_text:
        return jsonify({"error": "Parameter 'text' is required"}), 400

    # Translate the sentence
    translated_text = translate_sentence(input_text, model, input_tokenizer, output_tokenizer, max_length)

    return jsonify({"input_text": input_text, "translated_text": translated_text})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Default port 8080
    app.run(host='0.0.0.0', port=port)
