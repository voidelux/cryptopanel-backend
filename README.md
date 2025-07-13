
# 🚀 CryptoTracker Backend API

Backend service for the CryptoTracker app — a cryptocurrency tracker with up-to-date prices, changes, and charts.

## 📚 Contents

* [Technologies](#technologies)
* [Installation](#installation)
* [Running the app](#running-the-app)
* [API Endpoints](#api-endpoints)
* [Project Structure](#project-structure)
* [Deployment](#deployment)

## 🛠️ Technologies

* **FastAPI**: Modern, fast web framework for building APIs with automatic docs generation
* **Python 3.10+**: Primary programming language
* **CoinGecko API**: Source for cryptocurrency data
* **Docker**: Containerization of the application

## ⚙️ Installation

### Prerequisites

* Python 3.10+
* pip

### Install dependencies

```bash
# Clone the repository
git clone https://github.com/yourusername/cryptotracker.git
cd cryptotracker/backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Environment variables setup

Create a `.env` file in the backend root directory:

```env
COINGECKO_API_KEY=your_api_key
```

## ▶️ Running the app

### Local development server

```bash
# Create virtual environment
python -m venv .venv

# Activate virtual environment (if not activated yet)
source .venv/bin/activate  # On Windows: venv\Scripts\activate

# Run dev server
uvicorn main:app --reload --port 5174
```

### Running with Docker

```bash
# Build Docker image
docker build -t cryptotracker-backend .

# Run Docker container
docker run -p 5174:5174 -d cryptotracker-backend
```

## 🔌 API Endpoints

### Cryptocurrency data

#### Bitcoin

```
GET /bitcoin
```

Returns current Bitcoin price.

Example response:

```json
{
  "price": "48000.25"
}
```

```
GET /bitcoin/change
```

Returns 24h percentage price change for Bitcoin.

Example response:

```json
{
  "change": 2.45
}
```

```
GET /bitcoin/chart
```

Returns data for Bitcoin price chart.

Example response:

```json
{
  "chart": {
    "data": [40000, 41200, 40800, 42100, 41900, 43000, 42600, 43240]
  }
}
```

#### Monero

```
GET /monero
```

Returns current Monero price.

```
GET /monero/change
```

Returns 24h percentage price change for Monero.

```
GET /monero/chart
```

Returns data for Monero price chart.

#### Toncoin

```
GET /toncoin
```

Returns current Toncoin price.

```
GET /toncoin/change
```

Returns 24h percentage price change for Toncoin.

```
GET /toncoin/chart
```

Returns data for Toncoin price chart.

### 📄 API Documentation

```
GET /docs
```

FastAPI automatically generates interactive Swagger UI documentation.
