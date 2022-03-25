FROM wawsinoss/pyodbcpython3.7


# install applicaiont
EXPOSE 8080

WORKDIR /home/app
COPY *.py /home/app/
COPY best_gbr.pickle /home/app
COPY requirements.txt /home/app

RUN pip install --upgrade pip
RUN pip install scipy
RUN pip install pyodbc
RUN pip install -r requirements.txt


CMD ["python","./server.py"]


