"""Simple local deployment: copy the app to 'deploy' and run it."""
import os
import shutil
import subprocess  # nosec B404
import sys

DEPLOY_DIR = "deploy"
FILES = ["app.py", "requirements.txt"]


def deploy():
    os.makedirs(DEPLOY_DIR, exist_ok=True)
    for f in FILES:
        shutil.copy(f, DEPLOY_DIR)
        print(f"Copied {f} -> {DEPLOY_DIR}/")
    result = subprocess.run(  # nosec B603
        [sys.executable, os.path.join(DEPLOY_DIR, "app.py")],
        capture_output=True, text=True, check=True,
    )
    print("Deployed app output:", result.stdout.strip())
    print("Deployment successful!")


if __name__ == "__main__":
    deploy()
