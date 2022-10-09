from django.db import connections

def SqlPrintingMiddleware(get_response):
    def middleware(request):
        response = get_response(request)
        for con in connections: 
            print (f'{con} : {connections[con].queries}')
        return response
    return middleware