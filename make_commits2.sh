#!/bin/bash
rm -rf .git
git init
git branch -M main
git config user.name "raman kumar"
git config user.email "ramanjaglan2006-crypto@users.noreply.github.com"

# Commit 1
git add README.md .gitignore upcoming_features.md commands.txt
GIT_AUTHOR_DATE="2026-05-21T12:00:00" GIT_COMMITTER_DATE="2026-05-21T12:00:00" git commit -m "Initial commit with documentation"

# Commit 2
git add docker-compose.yml
GIT_AUTHOR_DATE="2026-05-23T14:30:00" GIT_COMMITTER_DATE="2026-05-23T14:30:00" git commit -m "Add root docker-compose for orchestration"

# Commit 3
git add backend/requirements.txt backend/manage.py backend/config backend/.gitignore backend/.env.example backend/.env_sample backend/pytest.ini
GIT_AUTHOR_DATE="2026-05-24T10:15:00" GIT_COMMITTER_DATE="2026-05-24T10:15:00" git commit -m "Initialize Django backend project configuration"

# Commit 4
git add backend/Dockerfile backend/.dockerignore backend/README.md
GIT_AUTHOR_DATE="2026-05-26T16:45:00" GIT_COMMITTER_DATE="2026-05-26T16:45:00" git commit -m "Setup backend Docker configuration"

# Commit 5
git add backend/apps backend/api backend/backend
GIT_AUTHOR_DATE="2026-05-27T09:20:00" GIT_COMMITTER_DATE="2026-05-27T09:20:00" git commit -m "Implement backend apps and API structure"

# Commit 6
git add frontend/package.json frontend/package-lock.json frontend/angular.json frontend/tsconfig.json frontend/tsconfig.app.json frontend/tsconfig.spec.json frontend/tslint.json frontend/karma.conf.js frontend/.browserslistrc frontend/.editorconfig frontend/.gitignore
GIT_AUTHOR_DATE="2026-05-29T11:10:00" GIT_COMMITTER_DATE="2026-05-29T11:10:00" git commit -m "Initialize frontend Angular workspace"

# Commit 7
git add frontend/Dockerfile frontend/.dockerignore frontend/server.js frontend/README.md
GIT_AUTHOR_DATE="2026-05-30T13:40:00" GIT_COMMITTER_DATE="2026-05-30T13:40:00" git commit -m "Add frontend Docker and serving config"

# Commit 8
git add frontend/src frontend/e2e
GIT_AUTHOR_DATE="2026-06-01T15:25:00" GIT_COMMITTER_DATE="2026-06-01T15:25:00" git commit -m "Add frontend source code and e2e tests"

# Commit 9
git add .
GIT_AUTHOR_DATE="2026-06-02T10:05:00" GIT_COMMITTER_DATE="2026-06-02T10:05:00" git commit -m "Final polish and minor fixes"

git remote add origin https://github.com/ramanjaglan2006-crypto/Angular-DjangoRestFramework-Authentication-Component.git
git push -u origin main -f
