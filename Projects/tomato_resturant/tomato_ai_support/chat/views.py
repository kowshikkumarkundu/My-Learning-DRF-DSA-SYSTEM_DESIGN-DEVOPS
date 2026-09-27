from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response

from google import genai

from .models import Conversation, ChatMessage, MenuItem, RestaurantInfo


# --------------------------------
# System Prompt
# --------------------------------

SYSTEM_PROMPT = """
You are the customer support assistant for Tomato Restaurant.

Your job is to help customers with:
- Menu
- Food items
- Prices
- Orders
- Delivery
- Opening hours
- Restaurant-related questions

Only answer questions related to Tomato Restaurant.

If the customer asks something unrelated to the restaurant,
politely tell them that you can only help with Tomato Restaurant
related questions.

Do not make up information.

If you don't know something, say that a customer support
representative will help them.
"""


# --------------------------------
# Menu Function
# --------------------------------

def get_menu(category: str = None):
    """
    Get available menu items from Tomato Restaurant.

    Args:
        category: The food category to search for,
                  such as Pizza or Burger.
                  Leave empty to get the full menu.
    """

    if category:
        menu_items = MenuItem.objects.filter(
            category=category,
            is_available=True
        )
    else:
        menu_items = MenuItem.objects.filter(
            is_available=True
        )

    menu = []

    for item in menu_items:
        menu.append({
            "name": item.name,
            "price": float(item.price),
            "description": item.description,
            "category": item.category,
        })

    return menu


# --------------------------------
# Restaurant Info Function
# --------------------------------

def get_restaurant_info():
    """
    Get restaurant information such as
    opening hours, delivery charge, minimum order,
    address, and delivery areas.
    """

    infos = RestaurantInfo.objects.all()

    restaurant_info = {}

    for info in infos:
        restaurant_info[info.key] = info.value

    return restaurant_info

# --------------------------------
# order function
# --------------------------------
def ordre():
    pass

# --------------------------------
# Chat API
# --------------------------------

@api_view(["POST"])
def chat(request):

    # 1. Get data from frontend

    message = request.data.get("message")
    conversation_id = request.data.get("conversation_id")


    # 2. Get or create conversation

    if conversation_id:
        conversation = Conversation.objects.get(
            id=conversation_id
        )
    else:
        conversation = Conversation.objects.create()


    # 3. Save user's message

    ChatMessage.objects.create(
        conversation=conversation,
        role="user",
        content=message
    )


    # 4. Get conversation history

    history = ChatMessage.objects.filter(
        conversation=conversation
    ).order_by("created_at")


    # 5. Convert database history into Gemini format

    contents = []

    for msg in history:

        contents.append({
            "role": "user" if msg.role == "user" else "model",
            "parts": [
                {
                    "text": msg.content
                }
            ]
        })


    # 6. Create Gemini client

    client = genai.Client(
        api_key=settings.GEMINI_API_KEY
    )


    # 7. Gemini handles tool calling automatically

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",

        contents=contents,

        config={
            "system_instruction": SYSTEM_PROMPT,

            "tools": [
                get_menu,
                get_restaurant_info
            ]
        }
    )


    # 8. Final answer

    answer = response.text


    # 9. Save AI response

    ChatMessage.objects.create(
        conversation=conversation,
        role="assistant",
        content=answer
    )


    # 10. Send response to frontend

    return Response({
        "conversation_id": conversation.id,
        "message": answer
    })





