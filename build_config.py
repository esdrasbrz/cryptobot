import os
import json

config_template = {
    "dry_run": True,
    "db_url": "sqlite:////data/tradesv3.dry_run.sqlite",
    "exchange": {
        "name": "binance",
        "key": "",
        "secret": "",
        "ccxt_config": {
            "enableRateLimit": True,
            "rateLimit": 60,
            "options": {
                "brokerId": None,
                "partner": {
                    "spot": {
                        "id": None,
                        "key": None
                    },
                    "future": {
                        "id": None,
                        "key": None
                    }
                }
            }
            },
            "ccxt_async_config": {
            "enableRateLimit": True,
            "rateLimit": 60,
            "options": {
                "brokerId": None,
                "partner": {
                    "spot": {
                        "id": None,
                        "key": None
                    },
                    "future": {
                        "id": None,
                        "key": None
                    }
                }
            }
        }
    },
    "telegram": {
        "enabled": True,
        "token": "",
        "chat_id": ""
    },
    "api_server": {
        "enabled": True,
        "listen_ip_address": "0.0.0.0",
        "listen_port": 8080,
        "username": "admin",
        "password": "admin"
    }
}

def main():
    binance_key = os.environ.get('BINANCE_KEY', '')
    binance_secret = os.environ.get('BINANCE_SECRET', '')

    telegram_token = os.environ.get('TELEGRAM_TOKEN', '')
    telegram_chat_id = os.environ.get('TELEGRAM_CHAT_ID', '')

    dry_run = os.environ.get('DRY_RUN', 'true').lower() == 'true'

    config = config_template

    with open('./user_data/config-private.json', 'w', encoding='UTF-8') as fout:
        config['exchange']['key'] = binance_key
        config['exchange']['secret'] = binance_secret

        config['telegram']['token'] = telegram_token
        config['telegram']['chat_id'] = telegram_chat_id

        config['dry_run'] = dry_run

        if not dry_run:
            config['db_url'] = config['db_url'].replace('.dry_run', '')

        json.dump(config_template, fout, indent=4)

if __name__ == '__main__':
    main()
