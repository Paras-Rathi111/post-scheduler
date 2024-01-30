from instabot import Bot
import schedule
import time


def post_on_instagram(image_path, caption, posting_time):
    bot = Bot()
    bot.login(username="instapost844", password="insta@123")

    try:
        schedule.every().day.at(posting_time).do(bot.upload_photo, image_path, caption=caption)

        while True:
            schedule.run_pending()
            time.sleep(1) 
            

    except Exception as e:
        print(f"Error occurred: {e}")

    finally:
        bot.logout()


image_path = "post/test.jpg"
caption = "Your caption here"
posting_time = "12:42" 

post_on_instagram(image_path, caption, posting_time)