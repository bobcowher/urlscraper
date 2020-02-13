FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader wordnet
RUN python -m nltk.downloader stopwords
ENTRYPOINT ["python"]
CMD ["app.py"]