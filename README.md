# Tobi-v3

A Python packet interceptor that use a TUN interface

Get started with:

```
cd Tobi-v3/
./createTUNInterface
python3 Tobi.py
```

TODO:
- Add threading to analyse packets (in the Model class)
- Stop/Continue packet capture (only in the view, the traffic still needs to pass)
- Block/Allow packets
- Double click and open a packet with all the details (parse HTTP/RawData protocols)
