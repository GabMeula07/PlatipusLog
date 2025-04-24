from app.core.logger import Logger

logger = Logger("Core", "production")

# Test Error Example
try:
    valcum = 0
    print(valcum[0])

except Exception as e:
    logger.error(f"error: {e}")

logger.debug("This is a debug")
logger.info("This is a info")
logger.warn("This is a warn")
logger.error("This is a error")
logger.critical("this is a critical")


