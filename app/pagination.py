from rest_framework.pagination import  LimitOffsetPagination

class InfiniteLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
