# geocoding-telegram-bot

## Usage

Your container has to be exposed to the internet somehow, preferably by a reverse proxy with SSL.
PLACES_API_KEY must be a Google Places enabled API key.

```
docker run -d -it \
    --restart always \
    -e TELEGRAM_API_KEY={TELEGRAM_API_KEY} \
    -e PLACES_API_KEY={PLACES_API_KEY} \
    -e WEBHOOK_URL={YOUR_URL}/bot \
    -e WEBHOOK_SERVER_PORT={WEBHOOK_SERVER_PORT} \
    victor141516/geocoding-telegram-bot
```
