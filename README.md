# Fanar Abtal — Road to Abtal

Fanar Abtal is a bilingual family companion for children and parents in Qatar. It helps families turn stories, activities, and learning moments into child-friendly journeys in Arabic, English, or both.

## Main features

1. **Road to Abtal**  
   Introduces the overall vision: every child can imagine, create, reflect, and grow.

2. **Parent Story Studio**  
   Parents can turn a real family moment into a personalised child story.

3. **My Story Maker — Dream Career Adventures**  
   Children choose a dream profession such as police officer, firefighter, pilot, imam, mu'adhin, Islamic scholar, teacher, engineer, or doctor. Fanar creates a safe, inspiring story with scenes and optional illustrations.

4. **Family Personalization Settings**  
   Parent Story Studio and My Story Maker include image and voice settings. Families can guide illustration style, colours, cultural setting, age-aware design, narration feeling, and optional Fanar personalized voice names when authorized.

5. **Activity Companion**  
   Parents can paste a WhatsApp caption, upload a community flyer, or use a demo flyer. Fanar turns the activity into a practical family journey:

   - what the activity is
   - who can join
   - why it may fit the child
   - what to confirm with the organiser
   - what to do before, during, and after the activity

6. **Summer Camp Extension**  
   Helps families continue a child’s camp learning at home through simple explanations, questions, missions, and parent notes.

7. **Parent Space**  
   Gives parents a simple place to review child growth, activity notes, and family conversation prompts.

## Why this matters

Many useful activities in Qatar are shared through WhatsApp groups and community flyers. Families may speak Arabic, English, or both. Fanar Abtal helps parents and children understand these opportunities and turn them into meaningful growth experiences.

## Run locally

Install the packages:

```powershell
python -m pip install -r requirements.txt
```

Create a `.env` file in the project folder. You can copy `.env.example` and replace the placeholder values:

```env
FANAR_API_KEY=your_fanar_key
FANAR_TEXT_URL=https://api.fanar.qa/v1/chat/completions
FANAR_TEXT_MODEL=Fanar
FANAR_IMAGE_URL=https://api.fanar.qa/v1/images/generations
FANAR_IMAGE_MODEL=Fanar-Oryx-IG-2
OPENAI_API_KEY=
OPENAI_IMAGE_URL=https://api.openai.com/v1/images/generations
OPENAI_IMAGE_MODEL=gpt-image-1
FANAR_TTS_URL=https://api.fanar.qa/v1/audio/speech
FANAR_TTS_MODEL=Fanar-Aura-TTS-2
FANAR_TTS_VOICE_EN=Amelia
FANAR_TTS_VOICE_AR=Hamad
```

Optional, when a Fanar image-to-text model is available:

```env
FANAR_VISION_MODEL=Fanar-Oryx-IVU-2
```

Optional personalized voice names, only if Fanar has authorized and created them:

```env
FANAR_TTS_VOICE_FATHER=
FANAR_TTS_VOICE_MOTHER=
FANAR_TTS_VOICE_GRANDPARENT=
FANAR_TTS_VOICE_FAVORITE=
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

The Activity Companion uses Fanar image-to-text (`Fanar-Oryx-IVU-2`) first to read uploaded flyer images. Local OCR is only a backup if Fanar image reading is unavailable. For the backup to work, install the Tesseract OCR desktop application with English and Arabic language data.

If OCR or Fanar image reading is not available, the app still works: parents can paste the WhatsApp caption or visible flyer text.

## Image generation fallback

Story illustrations use Fanar image generation first (`Fanar-Oryx-IG-2`). If Fanar image generation is unavailable, the app can use GPT image generation when `OPENAI_API_KEY` is configured. Bundled sample illustrations remain the final fallback.

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
