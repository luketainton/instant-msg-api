#!/usr/local/bin/python3

from dotenv import load_dotenv

from app.api import webapp


if __name__ == "__main__":
    import uvicorn
    load_dotenv()
    uvicorn.run(webapp, host="0.0.0.0", port=8000)

