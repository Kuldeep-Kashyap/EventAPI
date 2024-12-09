from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from .models import Event, Ticket
from .serializers import EventSerializer, TicketSerializer, UserSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=201)
        return Response(serializer.errors, status=400)

class EventView(APIView):
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.role != 'Admin':
            return Response({"error": "Permission denied"}, status=403)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['POST'])
def purchase_ticket(request, id):
    try:
        event = Event.objects.get(id=id)
    except Event.DoesNotExist:
        return Response({"error": "Event not found"}, status=404)

    quantity = request.data.get('quantity', 0)
    if event.tickets_sold + quantity > event.total_tickets:
        return Response({"error": "Not enough tickets available"}, status=400)

    ticket = Ticket.objects.create(
        user=request.user, event=event, quantity=quantity
    )
    event.tickets_sold += quantity
    event.save()
    return Response(TicketSerializer(ticket).data, status=201)
