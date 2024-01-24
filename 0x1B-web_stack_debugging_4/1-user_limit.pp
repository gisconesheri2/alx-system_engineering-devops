# remove limits for file acess
exec { '/usr/bin/env sed -i "s/holberton/prego/" /etc/security/limits.conf': }
