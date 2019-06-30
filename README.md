# geocoding-telegram-bot

## Usage

Your container has to be exposed to the internet somehow, preferably by a reverse proxy with SSL.

```
docker run -d -it \
    --restart always \
    -e TELEGRAM_API_KEY={TELEGRAM_API_KEY} \
    -e MAPS_API_KEY={MAPS_API_KEY} \
    -e WEBHOOK_URL={YOUR_URL}/bot \
    -e WEBHOOK_SERVER_PORT={WEBHOOK_SERVER_PORT} \
    victor141516/geocoding-telegram-bot
```
