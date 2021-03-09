#!/usr/bin/env python

from random import choice

long = 10
values = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

password = ""
password = password.join([choice(values) for i in range(long)])
print('tu pasword es:', password)