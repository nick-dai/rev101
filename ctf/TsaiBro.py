#!/usr/bin/env python3

items = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXY0123456789{}_'
flag = ''

with open('flag.txt', 'r') as f:
    # Skip the first line
    f.readline()
    payload = f.read().strip()
    payload = payload.split('發財')
    payload = [len(p) for p in payload][1:]
    for i in range(int(len(payload)/2)):
        for k in range(len(items)):
            if payload[2*i] == (k // 8 + 1) and payload[2*i+1] == (k % 8 + 1):
                flag += items[k]
                break

print(flag)