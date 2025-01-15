from app.ParkApi import app, scrape_data, load_parks  # Import app and scrape_data from ParkApi.py
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
    if not load_parks():
        scrape_data()
    app.run(host="127.0.0.1", port=5001)  # Localhost, port 5001

