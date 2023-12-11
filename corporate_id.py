import requests



def get_c_ids():
    """
    Queries GraphQL for corporates in all cities from pages 1-27
    :return: a list of corporate ids
    """
    headers = {
        # 'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Connection': 'keep-alive',
        'DNT': '1',
        'Origin': 'https://ranking.glassdollar.com',
    }

    c_ids = []

    json_data_template = {
        'query': 'query {\n  corporates(\n    filters: {\n      hq_city: [\n      "Cyprus",\n      "Turkey",\n      "Switzerland",\n      "Italy",\n      "Hungary",\n      "China",\n      "Russia",\n      "Luxembourg",\n      "Czech Republic",\n      "Norway",\n      "Sweden",\n      "United Kingdom",\n      "Netherlands",\n      "Romania",\n      "Austria",\n      "Ireland",\n      "Germany",\n      "Singapore",\n      "South Korea",\n      "Portugal",\n      "Finland",\n      "Ukraine",\n      "Bulgaria",\n      "Spain",\n      "Liechtenstein",\n      "India",\n      "Belgium",\n      "France",\n      "Slovakia",\n      "Israel",\n      "Poland",\n      "Japan",\n      "Denmark",\n      "United States"\n    ],\n      industry: []\n    },\n    page: 1,\n  ) {\n    rows {\n      id\n    }\n    count\n  }\n}',
    }

    for page in range(1, 28):
        json_data = json_data_template.copy()
        json_data['query'] = json_data['query'].replace('page: 1', f'page: {page}')

        response = requests.post('https://ranking.glassdollar.com/graphql', headers=headers, json=json_data)
        for row in response.json()["data"]["corporates"]["rows"]:
            c_ids.append(row["id"])


    return c_ids








