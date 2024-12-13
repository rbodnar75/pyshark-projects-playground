capture.set_debug()
   capture.apply_on_packets(lambda pkt: print(pkt), timeout=5, packet_count=10, bpf_filter='port 80')