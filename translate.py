from google.cloud import translate
import os

client = translate.TranslationServiceClient()
project_id = os.environ.get("PROJECT_ID")
location = "global"
parent = f"projects/{project_id}/locations/{location}"


def translate_text(text="Hello, world!"):
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": "en-US",
            "target_language_code": "lt",
        }
    )
    return response.translations[0].translated_text
