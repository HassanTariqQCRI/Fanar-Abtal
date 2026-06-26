# Fanar API reference notes for Fanar Abtal

Source: screenshots supplied by Amina from the Fanar API documentation on 2026-06-26.

Purpose: keep the important Fanar model and endpoint information in the Fanar Abtal project so future features can be added consistently.

Important: verify these details against the official Fanar API documentation before production use, because models, limits, and authorization rules can change.

## Base API information

- Base URL: `https://api.fanar.qa`
- API access request page: `https://api.fanar.qa/request`
- OpenAI-compatible style:
  - Use the API domain followed by `/v1`.
  - Example base URL for OpenAI-compatible clients: `https://api.fanar.qa/v1`
- Authentication:
  - All endpoints require a Bearer token.
  - Header format:

```text
Authorization: Bearer YOUR_API_KEY
```

Do not place the real API key in source code or GitHub. Store it in `.env` locally and Streamlit secrets when deployed.

## Recommended environment variables for this app

Use these names in `.env` or Streamlit secrets:

```text
FANAR_API_KEY=...

FANAR_TEXT_URL=https://api.fanar.qa/v1/chat/completions
FANAR_TEXT_MODEL=Fanar

FANAR_IMAGE_URL=https://api.fanar.qa/v1/images/generations
FANAR_IMAGE_MODEL=Fanar-Oryx-IG-2

FANAR_TTS_URL=https://api.fanar.qa/v1/audio/speech
FANAR_TTS_MODEL=Fanar-Aura-TTS-2
FANAR_TTS_VOICE_EN=Amelia
FANAR_TTS_VOICE_AR=Hamad

FANAR_STT_URL=https://api.fanar.qa/v1/audio/transcriptions
FANAR_STT_MODEL=Fanar-Aura-STT-1
FANAR_STT_LONG_MODEL=Fanar-Aura-STT-LF-1

FANAR_TRANSLATION_URL=https://api.fanar.qa/v1/translations
FANAR_TRANSLATION_MODEL=Fanar-Shaheen-MT-1

FANAR_MODERATION_URL=https://api.fanar.qa/v1/moderations
FANAR_MODERATION_MODEL=Fanar-Guard-2

FANAR_POEM_URL=https://api.fanar.qa/v1/poems/generations
FANAR_POEM_MODEL=Fanar-Diwan

FANAR_MODELS_URL=https://api.fanar.qa/v1/models
```

## Chat completion

Endpoint:

```text
POST /v1/chat/completions
```

Required request fields:

- `model`
- `messages`

Visible model options from screenshots:

- `Fanar`
- `Fanar-S-1-7B`
- `Fanar-C-1-8.7B`
- `Fanar-C-2-27B`
- `Fanar-Sadiq`
- `Fanar-Sadiq-Agentic`
- `Fanar-Oryx-IVU-2`

Notes:

- `Islamic-RAG` is replaced with `Fanar-Sadiq`; use `Fanar-Sadiq` instead.
- `enable_thinking` appears to apply only when the selected model supports it. The screenshots mention `Fanar-C-2-27B` and additional authorization.
- `Fanar-Sadiq` supports source filtering fields such as:
  - `exclude_sources`
  - `filter_sources`
  - `book_names`
- Source names can include predefined names or values starting with `digital_seerah`.

Example `book_names` values visible in screenshots:

- `أصل الزراري شرح صحيح البخاري - مخطوط`
- `جمهرة تراجم الفقهاء المالكية`
- `مختصر تحفة المحتاج بشرح المنهاج`
- `شرح رياض الصالحين - حطبية`
- `تفسير العثيمين: الزمر`

Other visible optional fields:

- `best_of`
- `early_stopping`
- `enable_thinking`
- `frequency_penalty`
- `ignore_eos`
- `length_penalty`
- `logit_bias`

## Text-to-speech

Endpoint:

```text
POST /v1/audio/speech
```

