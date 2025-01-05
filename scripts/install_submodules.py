import sys
import os
import subprocess
import configparser


def clone_and_initialize_submodules(build_dir):
    print("Starting submodule initialization...")

    gitmodules_path = os.path.join(build_dir, ".gitmodules")
    if not os.path.exists(gitmodules_path):
        print("No .gitmodules file found. Skipping submodule initialization.")
        return

    config = configparser.ConfigParser()
    config.read(gitmodules_path)

    auth_key = os.getenv("GITHUB_AUTH_KEY")

    for section in config.sections():
        if not section.startswith("submodule"):
            continue

        path = config.get(section, "path")
        url = config.get(section, "url")

        if auth_key:
            url_parts = url.split("://")
            if len(url_parts) == 2:
                url = f"{url_parts[0]}://{auth_key}@{url_parts[1]}"
                print(f"Modified URL for submodule '{path}': {url}")

        build_path = os.path.join(build_dir, path)
        print(f"Cloning submodule '{path}' from '{url}' into '{build_path}'...")
        try:
            subprocess.run(
                ["git", "clone", "--single-branch", url, build_path],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
        except subprocess.CalledProcessError as e:
            print(f"Error cloning submodule '{path}': {e.stderr.decode().strip()}")
            continue

        git_dir = os.path.join(build_path, ".git")
        if os.path.exists(git_dir):
            print(f"Removing .git folder from '{build_path}'...")
            subprocess.run(["rm", "-rf", git_dir], check=True)

    print("Submodule initialization complete.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Error: Missing required argument <build_dir>.")
        sys.exit(1)

    build_directory = sys.argv[1]
    clone_and_initialize_submodules(build_directory)
