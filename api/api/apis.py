from django.http import JsonResponse, HttpResponseBadRequest
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Weather
from django.db.models import Avg
from rest_framework.decorators import api_view, renderer_classes
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
import logging

@api_view(['GET'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def get_weather_api(request):
    """
                   To use this api, you need to pass Location, year, and maybe page to it.
                   Otherwise, it will show you all the data.

                    ---

                    """

    logger = set_logger()
    location = request.GET.get('location')
    year = request.GET.get('year')
    page_number = request.GET.get('page')
    logger.info('get_weather_api with params: %s , %s, %s', location, year, page_number)
    weather_list = Weather.objects.all()
    if location:
        weather_list = weather_list.filter(Location=location)
    if year:
        weather_list = weather_list.filter(DateStamp__year=year)
    weather_list = weather_list.order_by('DateStamp')
    paginator = Paginator(weather_list, 10)

    try:
        # get the page from the paginator
        page = paginator.page(page_number)
    except PageNotAnInteger:
        # if page number is not an integer, default to the first page
        page = paginator.page(1)
    except EmptyPage:
        # if page number is out of range, return an empty page
        page = paginator.page(paginator.num_pages)

        # serialize the data into a JSON object
    serialized_data = list(page.object_list.values())

    # create a dictionary with the serialized data and pagination information
    response_data = {
        'data': serialized_data,
        'has_next': page.has_next(),
        'has_previous': page.has_previous(),
        'current_page': page_number,
        'total_pages': paginator.num_pages
    }

    # return a JSON response with the response data
    return JsonResponse(response_data)


@api_view(['GET'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def get_stats_min_avg(request):
    """
                   To use this api, you need to pass Location, year, and maybe page to it.

                    ---

    """
    logger = set_logger()
    location = request.GET.get('location')
    year = request.GET.get('year')
    logger.info('get_stats_min_avg with params: %s , %s', location, year)
    if location and year:
        # Filter queryset based on location and year
        data = Weather.objects.filter(Location=location, DateStamp__year=year).aggregate(Avg('MinTemp'))
        avg_mintemp = data['MinTemp__avg']
        response_data = {'Result (Average of Min Temperature)': avg_mintemp}
        return JsonResponse(response_data)
    else:
        logger.error('invalid input: %s , %s', location, year)
        return HttpResponseBadRequest('Please provide both location and year parameters.')


@api_view(['GET'])
@renderer_classes([OpenAPIRenderer, SwaggerUIRenderer])
def get_stats_max_avg(request):
    """
                       To use this api, you need to pass Location, year, and maybe page to it.

                        ---

                        """
    logger = set_logger()
    location = request.GET.get('location')
    year = request.GET.get('year')
    logger.info('get_stats_min_avg with params: %s , %s', location, year)
    if location and year:
        # Filter queryset based on location and year
        data = Weather.objects.filter(Location=location, DateStamp__year=year).aggregate(Avg('MaxTemp'))
        avg_maxtemp = data['MaxTemp__avg']
        response_data = {'Result (Average of Max Temperature)': avg_maxtemp}
        return JsonResponse(response_data)
    else:
        logger.error('invalid input: %s , %s', location, year)
        return HttpResponseBadRequest('Please provide both location and year parameters.')


def set_logger():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('API-Logger')

    return logger
