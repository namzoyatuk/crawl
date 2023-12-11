from celery import Celery
from celery.utils.log import get_task_logger
import requests


app = Celery('tasks', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

celery_log = get_task_logger(__name__)

@app.task(name='get_corporate_info')
def corporate_info(c_id):
    """
    The task to be processed via celery worker
    :param c_id: corporate_id retrieved from GraphQL
    :return: Crawled corporate information in JSON format
    """
    headers = {
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://ranking.glassdollar.com',
    }

    json_data = {
        'query': f'query {{\n  corporate(id: "{c_id}") {{\n    name\n    description\n    logo_url\n    website_url\n    linkedin_url\n    twitter_url\n    hq_city\n    hq_country\n    startup_partners_count\n    startup_partners {{\n      company_name\n      website\n      city\n      country\n      logo\n      theme_gd\n    }}\n    startup_themes\n  }}\n}}',
    }

    celery_log.info("Celery task completed")

    response = requests.post('https://ranking.glassdollar.com/graphql', headers=headers, json=json_data)


    return response.json()



