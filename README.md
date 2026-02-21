# 🧮 Talli-SMS-Gateway

**🚀 The Apex of Digital Accounting. AI-Architected. Human-Engineered.**

Zero fees. Zero middleman. Just raw **SIM-card** power delivered straight to your ledger. This isn't just a spreadsheet; it's a high-frequency automation engine designed for those who demand immediate transaction updates and absolute financial transparency.

`sms-gateway` • `ledger` • `business-automation` • `python-proxy` • `local-first` • `no-fee`

---

## ⚡ The Power

Stop paying for sluggish bulk SMS services that eat your profit. Talli-SMS-Gateway is built for **speed and sovereignty**.

-   **SIM-Injection Core**: Powered by a Flask-proxy, tapping directly into your Android device's SMS pipeline. We don't pay providers for permission; we take the carrier signal you've already paid for.
-   **Smart Bengali Synthesis**: Our engine crafts personalized messages in real-time. If a record has no fines or extra payments, Talli intelligence prunes the message dynamically. No clutter, just pixels of precision.
-   **Proxy-Shielded Logic**: We bypass browser-level CORS restrictions with a dedicated Python backend. Your network communication isn't just fast; it's bulletproof.
-   **Zero-Cloud Sovereignty**: Your records remain on your local machine. No data leaks, no subscriptions, no prying eyes. Your business, your data.
-   **Latency-Linked Updates**: Real-time status feedback for every SMS sent. If the gateway app is running, the message fires. We don't buffer; we deliver.

---

## 🛠️ The Gear (Requirements)

-   **OS**: Windows/Linux/MacOS (Backend runs anywhere Python lives).
-   **Mobile**: Android Phone (Required for the SIM-gateway app).
-   **Python**: 3.11+
-   **Manager**: [uv](https://github.com/astral-sh/uv) (We standardise on `uv` for its superior dependency resolution speed).

---

## 🚀 Ignition (Installation)

1.  **Clone the Repository**:
    ```bash
    git clone https://github.com/AmiXDme/Talli-SMS-Gateway.git
    cd Talli-SMS-Gateway
    ```

2.  **Sync Dependencies**:
    ```bash
    uv sync
    ```

3.  **Launch (The Savage Way)**:
    Just double-click **`RUN_TALLI.bat`** or run:
    ```bash
    uv run app.py
    ```
    *Access at http://localhost:5000. Take control. That's it.*

---

## 📱 Mobile Integration (Gateway Setup)

1.  **Grab an Android phone.**
2.  **Install the [Simple SMS Gateway](https://play.google.com/store/apps/details?id=com.pabrikaplikasi.simplesmsgateway)** (by Pabrik Aplikasi).
3.  **Tap "Start Server"** on the app.
4.  **Copy the IP Address** shown in the app (e.g., `http://192.168.1.100:8080`).
5.  In Talli web settings, hit **⚙️ SMS গেটওয়ে সেটিংস** and paste that IP.
6.  **Save.** You are now a telecom powerhouse.

---

## 🏗️ Architecture (The Blueprint)

```text
talli/
├── app.py           # The Python Proxy (Bypassing CORS like a pro)
├── index.html       # The UI (Premium aesthetics and savage logic)
├── RUN_TALLI.bat    # The Magic Stick (One-click launch for Windows)
├── pyproject.toml   # Project manifest
└── README.md        # This Manifesto
```

---

## ⚔️ Contributing

Think you can optimize the proxy or improve the UI aesthetics? We want to see it.
Read our **[CONTRIBUTING.md](CONTRIBUTING.md)** before you touch the code. We have standards.

---

## 📺 Witness the Logic

High-performance technical showcases, business automation, and development deep-dives:
[**▶️ Visit the AmiXDme YouTube Channel**](https://www.youtube.com/@AmiXDme)

---

## 📄 License

Apache License 2.0. Clean, open, powerful.

---

*Created by [AmiXDme](https://github.com/AmiXDme). Think you're better than the machine? Prove it.*