Purpose: generate audio from input text.

Required request fields:

- `input`: text to generate audio for
- `model`
- `voice`

Model options visible:

- `Fanar-Aura-TTS-2`
- `Fanar-Sadiq-TTS-1`

Supported output formats:

- `mp3`
- `wav`

Useful optional fields:

- `response_format`: `mp3` or `wav`
- `stream`: stream the audio as it is generated; supported for both `mp3` and `wav`
- `with_emotion`: emotional speech synthesis

Important emotion note:

- `with_emotion` is only applicable to `Fanar-Aura-TTS-2`.
- It also requires a voice where `emotion: true` appears in the voices list.
- If unsupported, the request can be rejected with a `422` error.
- Default is `false`.

Example request shape:

```json
{
  "model": "Fanar-Aura-TTS-2",
  "input": "Hello! I hope you are having a wonderful day.",
  "voice": "Amelia",
  "response_format": "mp3"
}
```

Recommended Fanar Abtal use:

- Add “Listen to this story” in My Story Maker.
- Add Arabic and English story narration.
- Use voice by child language:
  - English: `Amelia`, `Emily`, `Harry`, or `Jake`
  - Arabic: `Hamad`, `Huda`, `Jasim`, `Noor`, `Radwa`, or `Abdulrahman`

## Available TTS voices

Visible public voices from screenshots:

| Voice | Gender | Language |
| --- | --- | --- |
| Abdulrahman | Male | Arabic |
| Amelia | Female | English |
| Emily | Female | English |
| Hamad | Male | Arabic |
| Harry | Male | English |
| Huda | Female | Arabic |
| Jake | Male | English |
| Jasim | Male | Arabic |
| Noor | Female | Arabic |
| Radwa | Female | Arabic |

The voices API response may include:

- `name`
- `name_ar`
- `gender`
- `accent`
- `languages`
- `type`
- `emotion`

Example details visible:

- `Amelia`: Arabic name `أميليا`, female, British accent, English, public, emotion false.
- `Hamad`: Arabic name `حمد`, male, Gulf accent, Arabic, public, emotion false.

For `Fanar-Sadiq-TTS-1`, Quranic text can use `quran_reciter`.

Visible `quran_reciter` values:

- `abdul-basit`
- `maher-al-muaiqly`
- `mahmoud-al-husary`

## Speech-to-text

Endpoint:

```text
POST /v1/audio/transcriptions
```

Purpose: transcribe audio into the input language.

Request content type:

```text
multipart/form-data
```

Required request fields:

- `file`: binary audio file
- `model`

Model options visible:

- `Fanar-Aura-STT-1`: for short audio clips up to about 20–30 seconds
- `Fanar-Aura-STT-LF-1`: for long-form transcription of longer audio files

Output format options visible:

- `text`
- `srt`
- `json`

Important note:

- The screenshot says `Fanar-Aura-STT-1` only supports `text` format.

Example cURL shape:

```bash
curl -X POST "https://api.fanar.qa/v1/audio/transcriptions" \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@sample.wav" \
  -F "model=Fanar-Aura-STT-1"
```

Recommended Fanar Abtal use:

- Let parents speak their story idea instead of typing.
- Let children record a short answer after an activity.
- Use short model by default.
- Use long-form model only for longer audio because the rate limit is lower.

## List voices

Endpoint:

```text
GET /v1/audio/voices
```

Purpose: list all available text-to-speech voices.

Notes:

- Built-in public voices are included by default.
- Personalized voices are included only when the API key is authorized for them.
- Personalized voices appear with `type: "personal"`.

## Personalized voice creation

Endpoint:

```text
POST /v1/audio/voices
```

Purpose: create a personalized voice for speech generation.

Important:

- This endpoint requires additional authorization.
- It is not allowed by default.
- The screenshots say to contact `support@fanar.qa`.

Request content type:

```text
multipart/form-data
```

