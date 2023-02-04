FROM python:3.7.1
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
# RUN git clone https://github.com/ultralytics/yolov5
ENV PYTHONPATH "${PYTHONPATH}:/apps"
COPY . .
EXPOSE 5000
CMD ["python", "api_flask.py"]
