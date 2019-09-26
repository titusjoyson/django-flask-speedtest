from django.urls import path
from .views import (
    simple_list_view,
    paginated_list_view,
    aggregation_list_view,
    count_list_view,
    select_list_view,
    create_view,
    update_view,
    algo_view
)


urlpatterns = [
    path('simple/', simple_list_view),
    path('paginated/', paginated_list_view),
    path('aggregation/', aggregation_list_view),
    path('select/', select_list_view),
    path('count/', count_list_view),
    path('create/', create_view),
    path('update/', update_view),
    path('algo/', algo_view),
]