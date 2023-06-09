FROM python:3.10-buster

# Install nginx
RUN apt-get update && apt-get install nginx vim sqlite3 -y --no-install-recommends
COPY nginx.conf /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Copy source and install dependencies
RUN mkdir -p /opt/app/books
RUN mkdir -p /opt/app/pip_cache
COPY requirements.txt start-server.sh /opt/app/
RUN chmod +x /opt/app/start-server.sh
COPY  /opt/app/books/
WORKDIR /opt/app
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
RUN rm /opt/app/books/db.sqlite3
RUN python3 /opt/app/books/manage.py makemigrations
RUN python3 /opt/app/books/manage.py migrate
RUN chown -R www-data:www-data /opt/app

# Just in case there are temporary files...
RUN find /opt/app/books -name "*~" -exec /bin/rm {} \;
RUN find /opt/app/books -name "*.swp" -exec /bin/rm {} \;

# Start server
EXPOSE 8020
STOPSIGNAL SIGTERM
CMD ["/opt/app/start-server.sh"]