Required fields:

- `audio`: WAV audio sample
- `name`: unique personalized voice name
- `transcript`: transcript of the audio sample

Notes:

- Only WAV format is accepted.
- Public voices and personalized voices live in separate namespaces.
- If the same name exists in both, the personalized voice takes precedence during speech generation.

Delete personalized voice:

```text
DELETE /v1/audio/voices/{name}
```

This also requires additional authorization and is not allowed by default.

Recommendation for Fanar Abtal:

- Do not build personalized voice as a default hackathon feature yet.
- Add it later only if Fanar grants extra authorization.

## Image generation

Endpoint:

```text
POST /v1/images/generations
```

Purpose: create an image from a text prompt.

Model:

- `Fanar-Oryx-IG-2`

Required fields:

- `model`: `Fanar-Oryx-IG-2`
- `prompt`: text description of the desired image

Optional field:

- `revise`: whether to automatically revise the prompt to improve style, quality, and cultural alignment.

Recommended Fanar Abtal use:

- Generate four story illustrations in My Story Maker.
- Generate child-friendly, culturally respectful images for Qatar families.
- Cache generated images where possible because daily limits are low.

## Image understanding / image-to-text

Visible model name:

- `Fanar-Oryx-IVU-2`

Notes:

- The screenshots show this model in the model/rate-limit list, but the exact image-to-text request shape was not captured.
- Keep the current local OCR fallback for WhatsApp flyers until the mentor confirms the correct Fanar image-to-text API usage.

Recommended Fanar Abtal use once confirmed:

- Replace or supplement local OCR for Activity Companion.
- Let parents upload WhatsApp flyers and ask Fanar to extract event details.
- Keep “Needs confirmation” for unclear dates, prices, locations, and registration links.

## Translation

Endpoint:

```text
POST /v1/translations
```

Purpose: translate text into the specified language.

Model:

- `Fanar-Shaheen-MT-1`

Required fields:

- `model`: `Fanar-Shaheen-MT-1`
- `text`: text to translate; must not exceed 4,000 words
- `langpair`

Supported `langpair` values:

- `en-ar`: English to Arabic
- `ar-en`: Arabic to English

Optional preprocessing values:

- `default`: splits sentences by natural punctuation, trims whitespace, removes HTML tags
- `preserve_html`
- `preserve_whitespace`
- `preserve_whitespace_and_html`

Recommended Fanar Abtal use:

- Add bilingual Arabic/English support for Qatar communities.
- Translate activity flyers and parent guidance.
- Let the app output in the family’s selected language.

## Moderation and cultural safety

Endpoint:

```text
POST /v1/moderations
```

Purpose: identify safety and cultural-awareness scores.

Model:

- `Fanar-Guard-2`

Required fields:

- `model`: `Fanar-Guard-2`
- `prompt`
- `response`

Screenshot description:

- FanarGuard gives each prompt-response pair safety and cultural-awareness scores.
- This allows moderation thresholds to be tailored to the deployment.
- The screenshot references cultural awareness: `https://arxiv.org/abs/2511.18852`

Recommended Fanar Abtal use:

- Run generated child-facing content through moderation before display.
- Use it especially for My Story Maker, Parent Story Studio, and Activity Companion.
- If content is flagged, show a gentle fallback message and ask the user to revise.

## Poems

Endpoint:

```text
POST /v1/poems/generations
```

Purpose: create a poem from a prompt.

Model:

- `Fanar-Diwan`

Required fields:

- `model`: `Fanar-Diwan`
- `prompt`

Recommended Fanar Abtal use:

- Add “Make it a poem” for children.
- Create Arabic or English motivational poems after completing an activity.

## Tokens

Endpoint:

```text
POST /v1/tokens
```

Purpose: count tokens and check maximum request tokens.

Required fields visible:

- `content`
- `model`

Visible model values:

