from google import genai
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings
from .models import Conversation, ChatMessage


@api_view(["POST"])
def chat(request):

    message = request.data.get("message")


    client = genai.Client(api_key=settings.GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=message
    )

    return Response({
        "message": message,
        "reply": response.text
    })