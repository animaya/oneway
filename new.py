line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

name, *fields, homedir, path = line.split(":")

print(fields)

print(homedir)