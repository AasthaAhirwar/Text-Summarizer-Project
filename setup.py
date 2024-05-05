import setuptools

with open("README.md", "r", encoding= "utf-8") as f:
    log_description = f.read()

__version__ ="0.0.0"

REPO_NAME = "Text-Summarizer-Project"
AUTHOR_USER_NAME = "AasthaAhirwar"
SRC_REPO ="textSummarizer"
AUTHOR_EMAIL = "aasthaahirwar1008@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NPL app",
    Long_description=log_description,
    Long_description_content ="text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls ={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",

    },

    package_dir ={"":"scr"},
    packages=setuptools.find_packages(where="scr"),
)