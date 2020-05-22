FROM python:3.7-slim
EXPOSE 8510
RUN pip install numpy pandas matplotlib folium urllib3 requests python-dateutil
COPY . /usr/local/share/
WORKDIR /usr/local/share/
#ENTRYPOINT ["tail", "-f", "/dev/null"]
CMD ["python", "ThreadedServer.py"]
