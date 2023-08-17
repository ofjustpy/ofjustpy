import os
import tempfile
from pathlib import Path

import nox

locations = "src", "noxfile.py"


@nox.session(python=["3.11"])
def lint(session):
    args = session.posargs or locations
    session.install(
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


# noxfile.py
@nox.session(python=["3.11"])
def black(session):
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


# noxfile.py
@nox.session(python=["3.11"])
def reorder_imports(session):
    args = session.posargs or locations
    session.install("reorder-python-imports")
    # run reorder on each python file
    files = []
    for location in locations:
        p = Path(location)
        if p.is_file():
            files.append(p)
        elif p.is_dir():
            files.extend(p.rglob("*.py"))

    for file in files:
        session.run("reorder-python-imports", str(file))


@nox.session(python="3.11")
def safety(session):
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "bash",
            "-c",
            f"pipenv requirements >  {requirements.name}",
            external=True,
        )
        session.install("safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python="3.11")
def docs(session):
    # Install Sphinx and ghp-import
    session.install(
        "sphinx", "ghp-import", "git+https://github.com/bashtage/sphinx-material.git"
    )

    # Build the documentation
    os.chdir("docs")
    session.run("sphinx-build", "-b", "html", ".", "_build/html")

    # Push the documentation to the gh-pages branch
    session.run("ghp-import", "-n", "-p", "-f", "_build/html")


@nox.session(python="3.11")
def badges(session):
    # Install pytest, pytest-cov, flake8 and genbadge
    session.install("pytest", "pytest-cov", "flake8", "flake8-html", "genbadge[all]")

    session.env["PIPENV_VERBOSITY"] = "-1"
    with tempfile.NamedTemporaryFile(delete=False) as fp:
        print("THE FILE PATH NAME = ", fp.name)
        session.run(
            "pipenv",
            "run",
            "pip",
            "freeze",
            external=True,
            stdout=fp,
        )

    #
    # session.env["PIPENV_IGNORE_VIRTUALENVS"]=1

    # Install dependencies from the temporary requirements.txt
    session.install("-r", fp.name)

    # Install your package in editable mode
    session.run("pip", "install", "-e", ".")

    # Run pytest to generate the junit and html reports
    with session.chdir("tests"):
        session.run(
            "pytest",
            "--cov",
            "--junitxml=reports/junit/junit.xml",
            "--cov-report=xml:reports/coverage/coverage.xml",
            "--cov-report=html:reports/coverage/coverage.html",
        )

    # Run flake8 to generate the HTML report and statistics
    session.run(
        "flake8",
        "src/ofjustpy",
        "--exit-zero",
        "--format=pylint",
        # "--htmldir=./reports/flake8",
        "--statistics",
        "--output-file=reports/flake8/flake8stats.txt",
    )

    # Generate a badge for tests
    session.run(
        "genbadge", "tests", "-i", "reports/junit/junit.xml", "-o", "badge_tests.svg"
    )

    # Generate a badge for coverage
    session.run(
        "genbadge",
        "coverage",
        "-i",
        "reports/coverage/coverage.xml",
        "-o",
        "badge_coverage.svg",
    )

    # Generate a badge for flake8 based on the statistics text report
    session.run(
        "genbadge",
        "flake8",
        "-i",
        "reports/flake8/flake8stats.txt",
        "-o",
        "badge_flake8.svg",
    )


# @nox.session(python="3.11")
# def badges(session):
#     # Install pytest, pytest-cov, flake8 and genbadge
#     session.install("pytest", "pytest-cov", "flake8", "flake8-html", "ofjustpy-engine", "genbadge[all]")
#     #session.install("ofjustpy-engine")

#     # we need the dependencies
#     #session.install("pipenv")
#     # with tempfile.NamedTemporaryFile(delete=False) as fp:
#     #     print("THE FILE PATH NAME = ", fp.name)
#     #     session.run(
#     #         "pipenv",
#     #         "run",
#     #         "pip",
#     #         "freeze",
#     #         external=True,
#     #         stdout=fp,
#     #     )


#     # # Generate requirements.txt in a temporary file
#     # with tempfile.NamedTemporaryFile(delete=False) as fp:
#     #     session.run(
#     #         "pipenv",
#     #         "requirements",
#     #         external=True,
#     #         stdout=fp,
#     #     )

#     session.env["PIPENV_VERBOSITY"] = "-1"


#     # Install dependencies from the temporary requirements.txt
#     #session.install("-r", fp.name)

#     # Install your package in editable mode
#     #session.run("pip", "install", "ofjustpy-engine")
#     session.run("pip", "install", "-e", ".")

#     # Run pytest to generate the junit and html reports
#     session.run(
#         "pytest",
#         "--cov",
#         "--junitxml=reports/junit/junit.xml",
#         "--cov-report=xml:reports/coverage/coverage.xml",
#         "--cov-report=html:reports/coverage/coverage.html",
#     )

#     # Run flake8 to generate the HTML report and statistics
#     session.run(
#         "flake8",
#         "src/addict_tracking_changes",
#         "--exit-zero",
#         "--format=pylint",
#         # "--htmldir=./reports/flake8",
#         "--statistics",
#         "--output-file=reports/flake8/flake8stats.txt",
#     )

#     # Generate a badge for tests
#     session.run(
#         "genbadge", "tests", "-i", "reports/junit/junit.xml", "-o", "badge_tests.svg"
#     )

#     # Generate a badge for coverage
#     session.run(
#         "genbadge",
#         "coverage",
#         "-i",
#         "reports/coverage/coverage.xml",
#         "-o",
#         "badge_coverage.svg",
#     )

#     # Generate a badge for flake8 based on the statistics text report
#     session.run(
#         "genbadge",
#         "flake8",
#         "-i",
#         "reports/flake8/flake8stats.txt",
#         "-o",
#         "badge_flake8.svg",
#     )
