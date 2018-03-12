FROM postgres

# run create.sql on init
# by adding a SQL file to the "docker-entrypoint-initdb.d" directory in the container, which will execute on init
ADD create.sql /docker-entrypoint-initdb.d