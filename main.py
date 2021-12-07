from apiflask import APIFlask

from apiflask import HTTPError

app = APIFlask(__name__)


class PetNotFound(HTTPError):
    status_code = 404
    message = 'This pet is missing.',


@app.get('/pets/<int:pet_id>')
def get_pet(pet_id):
    raise HTTPError(404, 'This pet is missing.')
    # raise PetNotFound


if __name__ == '__main__':
    app.run(
        debug=True,
        port=80
    )
