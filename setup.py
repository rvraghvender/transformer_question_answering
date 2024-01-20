import setuptools

with open("README.md", "r", encoding='utf-8') as file_object:
    long_description = file_object.read()


__version__ = '0.0.0'
REPO_NAME = 'transformer_question_answering'
AUTHOR_USER_NAME = 'rvraghvender'
AUTHOR_EMAIL = 'rvraghvender@gmail.com'
SRC_REPO = 'transformer_question_answering'
DESCRIPTION = 'Transformer model for question answering'


setuptools.setup(
    name=REPO_NAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}',
    project_urls={
        'Bug Tracker': f'https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues',
    },
    package_dir={'':'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)