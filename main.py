from app.core.logger import Logger

logger = Logger("Core")

# Test Error Example
try:
    valcum = 0
    print(valcum[0])

except Exception as e:
    logger.error(f"error: {e}")


logger.info("Im Here!")
logger.warn("Warning!")