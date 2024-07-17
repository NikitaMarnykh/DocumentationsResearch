from rest_framework import permissions

from rest_framework.viewsets import mixins, GenericViewSet

from .models import Quote
from .serializes import QuoteSerializer


# Представление API всех котировок или одной необходимой
class QuotesViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, GenericViewSet):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    permission_classes = (permissions.IsAuthenticated, )