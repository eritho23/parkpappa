from app import app, scrape_data  # Import app and scrape_data from app.py
import schedule
import threading
import time

def schedule_scrape():
    # Schedule the scrape_data function to run daily at midnight
    schedule.every().day.at("00:00").do(scrape_data)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Start the scheduling thread
threading.Thread(target=schedule_scrape, daemon=True).start()

if __name__ == '__main__':
    app.run()
