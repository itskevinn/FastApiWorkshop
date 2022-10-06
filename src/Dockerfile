
FROM python:3.9

#
WORKDIR /code

#
COPY ./requirements.txt /code/requirements.txt

#
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#
COPY ./ /code/src

#
CMD ["uvicorn", "__init__:init_app", "--host", "0.0.0.0", "--port", "80"]