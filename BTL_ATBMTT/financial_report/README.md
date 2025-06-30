# �� Secure Financial Report Transmission with Compression
**Final Project – Introduction to Information Security**  
**Student: Lê Trọng Nhân – Year 2 – University of Information Technology**

---

## �� Project Description

This project demonstrates a secure system for transmitting financial reports using symmetric encryption (DES) combined with file compression techniques. It simulates a real-world scenario where sensitive financial data must be securely sent over a network.

---

## ⚙️ Technologies Used

- **Python 3.10+**
- **Socket programming**
- **DES encryption** (from `pyDes` library)
- **ZIP compression** (`zipfile` built-in module)
- **Client–Server architecture**
- **LaTeX** for documentation (based on Overleaf professional template)

---

## ��️ System Architecture

```
+----------------+         Encrypted + Compressed         +----------------+
|  Sender (Client) | -----------------------------------> | Receiver (Server) |
|    DES + ZIP    |                                     |   Decrypt + Extract |
+----------------+                                     +----------------+
```

All communication is done over TCP sockets. The client encrypts and compresses the financial report before sending. The server receives, decrypts, and extracts the content.

---

## ��️ Project Structure

```
project-root/
├── code/                    # Source code (Python)
│   ├── client.py
│   ├── server.py
│   ├── des_crypto.py
│   ├── compression.py
│   └── financial_report/    # Input file
├── figs/                    # Images (test logs, architecture diagrams)
├── assets/                  # Additional resources
├── chapters/                # LaTeX report chapters
├── styles/                  # LaTeX formatting
├── thesis.tex               # Main LaTeX file
├── refs.bib                 # Bibliography
└── README.md
```

---

## �� How to Run

### 1. Install dependencies

```bash
pip install pyDes
```

### 2. Start the server

```bash
python code/server.py
```

### 3. Run the client

```bash
python code/client.py
```

The encrypted and compressed financial report will be sent to the server and extracted at the destination.

---

## �� Report (PDF)

The full report is written in LaTeX and includes:

- Introduction to the problem and motivation
- System architecture and algorithm design
- Code implementation and experiment logs
- Conclusion and future directions
- Appendix with full source code

> �� The report follows the [Overleaf academic template](https://www.overleaf.com/project/67acb5eed4f0850f6fc86e76) strictly and is formatted in Times New Roman, size 14, ready for academic submission.

---

## �� References

Full list in [`refs.bib`](./refs.bib), including:

- DES encryption standards
- Python socket documentation
- Data compression theory
- Network security fundamentals

---

## ��‍�� Author

- **Lê Trọng Nhân** – Student ID: 177102051  
- Email: [lenhan16112005@gmail.com]  
- Dai Nam University – Class of Ìnormation and technology 17-11  

---

## �� License

This project is for educational purposes only. Do not reuse the encryption design for production-level security systems.
