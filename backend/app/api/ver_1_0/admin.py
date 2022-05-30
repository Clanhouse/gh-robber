from flask import jsonify
import app.GH_API_handling as GH_API_handling
from app.api.ver_1_0 import admin_api
from app.models_helpers import create_fake_info


@admin_api.route("/init-fake-data/")
def init_fake_data():
    create_fake_info()
    return {"status": "Success"}


@admin_api.route("/scraping/GH-scrape-user/<user>", methods=["GET", "POST"])
def scrape_user_from_GH(user):
    # stop scraping
    GH_API_handling.add_user_to_database(user)
    # start scraping
    return jsonify(status="Request to scrape user " + user + " sent")


@admin_api.route("/scraping/GH-scrape-repo/<repo>", methods=["GET", "POST"])
def scrape_repo_from_GH(repo):
    # stop scraping
    GH_API_handling.add_user_to_database(repo)
    # start scraping
    return jsonify(status="Request to scrape repo " + repo + " sent")


@admin_api.route("/scraping/GHstatus/")
def GH_scraping_status():
    # add function to show scraping flag
    return jsonify(status=GH_API_handling.is_scraping_running())


@admin_api.route("/scraping/GHstartscraping/", methods=["GET", "POST"])
def start_scraping_GH():
    # set scraping flag True
    GH_API_handling.set_scraping_running_true()
    GH_API_handling.auto_scraping_GH()
    # return {"status": "Scraping started"}  # why is it unreachable
