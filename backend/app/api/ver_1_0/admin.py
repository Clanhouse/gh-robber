from backend.app.api.ver_1_0 import admin_api
from backend.app.models_helpers import create_fake_data, create_fake_info


@admin_api.route("/init-fake-data/")
def init_fake_data():
    create_fake_data()
    create_fake_info()
    return {"status": "Success"}
