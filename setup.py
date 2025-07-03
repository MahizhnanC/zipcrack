from setuptools import setup

setup(
    name="zipcrack",
    version="0.1",
    py_modules=["main"],  # using main.py directly
    install_requires=["tqdm"],
    entry_points={
        "console_scripts": [
            "zipcrack=main:main",
        ],
    },
    author="Mahizhnan",
    description="Brute-force numeric ZIP passwords (default: 9-digit)",
    keywords=["zip", "bruteforce", "ctf", "password", "cracker"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
