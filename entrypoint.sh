#!/bin/bash

poetry run uvicorn backend.main:app --host 0.0.0.0
