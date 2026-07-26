from django.shortcuts import render
from deep_translator import GoogleTranslator


def translate(request):
    translated_text = ''

    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        source_language = request.POST.get('source_language')
        target_language = request.POST.get('target_language')

        if text and source_language and target_language:
            try:
                translated_text = GoogleTranslator(
                    source=source_language,
                    target=target_language
                ).translate(text)

            except Exception:
                translated_text = 'Translation failed. Please try again.'

    return render(request, 'aishat.html', {
        'translated_text': translated_text
    })