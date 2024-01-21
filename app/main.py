#!/usr/local/bin/python3

from app.api import webapp


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(webapp, host="0.0.0.0", port=8000)

