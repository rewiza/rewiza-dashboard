from django.conf import settings
import requests, json


def trigger_gitlab_job(job):
    get_url = "{}jobs?name={}".format(settings.GITLAB_PROJECT_NAME, job)
    headers = {'PRIVATE-TOKEN': settings.GITLAB_API_ACCESS_TOKEN}
    r = requests.get(get_url, headers=headers)
    job_id = r.json()[0]['id']
    post_url = "{}jobs/{}/play".format(settings.GITLAB_PROJECT_NAME, job_id)
    print(post_url)
    requests.post(post_url, headers=headers)
