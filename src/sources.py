BASE_URL = 'https://rahulshettyacademy.com'

POST_RESOURCE = '/maps/api/place/add/json'
GET_SOURCE = '/maps/api/place/get/json'
PUT_SOURCE = '/maps/api/place/update/json'
DELETE_SOURCE = '/maps/api/place/delete/json'

REQUIRED_PARAMETER = '?key=qaclick123'

POST_BODY = {
    "location": {
        "lat": -38.383494,
        "lng": 33.427362},
    "accuracy": 50,
    "name": "Front_line house",
    "phone_number": "(+91) 983 893 3937",
    "address": "29, side layout, cohen 09",
    "types": [
        "shoe park",
        "shop"],
    "website": "http://google.com",
    "language": "French-IN"}

PUT_BODY = {"address": "100 Lenina street, RU",
            "key": "qaclick123"}

GET_404_MESSAGE = '''{"msg":"Get operation failed, looks like place_id  doesn't exists"}'''

PUT_200_MESSAGE = '''{"msg":"Address successfully updated"}'''
PUT_404_MESSAGE = '''{"msg":"Update address operation failed, looks like the data doesn't exists"}'''

DELETE_200_MESSAGE = '''{"status":"OK"}'''
DELETE_404_MESSAGE = '''{"msg":"Delete operation failed, looks like the data doesn't exists"}'''
