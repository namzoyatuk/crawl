from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from corporate_id import get_c_ids
from tasks import corporate_info
from celery import group



app = FastAPI(openapi_url='/api/v1/crawler/openapi.json', docs_url='/api/v1/crawler/docs')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get('/crawl', status_code=202)
async def crawl_companies():
    corporate_ids = get_c_ids()

    tasks = group([corporate_info.s(c_id) for c_id in corporate_ids])

    result = tasks.apply_async()

    results = result.join()

    print(len(results))
    print(results[11])
    return {'crawled_companies': results}
