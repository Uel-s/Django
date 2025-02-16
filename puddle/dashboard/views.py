from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from item.models import Item
import logging

logger = logging.getLogger(__name__)

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)
    logger.debug(f"Fetched {len(items)} items for user {request.user.username}")
    return render(request, 'dashboard/index.html', {
        'items': items,
        'username': request.user.username
    })
