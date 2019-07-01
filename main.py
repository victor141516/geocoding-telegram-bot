import datetime
from geo import get_coordinates
import logging
import os
from telegram.ext import Updater, InlineQueryHandler
from telegram import (
    InputTextMessageContent,
    InlineQueryResultArticle,
    InputVenueMessageContent,
)


ENVS = ["TELEGRAM_API_KEY", "PLACES_API_KEY"]
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
WEBHOOK_SERVER_PORT = os.environ.get("WEBHOOK_SERVER_PORT")
config = {k: os.environ[k] for k in ENVS}
config["WEBHOOK_URL"] = WEBHOOK_URL
config["WEBHOOK_SERVER_PORT"] = WEBHOOK_SERVER_PORT
config["CURRENT_MONTH"] = datetime.datetime.now().month
config["NOF_API_QUERYS"] = 0


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


updater = Updater(token=config["TELEGRAM_API_KEY"], use_context=True)
dispatcher = updater.dispatcher


def inline_caps(update, context):
    query = update.inline_query.query
    if not query:
        return

    inline_results = []

    if datetime.datetime.now().month != config["CURRENT_MONTH"]:
        config["CURRENT_MONTH"] = datetime.datetime.now().month
        config["NOF_API_QUERYS"] = 0

    if config["NOF_API_QUERYS"] > 2000:
        inline_results.append(
            InlineQueryResultArticle(
                id=query.upper(),
                title="API limit reached",
                input_message_content=InputTextMessageContent("API limit reached"),
            )
        )
    else:
        geocoding_results = get_coordinates(config["PLACES_API_KEY"], query)

        config["NOF_API_QUERYS"] += 1

        if len(geocoding_results) == 0:
            inline_results.append(
                InlineQueryResultArticle(
                    id=query.upper(),
                    title="No results",
                    input_message_content=InputTextMessageContent("No results"),
                )
            )
        else:
            for gr in geocoding_results:
                inline_results.append(
                    InlineQueryResultArticle(
                        id=query.upper(),
                        title=gr["formatted"],
                        input_message_content=InputVenueMessageContent(
                            title=gr["name"],
                            address=gr["formatted"],
                            latitude=gr["lat"],
                            longitude=gr["lng"],
                        ),
                    )
                )
    context.bot.answer_inline_query(update.inline_query.id, inline_results)


inline_caps_handler = InlineQueryHandler(inline_caps)
dispatcher.add_handler(inline_caps_handler)


if config["WEBHOOK_URL"] and config["WEBHOOK_SERVER_PORT"]:
    updater.start_webhook(
        listen="0.0.0.0", port=config["WEBHOOK_SERVER_PORT"], url_path="bot"
    )
    updater.bot.set_webhook(webhook_url=config["WEBHOOK_URL"])
else:
    updater.start_polling()
