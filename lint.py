#!/usr/bin/env python3
import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
WORKING_PROJECT_DIR = os.path.join(BASE_DIR, "working_project")
TARGET_DIR = os.getcwd()

ESLINT_PATH = "./node_modules/.bin/eslint"
ESLINT_CONFIG_PATH = os.path.join(BASE_DIR, ".eslintrc.json")

if __name__ == "__main__":
    # Set up run args
    run_args = [
        ESLINT_PATH,
        "--ext", ".js,.ts,.jsx,.tsx,.vue",
        "--config", ESLINT_CONFIG_PATH
    ]
    if len(sys.argv) > 1 and sys.argv[1].lower().strip() == "fix":
        run_args.append("--fix")
    run_args.append(WORKING_PROJECT_DIR)

    # Symlink the target dir
    if os.path.islink(WORKING_PROJECT_DIR):
        os.unlink(WORKING_PROJECT_DIR)
    os.symlink(TARGET_DIR, WORKING_PROJECT_DIR)

    res = subprocess.run(run_args, cwd=BASE_DIR)

    # Remove the symlink
    os.unlink(WORKING_PROJECT_DIR)

    if res.returncode != 0:
        sys.exit(res.returncode)
