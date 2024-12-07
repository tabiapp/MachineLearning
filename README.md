# **TABI Translation API**  

This API translates text from English to Indonesian using a pre-trained machine learning model. The service is hosted on Google Cloud Run for efficient, real-time translation.

---

## **Datasets and Model**  

### **Model**  
- **Translation Model (MT.h5):**  
  [Download Here](https://storage.googleapis.com/tabi-translate/TextToText/MT.h5)  

### **Datasets**  
- **English Source Dataset:**  
  [Download OpenSubtitles.en-id.en](https://storage.googleapis.com/tabi-translate/TextToText/OpenSubtitles.en-id.en)  
- **Indonesian Target Dataset:**  
  [Download OpenSubtitles.en-id.id](https://storage.googleapis.com/tabi-translate/TextToText/OpenSubtitles.en-id.id)  

### **Tokenizers**  
- **Input Tokenizer:**  
  [Download input_tokenizer.pkl](https://storage.googleapis.com/tabi-translate/TextToText/input_tokenizer.pkl)  
- **Output Tokenizer:**  
  [Download output_tokenizer.pkl](https://storage.googleapis.com/tabi-translate/TextToText/output_tokenizer.pkl)  

---

## **API Specification**  

### **Base URL**  
```
https://translate-api-65059410484.asia-southeast2.run.app
```

---

### **Endpoint: Translate Text**  

#### **Request**  

**Method:** `GET`  
**URL:** `/translate`  

**Query Parameters:**  
| Parameter | Type   | Required | Description                  | Example         |  
|-----------|--------|----------|------------------------------|-----------------|  
| `text`    | string | Yes      | The text to translate (UTF-8)| `good morning`  |  

---

#### **Response**  

**Status Code:** `200 OK`  

**Content-Type:** `application/json`  

**Response Body:**  
```json
{
  "original_text": "good morning",
  "translated_text": "selamat pagi"
}
```

---

### **Example Usage**  

#### **Using cURL**  
```bash
curl "https://translate-api-65059410484.asia-southeast2.run.app/translate?text=good%20morning"
```

#### **Using Python (Requests)**  
```python
import requests

url = "https://translate-api-65059410484.asia-southeast2.run.app/translate"
params = {"text": "good morning"}
response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Original Text:", data["original_text"])
    print("Translated Text:", data["translated_text"])
else:
    print("Error:", response.status_code)
```
