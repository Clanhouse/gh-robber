from email import message
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
    scraping = GH_API_handling.Scraping()
    scraping.add_user_to_database(user)
    return jsonify(message="Request to scrape user " + user + " sent")


@admin_api.route("/scraping/GH-scrape-repo/<repo>", methods=["GET", "POST"])
def scrape_repo_from_GH(repo):
    scraping = GH_API_handling.Scraping()
    scraping.add_repo_to_database(repo)
    return jsonify(message="Request to scrape repo " + repo + " sent")


@admin_api.route("/scraping/GH-update-user/<user>", methods=["GET", "POST"])
def update_GH_user(user):
    scraping = GH_API_handling.Scraping()
    scraping.update_user_info(user)
    return jsonify(message="Request to update user " + user + " sent")


@admin_api.route("/scraping/GH-update-repo/<repo>", methods=["GET", "POST"])
def update_GH_repo(repo):
    scraping = GH_API_handling.Scraping()
    scraping.update_repo(repo)
    return jsonify(message="Request to update repo " + repo + " sent")


@admin_api.route("/scraping/GH-status/")
def GH_scraping_status():
    return jsonify(
        running=GH_API_handling.Scraping.gh_scraping_running,
        last_scraped_repo=GH_API_handling.Scraping.last_scraped_repo_name,
        last_scraped_repo_timestamp=GH_API_handling.Scraping.last_scraped_repo_timestamp,
        last_scraped_user=GH_API_handling.Scraping.last_scraped_user_name,
        last_scraped_user_timestamp=GH_API_handling.Scraping.last_scraped_user_timestamp,
    )


@admin_api.route("/scraping/GH-init-scraping/", methods=["GET", "POST"])
def init_scraping_GH():
    scraping = GH_API_handling.Scraping()
    scraping.auto_scraping_GH()
    # return {"status": "Scraping started"}  # why is it unreachable


@admin_api.route("/scraping/GH-spause-scraping/", methods=["GET", "POST"])
def pause_scraping_GH():
    GH_API_handling.Scraping.gh_scraping_running = False
    return jsonify(message="Scraping is paused")


@admin_api.route("/scraping/GH-resume-scraping/", methods=["GET", "POST"])
def resume_scraping_GH():
    GH_API_handling.Scraping.gh_scraping_running = True
    return jsonify(message="Scraping is resumed")
