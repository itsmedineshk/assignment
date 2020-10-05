from ..models import Category, MovieCategoryAssociation


def filter_movies(query_params, queryset):
    if "category" in query_params:
        try:
            categories = Category.objects.filter(name__in=query_params["category"].split(","))
            movie_uuids = [association.movie.uuid for association in
                           MovieCategoryAssociation.objects.filter(category__in=categories)]
            queryset = queryset.filter(uuid__in=movie_uuids)
        except:
            pass

    if "from-rating" in query_params:
        try:
            val = query_params["from-rating"]
            queryset = queryset.filter(rating__gte=float(val))
        except:
            pass
    if "to-rating" in query_params:
        try:
            val = query_params["to-rating"]
            queryset = queryset.filter(rating__lte=float(val))
        except:
            pass

    if "from-year" in query_params:
        try:
            val = query_params["from-year"]
            queryset = queryset.filter(pub_date__gte=float(val))
        except:
            pass
    if "to-year" in query_params:
        try:
            val = query_params["to-year"]
            queryset = queryset.filter(pub_date__lte=float(val))
        except:
            pass

    return queryset


def order_movies(query_params, queryset):
    if "orderBy" in query_params:
        if query_params["orderBy"] in ['name', 'pub_date', 'duration', 'ranking']:
            order_column = query_params["orderBy"]
            sort_order = "sortOrder" in query_params and str(query_params["sortOrder"]) != "desc"
            sort_flag = "" if sort_order else "-"
            queryset = queryset.order_by(sort_flag + order_column)
    return queryset


def filter_rentals(query_params, queryset):
    if "only-active" in query_params:
        queryset = queryset.filter(return_date=None)
    return queryset
