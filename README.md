# Pax's Portfolio (Backend API)

<p align="center">
    <a href="https://app.netlify.com/sites/laughing-brattain-d0abbd/deploys">
        <img src="https://api.netlify.com/api/v1/badges/0ee12cf8-5b79-4a11-ae30-fd74576e16fa/deploy-status" alt="Netlify Status" />
    </a>
    <a href="https://app.buddy.works/paxmargret/portfolio-api/pipelines/pipeline/318477">
        <img src="https://app.buddy.works/paxmargret/portfolio-api/pipelines/pipeline/318477/badge.svg?token=4b2a7bd16f0c58f0eaa34f27824a709c73c4ea73cce5810e7fc62916ba745d3f" alt="buddy pipeline" />
    </a>
</p>

<p align="center"><em>Over-engineering my portfolio for hands-on learning experience! Frontend deployed in Netlify; API deployed in AWS EC2 instance; Set up CI/CD using <a href="https://buddy.works/">buddy.works</a></em></p>

## Project setup

1. Install [poetry](https://python-poetry.org/docs/#installation)
2. Inside the `backend` folder:
    - run `poetry shell` and then `poetry install`

### Serve the API Locally

```
uvicorn portfolio_api.main:app --reload
```

### Run Tests

```
pytest
```

### Deploy to Production

```
git checkout main
git push origin
```

## Roadmap

1) API for administration pages
    - Authentication and authorization
    - CRUD operations (save data to a PostgreSQL database)
2) (Celery) task to regularly pull GitHub data