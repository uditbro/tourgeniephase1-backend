from datetime import datetime, timedelta

def generate_basic_itinerary(destination, start_date, end_date, budget, travel_type):
    days = (end_date - start_date).days + 1
    itinerary = []

    activity_map = {
        'solo': ['Explore local cafés', 'Visit a museum', 'Take a walking tour'],
        'family': ['Zoo visit', 'Theme park day', 'Family picnic'],
        'honeymoon': ['Sunset dinner', 'Spa & wellness', 'Private boat ride'],
        'friends': ['Bar hopping', 'Adventure park', 'Local food tour'],
        'group': ['City sightseeing', 'Cultural show', 'Beach activities'],
        'spiritual': ['Temple visit', 'Meditation session', 'Attend prayer rituals']
    }

    activities = activity_map.get(travel_type.lower(), ['Explore local sites'])

    for i in range(days):
        day = start_date + timedelta(days=i)
        plan = {
            'day': f'Day {i+1}',
            'date': day.strftime('%Y-%m-%d'),
            'activity': activities[i % len(activities)],
            'location': destination,
        }
        itinerary.append(plan)

    return itinerary
