from internet_speed_twitter_bot import InternetSpeedTwitterBot

PROMISED_DOWN = 150
TWITTER_EMAIL = "vinicius92as@gmail.com"
TWITTER_PASSWORD = "Johnny743399#"


internet_bot = InternetSpeedTwitterBot()

internet_bot.get_internet_speed()
internet_bot.tweet_at_provider()

