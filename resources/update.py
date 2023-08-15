from flask.views import MethodView
from flask_smorest import Blueprint, abort
from crawler import collect_new_data

blp = Blueprint("update", __name__, description="Updating the database")

@blp.route("/update")
class Update(MethodView):
    def post(self):
        try:
            collect_new_data()
            return {"message": "Update completed successfully!"}
        except:
            abort(500, message="An error occurred while updating the database")