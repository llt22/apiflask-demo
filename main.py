from apiflask import APIFlask, Schema, input, output
from apiflask.fields import String, Integer, Field

app = APIFlask(__name__)


class BaseResponseSchema(Schema):
    data = Field()
    message = String()
    code = Integer()


class PetOutSchema(Schema):
    pass


app.config['BASE_RESPONSE_SCHEMA'] = BaseResponseSchema


@app.get('/pets/<int:pet_id>')
@output(PetOutSchema)
def get_pet(pet_id):
    return {
        'data': None,
        'message': 'Get pet successfully.',
        'code': '1000'
    }


if __name__ == '__main__':
    app.run()
