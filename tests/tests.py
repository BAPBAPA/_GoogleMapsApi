from src.sources import *


class Tests:

    place_id = None

    @classmethod
    def test_place_creating(cls, api_instance):
        """Creating a place on the map and getting its 'id'"""
        response = api_instance.post()

        json = response.json()

        cls.place_id = json['place_id']

        assert response.status_code == 200, "Status code isn't equal to expected"

    @classmethod
    def test_place_is_created(cls, api_instance):
        """Checking that a place on the map has been created"""
        response = api_instance.get(cls.place_id)

        assert response.status_code == 200

    @classmethod
    def test_place_updating(cls, api_instance):
        """Updating location data"""
        response = api_instance.put(cls.place_id)

        assert response.status_code == 200
        assert response.text == PUT_200_MESSAGE

    @classmethod
    def test_place_is_updated(cls, api_instance, json_comparison):
        """Checking that the place's data has been successfully updated"""
        response = api_instance.get(cls.place_id)

        assert response.status_code == 200
        assert json_comparison(response.json())

    @classmethod
    def test_place_deleting(cls, api_instance):
        """Deleting a place on the map"""
        response = api_instance.delete(cls.place_id)

        assert response.status_code == 200
        assert response.text == DELETE_200_MESSAGE

    @classmethod
    def test_place_is_deleted(cls, api_instance):
        """Checking that place has been successfully deleted"""
        response = api_instance.get(cls.place_id)

        assert response.status_code == 404
        assert response.text == GET_404_MESSAGE
