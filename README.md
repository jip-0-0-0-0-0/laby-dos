# LabyMod Server API DoS PoC

## Overview
This repository provides a Proof of Concept (PoC) for testing potential Denial of Service (DoS) vulnerabilities in servers running the LabyMod Server API. By targeting the `laby:mod` plugin communication channel, the script demonstrates how rapid payload transmission can disrupt server functionality.

## Vulnerability Details
- **Affected Component**: `laby:mod` plugin channel.
- **Cause**: Lack of robust rate-limiting and payload validation in the LabyMod Server API.
- **Impact**:
  1. Memory exhaustion due to oversized or excessive payloads.
  2. Processing delays or crashes caused by malformed packets.
  3. Potential system instability or downtime from repeated rapid requests.

## How It Works
1. The LabyMod API listens on the `laby:mod` plugin channel for communication with clients.
2. The script establishes a connection and sends rapid, small payloads in succession to exploit possible rate-limiting gaps.
3. If the server lacks sufficient validation or protection, these payloads may disrupt normal operations or cause downtime.

## Usage Instructions
1. Clone this repository:
   git clone https://github.com/jip-0-0-0-0-0/laby-dos
2. Open the `dos_poc.py` script and configure the following:
   - Replace `<SERVER_IP>` with your server's IP address.
   - Replace `<SERVER_PORT>` with your server's port.
3. Run the script:
   python3 dos_poc.py

## Disclaimer
This project is intended for educational purposes and authorized testing only. Unauthorized use of this script on servers you do not own or manage may violate laws and regulations.

## License
This repository is licensed under the MIT License.
