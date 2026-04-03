from pathlib import Path

from setuptools import find_packages, setup

from maintenance_management import __version__ as version


def get_requirements():
    requirements_file = Path(__file__).parent / "requirements.txt"

    if not requirements_file.exists():
        return []

    return [
        line.strip()
        for line in requirements_file.read_text().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]


setup(
    name="maintenance_management",
    version=version,
    description="ERPNext custom app for maintenance breakdown tracking",
    author="Codex",
    author_email="support@example.com",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=get_requirements(),
)
