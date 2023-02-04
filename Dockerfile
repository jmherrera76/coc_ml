FROM nvcr.io/nvidia/pytorch:22.12-py3
RUN rm -rf /opt/pytorch  # remove 1.2GB dir
WORKDIR /app
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
RUN git clone https://github.com/ultralytics/yolov5
ENV PYTHONPATH "${PYTHONPATH}:/apps"
COPY . .
RUN prepare_yolo.sh

CMD ["python", "api_flask.py"]
