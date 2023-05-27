from src.sources import PUT_BODY


def json_parse(json):

    return json['address'] == PUT_BODY['address']
