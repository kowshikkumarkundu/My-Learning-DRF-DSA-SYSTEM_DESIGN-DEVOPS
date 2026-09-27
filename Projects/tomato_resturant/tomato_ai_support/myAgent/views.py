from django.shortcuts import render
from .tools import write_file,read_file,list_files
from google import genai
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.conf import   settings

tools = [
    write_file,
    read_file,
    list_files
]

@api_view(["GET","POST"])
def agent(request):
    message = request.data.get("message")

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=message,
        config={
            "tools": tools
        }
    )

    print(response)
    return Response({
        "message": message,
        "reply":response
    })