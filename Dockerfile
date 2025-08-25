# Use an official Python runtime as a parent image
FROM python:3.13.7-slim

# Set the working directory in the container
WORKDIR /app

# Copy app code
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy Streamlit config
RUN mkdir -p /root/.streamlit
COPY config.toml /root/.streamlit/config.toml

# Expose Streamlit port
EXPOSE 8501

# Run app
CMD ["streamlit", "run", "streamlit_app.py"]