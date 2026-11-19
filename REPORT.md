# Lab 10 Report – Jenkins CI/CD Pipeline
**Name:** Firyal Al Sharabati

## Changes made to the Jenkinsfile
1. **Coverage stage (new):** runs the tests with `coverage.py`, prints a coverage report, and makes an HTML report (`htmlcov/`), which Jenkins saves as a build artifact.
2. **Security Scan stage (new):** runs `bandit` on `app.py` and `deploy.py` to check for security problems.
3. **Deploy stage (changed):** now runs `deploy.py`, a simple local deployment. It copies the app into a `deploy/` folder and runs it.
4. **Windows support:** each stage uses `bat` on Windows and `sh` on Linux (`isUnix()`), because the original `source venv/bin/activate` only works on Linux.
5. **requirements.txt:** added `pytest`, `coverage` and `bandit`.
6. **app.py:** `greet()` now returns `"Hello, {name} from Firyal AlSharabati!"` so the unit test passes.

## Pipeline stages
Setup → Lint → Test → Coverage → Security Scan → Deploy

## Build output
All stages passed. Screenshot of the successful build:

![Jenkins build](build_success.png)

Key results:
- Test: 1 passed
- Coverage: 100% for app.py
- Bandit: No issues identified
- Deploy: "Deployment successful!"
