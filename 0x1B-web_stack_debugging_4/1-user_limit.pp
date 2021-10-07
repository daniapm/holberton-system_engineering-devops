# Change the OS configuration so that it is
# possible to login with the holberton user and open a file without any error message.
exec { '/usr/bin/env sed -i \'s/nofile 4/nofile 10000/\' /etc/security/limits.conf': }
