
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from deep_translator import GoogleTranslator

@api_view(['GET', 'POST'])
def translate_text(request):
    if request.method == 'GET':
        return Response({"message": "Use POST com 'text' e 'target'."})

    if request.method == 'POST':
        text = request.data.get("text")
        target_lang = request.data.get("target")

        if not text or not target_lang:
            return Response(
                {"error": "Campos 'text' e 'target' são obrigatórios."},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            translated = GoogleTranslator(source="auto", target=target_lang).translate(text)
            return Response({"translated_text": translated})
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
