# Fanar Abtal — Road to Abtal

Fanar Abtal is a bilingual family companion for children and parents in Qatar. It helps families turn stories, activities, and learning moments into child-friendly journeys in Arabic, English, or both.

## Main features

1. **Road to Abtal**  
   Introduces the overall vision: every child can imagine, create, reflect, and grow.

2. **Parent Story Studio**  
   Parents can turn a real family moment into a personalised child story.

3. **My Story Maker — Dream Career Adventures**  
   Children choose a dream profession such as police officer, firefighter, pilot, imam, mu'adhin, Islamic scholar, teacher, engineer, or doctor. Fanar creates a safe, inspiring story with scenes and optional illustrations.

4. **Activity Companion**  
   Parents can paste a WhatsApp caption, upload a community flyer, or use a demo flyer. Fanar turns the activity into a practical family journey:

   - what the activity is
   - who can join
   - why it may fit the child
   - what to confirm with the organiser
   - what to do before, during, and after the activity

5. **Summer Camp Extension**  
   Helps families continue a child’s camp learning at home through simple explanations, questions, missions, and parent notes.

6. **Parent Space**  
   Gives parents a simple place to review child growth, activity notes, and family conversation prompts.

## Why this matters

Many useful activities in Qatar are shared through WhatsApp groups and community flyers. Families may speak Arabic, English, or both. Fanar Abtal helps parents and children understand these opportunities and turn them into meaningful growth experiences.

## Run locally

Install the packages:

```powershell
python -m pip install -r requirements.txt
```

Create a `.env` file in the project folder:

```env
FANAR_API_KEY=your_fanar_key
FANAR_TEXT_URL=https://api.fanar.qa/v1/chat/completions
FANAR_TEXT_MODEL=Fanar
FANAR_IMAGE_URL=https://api.fanar.qa/v1/images/generations
FANAR_IMAGE_MODEL=Fanar-Oryx-IG-2
```

Optional, when a Fanar image-to-text model is available:

```env
FANAR_VISION_MODEL=your_fanar_image_to_text_model
```

Start the app:

```powershell
streamlit run app.py
```

Then open:

```text
http://localhost:8501
```

## OCR note

The Activity Companion can use local OCR as a backup to read flyer text. For this to work, install the Tesseract OCR desktop application with English and Arabic language data.

If OCR or Fanar image reading is not available, the app still works: parents can paste the WhatsApp caption or visible flyer text.

## Deploy for sharing

Recommended demo deployment:

1. Upload this project to a private GitHub repository.
2. Do **not** upload `.env`.
3. Deploy the repository on Streamlit Community Cloud.
4. Add the Fanar API key and model settings in Streamlit Secrets.
5. Send the Streamlit app link to reviewers.

## Suggested message to reviewer

Dear Dr. Hamdy,

I am sharing my Fanar Abtal prototype for review. The app demonstrates bilingual family support for children in Qatar, including Parent Story Studio, My Story Maker, Activity Companion, Summer Camp Extension, and Parent Space.

The Activity Companion shows how Fanar can help families use WhatsApp community activity flyers by turning them into practical before, during, and after guidance for parents and children.

Best regards,  
Amina
