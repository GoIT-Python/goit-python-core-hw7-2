from setuptools import setup, find_namespace_packages

setup(
    name="my_clean_folder",
    version="1",
    description="Very useful Clean Your Folder code",
    url="https://github.com/GoIT-Python/goit-python-core-hw7-2",
    author="Volodymyr Kurov",
    author_email="vokur13@gmail.com",
    license="MIT",
    include_package_data=True,
    packages=find_namespace_packages(),
    install_requires=["transliterate"],
    entry_points={"console_scripts": ["clean-folder=my_clean_folder.my_clean:sort"]},
)
