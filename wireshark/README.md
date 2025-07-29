# Wireshark Captures

This folder contains packet captures and notes for network traffic analysis.

## example_capture.pcapng

This is a basic capture taken while accessing [neverssl.com](http://neverssl.com), which uses unencrypted HTTP.

**Things you can explore in this capture:**
- TCP handshake (SYN, SYN-ACK, ACK)
- HTTP GET request to `/`
- HTTP 200 OK response
- Visible headers and response content (no encryption)
- Source and destination IPs

This capture is useful for basic protocol analysis and understanding how unencrypted web traffic looks in a packet sniffer.

## dns_query_capture.pcapng

A short capture showing DNS resolution for icanhazip.com using UDP port 53.

Useful to:
- Observe the DNS query/response handshake
- Understand how names are resolved into IPs
- Practice DNS filtering in Wireshark (use `dns` filter)


## dnd_filtered_capture.pcapng

Capture filtered on 'dns' with columns added for source and destination ports
