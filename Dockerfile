FROM freqtradeorg/freqtrade:stable

WORKDIR /app

COPY --chown=ftuser:ftuser NostalgiaForInfinity/configs /app/NostalgiaForInfinity/configs
COPY --chown=ftuser:ftuser user_data /app/user_data
COPY --chown=ftuser:ftuser build_config.py entrypoint.sh /app/

ENTRYPOINT ["./entrypoint.sh"]
CMD ["--config", "/app/user_data/config.json"]