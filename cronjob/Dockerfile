FROM python:3.9-slim

RUN pip install pymongo pandas openpyxl

COPY backup_to_excel.py /usr/src/app/backup_to_excel.py

WORKDIR /usr/src/app

CMD ["python", "backup_to_excel.py"]
