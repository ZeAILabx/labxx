# LABX

Flask and Supabase backend with a React and Vite frontend.

## Project structure

```text
backend/
  main.py                 # Flask application factory
  run.py                  # Existing server entry point
  database/database.py    # Supabase client setup
  src/
    config.py
    routes/routes.py      # Blueprint registration
    controllers/          # Existing HTTP handlers and route decorators
    service/              # Existing business-rule engines
    middleware/           # Authentication and role checks
    repository/
    models/
    validators/
    utils/
  tests/
frontend/
  src/
    app/App.jsx           # Application composition and routing
    features/             # Pages, components, and hooks grouped by feature
    components/layout/    # Navigation and layout components
    components/common/    # Shared components
    hooks/                # Shared hooks
    services/api/client.js
    assets/images/
    styles/
    main.jsx
  tests/
supabase/                 # Existing database scripts
docs/
```

This is a file-organization change. Existing API routes, response formats,
business logic, and database access remain unchanged. The backend's repository,
models, validators, and utils packages reserve the sample's folder structure;
existing handler logic has not been rewritten into new layers.

## Run locally

From `backend`, install `requirements.txt`, configure `backend/.env` with
`SUPABASE_URL`, `SUPABASE_SERVICE_ROLE_KEY`, and `SECRET_KEY`, then run:

```sh
python run.py
```

From `frontend`:

```sh
npm ci
npm run dev
```

## Checks

From `backend`, run `python -m pytest -q`. From `frontend`, run
`npm run build` and `npm run lint`.
