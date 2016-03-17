DOMAIN = {
    'maps': {
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'title',
        },
        'schema': {
            'title': {
                'type':'string'
            },
            'routes': {
                'type':'list',
                'schema': {
                    'type':'dict',
                    'schema': {
                        'origin': {'type':'string'},
                        'destiny': {'type':'string'},
                        'distance': {'type':'float'}
                    }
                }
            }
        }
    }

}

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'logistic'

RESOURCE_METHODS = ['GET', 'POST']
XML = False
