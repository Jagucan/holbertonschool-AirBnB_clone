#!/usr/bin/python3
""" Init Module """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
