from rest_framework import generics, permissions
from .models import Trip
from .serializers import TripSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from .models import Trip
from .serializers import TripSerializer
from .utils.itinerary_generator import generate_basic_itinerary



class TripCreateView(generics.CreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class PlanTripView(APIView):
    def post(self, request):
        data = request.data

        try:
            destination = data.get('destination')
            start_date = datetime.strptime(data.get('start_date'), '%Y-%m-%d')
            end_date = datetime.strptime(data.get('end_date'), '%Y-%m-%d')
            budget = int(data.get('budget'))
            currency = data.get('currency')
            travel_type = data.get('travel_type')

            itinerary = generate_basic_itinerary(destination, start_date, end_date, budget, travel_type)

            # Optional: Save the trip
            trip = Trip.objects.create(
                user=request.user,
                destination=destination,
                start_date=start_date,
                end_date=end_date,
                budget=budget,
                currency=currency,
                travel_type=travel_type,
                itinerary=itinerary  # if using JSONField
            )

            return Response({'itinerary': itinerary}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

### Logic for Itenary generation from open ai's api.

# import datetime
# import openai
# from openai import OpenAI
# from django.conf import settings
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status

# client = OpenAI(api_key=settings.OPENAI_API_KEY)




# # openai.api_key = settings.OPENAI_API_KEY

# class GenerateItineraryView(APIView):
#     def post(self, request):
#         try:
#             destination = request.data.get('destination')
#             start_date = request.data.get('start_date')
#             end_date = request.data.get('end_date')
#             budget = request.data.get('budget')
#             currency = request.data.get('currency', '₹')
#             travel_type = request.data.get('travel_type', 'solo')

#             if not all([destination, start_date, end_date, budget]):
#                 return Response({"error": "All fields are required."}, status=status.HTTP_400_BAD_REQUEST)

#             prompt = (
#                 f"Generate a personalized travel itinerary for a {travel_type} trip to {destination} "
#                 f"from {start_date} to {end_date}. Budget is {currency}{budget}. "
#                 "Make it detailed and enjoyable day-wise."
#             )

#             response = openai.chat.completions.create(
#                 model="gpt-3.5-turbo",
#                 messages=[
#                     {"role": "system", "content": "You are a helpful travel planner."},
#                     {"role": "user", "content": prompt},
#                 ],
#                 temperature=0.8,
#                 max_tokens=1000
#             )

#             itinerary = response.choices[0].message.content.strip()
#             return Response({"itinerary": itinerary}, status=status.HTTP_200_OK)

#         except Exception as e:
#             print("Error:", e)
#             return Response({"error": "Something went wrong while generating itinerary."},
#                             status=status.HTTP_500_INTERNAL_SERVER_ERROR)


###Open Router AI logic code.
# import httpx
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from django.conf import settings

# @api_view(['POST'])
# def generate_itinerary_openrouter(request):
#     data = request.data

#     source = data.get("source")
#     destination = data.get("destination")
#     start_date = data.get("start_date")
#     end_date = data.get("end_date")
#     budget = data.get("budget")
#     currency = data.get("currency", "INR")
#     travel_type = data.get("travel_type", "dual")

#     if not all([source,destination, start_date, end_date, budget,currency,travel_type]):
#         return JsonResponse({'error': 'Missing required fields'}, status=400)

#     prompt = f"""
#     You are a travel assistant AI. Generate a detailed day-by-day itinerary for a {travel_type} People trip from {source} to {destination} 
#     from {start_date} to {end_date}, with a budget of {budget} {currency}. Include activities, places to visit, and estimated daily cost.
#     """

#     try:
#         headers = {
#             "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
#             "HTTP-Referer": "https://tourgeniephase1-backend.onrender.com",  # replace with your domain or GitHub link
#             "Content-Type": "application/json"
#         }

#         body = {
#             "model": "mistralai/mixtral-8x7b-instruct",  # or gpt-3.5, meta-llama, etc.
#             "messages": [{"role": "user", "content": prompt}],
#         }

#         response = httpx.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=body)
#         response.raise_for_status()

#         content = response.json()
#         itinerary = content["choices"][0]["message"]["content"]

#         return JsonResponse({"itinerary": itinerary})

#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=500)


# import httpx
# from django.http import JsonResponse
# from rest_framework.decorators import api_view
# from django.conf import settings
# import traceback

# @api_view(['POST'])
# def generate_itinerary_openrouter(request):
#     data = request.data

#     source = data.get("source")
#     destination = data.get("destination")
#     start_date = data.get("start_date")
#     end_date = data.get("end_date")
#     budget = data.get("budget")
#     currency = data.get("currency", "INR")
#     travel_type = data.get("travel_type", "dual")

#     if not all([source, destination, start_date, end_date, budget, currency, travel_type]):
#         return JsonResponse({'error': 'Missing required fields'}, status=400)

#     prompt = f"""
#     You are a travel assistant AI. Generate a detailed day-by-day itinerary for a {travel_type} People trip from {source} to {destination} 
#     from {start_date} to {end_date}, with a budget of {budget} {currency}. Include activities, places to visit, and estimated daily cost.
#     """

#     try:
#         headers = {
#             "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
#             "Referer": "https://tourgeniephase1-backend.onrender.com",
#             "Content-Type": "application/json"
#         }

#         body = {
#             "model": "mistralai/mixtral-8x7b-instruct",
#             "messages": [{"role": "user", "content": prompt}],
#         }

#         response = httpx.post(
#             "https://openrouter.ai/api/v1/chat/completions",
#             headers=headers,
#             json=body,
#             timeout=30.0
#         )

#         print("RESPONSE TEXT:", response.text)

#         response.raise_for_status()
#         content = response.json()

#         itinerary = content["choices"][0]["message"]["content"]

#         return JsonResponse({"itinerary": itinerary})

#     except Exception as e:
#         traceback.print_exc()
#         return JsonResponse({'error': str(e)}, status=500)




import httpx
import traceback
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.conf import settings

@api_view(['POST'])
def generate_itinerary_openrouter(request):
    data = request.data

    source = data.get("source")
    destination = data.get("destination")
    start_date = data.get("start_date")
    end_date = data.get("end_date")
    budget = data.get("budget")
    currency = data.get("currency", "INR")
    travel_type = data.get("travel_type", "dual")

    if not all([source, destination, start_date, end_date, budget, currency, travel_type]):
        return JsonResponse({'error': 'Missing required fields'}, status=400)

    prompt = f"""
    You are a travel assistant AI. Generate a detailed day-by-day itinerary for a {travel_type} People trip from {source} to {destination} 
    from {start_date} to {end_date}, with a budget of {budget} {currency}. Include activities, places to visit, and estimated daily cost.
    """

    try:
        # 🔐 Get the API key from environment
        api_key = settings.OPENROUTER_API_KEY
        if not api_key:
            return JsonResponse({'error': 'OpenRouter API key not set in environment'}, status=500)

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Referer": "https://tourgeniephase1-backend.onrender.com",  # Update if needed
            "Content-Type": "application/json"
        }

        body = {
            "model": "mistralai/mixtral-8x7b-instruct",
            "messages": [{"role": "user", "content": prompt}],
        }

        # 🔁 Make the request
        response = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=body,
            timeout=30.0
        )

        # 🌐 Debug response (if needed)
        print("OpenRouter response status:", response.status_code)
        print("OpenRouter response body:", response.text)

        response.raise_for_status()  # Will raise if response is not 2xx
        content = response.json()
        itinerary = content["choices"][0]["message"]["content"]

        return JsonResponse({"itinerary": itinerary})

    except Exception as e:
        # Print full traceback in logs
        traceback.print_exc()
        return JsonResponse({'error': str(e)}, status=500)

