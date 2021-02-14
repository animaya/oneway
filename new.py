line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

name, *fields, homedir, path = line.split(":")

a = 6

print(fields)

print(homedir)

print(name)
