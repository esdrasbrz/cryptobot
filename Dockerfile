FROM freqtradeorg/freqtrade:stable

WORKDIR /app

COPY NostalgiaForInfinity/configs /app/NostalgiaForInfinity/configs
COPY user_data /app/user_data

CMD ["trade", "--config", "/app/user_data/config.json", "--db-url", "sqlite:////data/tradesv3.dry_run.sqlite"]