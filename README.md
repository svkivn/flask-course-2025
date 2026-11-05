# Flask and SQLAlchemy: Code-First Database Deployments

This project follows a code-first approach: define schema changes in application code, track them as migrations, and apply them deliberately during deployment.

## Migration workflow

Use Flask-Migrate (built on Alembic) to create and apply versioned schema changes:

```bash
pip install Flask-Migrate
```

Initialize migration support in the Flask application:

```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

Create the migration repository once, then generate a migration after changing SQLAlchemy models:

```bash
flask db init
flask db migrate -m "Describe the schema change"
flask db upgrade
```

Review generated migration files before committing them. Autogeneration is a starting point; it may miss some changes or require manual adjustments. Commit migration files alongside the model changes.

## Deployment checklist

1. Back up the database and test migrations against a staging copy.
2. Configure the production database URL and credentials through environment variables or a secret manager.
3. Run `flask db upgrade` as a controlled deployment step, before routing traffic to code that depends on the new schema.
4. Make changes backward-compatible where possible: add new nullable fields or tables first, deploy compatible application code, then backfill or remove obsolete schema in a later release.
5. Verify the migration result and application health; have a tested recovery plan. Database downgrades are not always safe or lossless.

Avoid relying on `db.create_all()` for ongoing production schema changes. Versioned migrations provide a reviewable, repeatable history for development, staging, and production.
    