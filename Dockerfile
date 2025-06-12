#The base image we are building on top of
FROM python:3.10-slim

#The working directory we are building into
WORKDIR /usr/src/app

#Copy all files from outside the container, into the container
COPY . .

#Install the Python/fastapi dependencies
RUN pip install --no-cache-dir -r requirements.txt

#Expo port 8000 to make the application accesible
EXPOSE 8000

#Define the command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

