# 📈 Tesla Stock & News Alert System 🚀

This project is a **Python-based automation tool** that monitors **Tesla Inc. (TSLA)** stock daily, detects significant price changes, fetches related breaking news, and instantly sends **SMS alerts** using the Twilio API. Perfect for anyone who wants real-time, actionable stock insights.

---

## 🔍 Features

- 📊 Fetches **daily stock data** for TSLA using the [Alpha Vantage API](https://www.alphavantage.co/documentation/)
- 🧠 Calculates **percentage change** between yesterday and the day before
- 📰 If change > 1%, fetches **latest Tesla news headlines** using the [News API](https://newsapi.org/)
- 💬 Sends a summary of headlines directly to the user via **SMS using Twilio**
- ⚙️ Fully automated and extendable for multiple stocks

---

## 🛠️ Tech Stack

- **Python** (requests, json)
- **Alpha Vantage API** – Stock data
- **News API** – Recent news
- **Twilio API** – SMS delivery

---

## 📦 Installation

```bash
git clone https://github.com/your-username/tesla-stock-alert.git
cd tesla-stock-alert
pip install -r requirements.txt
