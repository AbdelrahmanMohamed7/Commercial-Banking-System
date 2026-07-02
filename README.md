# Commercial Banking & Foreign Exchange (FX) Management System

A robust, terminal-based enterprise banking application built in Python. This system simulates core commercial banking functionalities alongside a dynamic Foreign Exchange (FX) engine, managing real-time data persistence through flat-file structures. 

This project was built to demonstrate clean algorithmic logic, secure state management, and file I/O handling without relying on heavy external database frameworks.

---

## 🚀 Features

### 1. Core Commercial Banking Engine
* **Account Provisioning:** Dynamic generation of unique customer profiles and account numbers.
* **Transaction Ledger:** Secure processing of real-time deposits, withdrawals, and peer-to-peer fund transfers.
* **State Persistence:** Automated logging of system states, transaction histories, and user credentials into flat-file ledgers (`.txt`).

### 2. Foreign Exchange (FX) Engine
* **Multi-Currency Wallets:** Support for currency holding across global denominations.
* **Live-Rate Simulation:** Algorithmic calculation of currency conversions and exchange spreads.
* **FX Transaction Logs:** Dedicated tracking of currency exchange histories and valuation shifts.

### 3. Security & Access Control
* **Credential Masking:** Secured authentication system for user and administrator login tiers.
* **Data Integrity Checks:** Strict server-side validation to prevent negative balances, unauthorized overdrafts, or malformed inputs.

---

## 📂 System Architecture & File Structure

The system uses local data streams to read and write application states dynamically. Ensure all files remain in the same directory:

* `banking_system.py` — The core application executable containing system logic.
* `Fourm.txt` — Customer profile registries.
* `Transaction.txt` — The global transaction ledger.
* `user_id & pass.txt` — Masked user authentication data.
* `ID.txt` — Automated unique ID increment tracker.
* `System_Documentation.pdf` — Comprehensive technical architecture report, flowcharts, and system specifications.

---

## 🛠️ Installation & Setup

### Prerequisites
* Python 3.x installed on your machine.

### Execution
1. Clone this repository to your local machine:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git](https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git)

```

2. Navigate into the project directory:
```bash
cd YOUR_REPOSITORY_NAME

```


3. Run the application:
```bash
python banking_system.py

```



---

## 🖥️ Interface Preview

```text
==================================================
        COMMERCIAL BANKING & FX PLATFORM         
==================================================
1. User Login
2. Open New Commercial Account
3. Admin Dashboard
4. Exit System
==================================================
Select an option: 

```

---

## ⚙️ Technical Skills Demonstrated

* **File Handling & Parsing:** Complex string splitting, parsing, and data cleaning from flat text files.
* **Defensive Programming:** Robust error-handling matrices to intercept invalid terminal inputs and unexpected edge cases.
* **Object/Procedural Logic Flow:** State management mapping out clean user-to-admin permission tiers.
