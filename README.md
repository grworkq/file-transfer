# File Transfer 

A TCP file transfer application written in Python using the standard socket library

## Description

This project allows a client to send any file to a server over a TCP connection.

Instead of loading the entire file into memory, the client reads the file in small chunks and sends them one by one. The server receives the data, reconstructs the original file, and saves it to disk.

To correctly identify incoming data, a simple binary protocol was implemented.

## Features 

- Send files of any type 
- Chunk-based file transfer (4096-byte blocks)
- Binary file support
- Custom TCP protocol
- Automatic file reconstruction
- Modular and lightweight implementation
- Uses only Python standard libriares

## Project Structure
```text
file-transfer/
|
├── client.py           # Sends files
├── server.py           # Receives files
├── server_files/       # Saved files
└── README.md
```

## Protocol

```text
The client sends data in the following order:

4 bytes     -> filename length
N bytes     -> filename
8 bytes     -> file size
N bytes     -> file data

The server reads the information in exactly the same order before receiving the file contents.
```

## How to Run

#### Start the server
```bash
python server.py
```

### Start the client

```bash
python client.py
```

Enter the absolute path to the file you want to send.

The received file will be saved inside the server_files directory.

## Technologies Used

- Python
- socket
- pathlib
- TCP networking

## What I Learned

- Binary file processing (rb / wb)
- Sending large files over TCP
- Reading and writing files in chunks
- Designing a custom binary protocol
- Converting integers to bytes (to_bytes)
- Restoring integers from bytes (from_bytes)
- Working with file metadata
- Reconstructing files on the receiver side