- `Fanar-S-1-7B`
- `Fanar-C-1-8.7B`
- `Fanar-C-2-27B`

Response fields visible:

- `tokens`
- `max_request_tokens`

Recommended Fanar Abtal use:

- Check prompt size before sending long story/flyer content.
- Avoid request failures for long inputs.

## Models

Endpoint:

```text
GET /v1/models
```

Purpose: list the currently available models.

Recommended Fanar Abtal use:

- Add a developer-only diagnostic button to confirm available models.
- Do not show this to children or normal parent users.

## Rate limits visible in screenshots

| Model | Rate limit |
| --- | --- |
| Fanar | 50 requests/minute |
| Fanar-S-1-7B | 50 requests/minute |
| Fanar-C-1-8.7B | 50 requests/minute |
| Fanar-C-2-27B | 50 requests/minute |
| Fanar-Sadiq | 50 requests/minute |
| Fanar-Sadiq-Agentic | 50 requests/minute |
| Fanar-Sadiq-TTS-1 | 20 requests/day |
| Fanar-Oryx-IVU-2 | 20 requests/day |
| Fanar-Aura-TTS-2 | 20 requests/day |
| Fanar-Aura-STT-1 | 20 requests/day |
| Fanar-Aura-STT-LF-1 | 10 requests/day |
| Fanar-Oryx-IG-2 | 20 requests/day |
| Fanar-Guard-2 | 50 requests/minute |
| Fanar-Shaheen-MT-1 | 20 requests/day |
| Fanar-Diwan | 50 requests/minute |

Design implication:

- Use caching and avoid repeated calls when the user clicks buttons multiple times.
- TTS, STT, image generation, image understanding, and translation have daily limits.
- Chat, moderation, poem generation, and some text models have higher per-minute limits.

## Common response/error codes

| Status | Meaning |
| --- | --- |
| 200 | Successful response |
| 400 | Content was filtered |
| 401 | Invalid authentication |
| 403 | Invalid authorization |
| 404 | Not found |
| 409 | Conflict |
| 410 | No longer supported |
| 413 | Request entity too large |
| 422 | Unprocessable |
| 429 | Rate limit reached or exceeded quota |
| 500 | Internal server error |
| 503 | Service overloaded |
| 504 | Request timed out |

## Suggested Fanar Abtal feature roadmap

1. Story narration
   - Add “Listen to story” using `POST /v1/audio/speech`.
   - Use Arabic or English voice based on the selected child language.

2. Parent and child voice input
   - Add speech-to-text with `POST /v1/audio/transcriptions`.
   - Use short audio model by default: `Fanar-Aura-STT-1`.
   - Use long-form model only when needed: `Fanar-Aura-STT-LF-1`.

3. Bilingual support for Qatar communities
   - Use `Fanar-Shaheen-MT-1`.
   - Support `en-ar` and `ar-en`.

4. Child safety layer
   - Use `Fanar-Guard-2` to review generated prompt-response pairs.
   - This is important because the app is child-facing.

5. Image generation
   - Use `Fanar-Oryx-IG-2` for story illustrations.
   - Keep prompts culturally respectful and child-friendly.

6. WhatsApp flyer reading
   - Continue local OCR fallback for now.
   - Add Fanar image-to-text when `Fanar-Oryx-IVU-2` usage is confirmed by the mentor.

7. Poems and reflection
   - Use `Fanar-Diwan` to create short celebration poems after a child completes a journey.

8. Developer diagnostics
   - Add a hidden or admin-only area for:
     - test API key
     - list models
     - list voices
     - check rate limit failures gracefully

## Implementation reminders

- Never commit real API keys to GitHub.
- Use Streamlit secrets for the deployed app.
- Keep fallback messages friendly and simple for parents.
- Add “Needs confirmation” whenever Fanar or OCR is uncertain.
- Cache expensive calls where possible.
- For child-facing features, prefer short outputs, clear language, and parent-visible safety notes.
