from flask_restplus import Namespace
from app.speedtest.views import  (
    SimpleList, 
    PaginatedList, 
    Aggregation, 
    Count,
    SelectList,
    Create,
    Update,
    Save,
    HeavyCodeList
)

api = Namespace('speedtest', description='speedtest related operations')
api.add_resource(SimpleList, '/simple')
api.add_resource(PaginatedList, '/paginated')
api.add_resource(Aggregation, '/aggregation')
api.add_resource(Count, '/count')
api.add_resource(SelectList, '/select')
api.add_resource(Create, '/create')
api.add_resource(Save, '/save')
api.add_resource(Update, '/update')
api.add_resource(HeavyCodeList, '/algo')
# /aggregation/