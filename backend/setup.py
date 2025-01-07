from setuptools import setup, find_packages


def read_requirements(file_name):
    with open(file_name, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]


setup(
    name="parks_api",
    version="1.0.0",
    description="Flask API for finding parks",
    author_email="david.lockley@hitachigymnasiet.se",
    packages=find_packages(),
    include_package_data=True,  # To include static files like ParkCache.json
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": [
            "park-api=app.ParkApi:run_gunicorn",
        ],
    },
)
