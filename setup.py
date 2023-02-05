#!/usr/bin/env python

from distutils.core import setup

setup(
    name="whisper-app",
    version="1.0",
    description="CAP-IT - Collection Aware Personalitation on Image Text Modalities",
    author="Antreas Antoniou",
    author_email="iam@antreas.io",
    packages=[
        "capit",
        "capit.core",
        "capit.core.data",
        "capit.core.models",
        "capit.core.utils",
    ],
)
