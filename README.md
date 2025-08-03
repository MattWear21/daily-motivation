# 🚀 Daily Dose of Motivation (Local LLM Powered)

**Never miss a beat! Get your daily dose of uplifting motivation delivered directly to your phone, powered by local LLMs and Discord webhooks.**

This project demonstrates a simple yet effective way to generate personalized motivational messages using an on-device Large Language Model (LLM) and push them as notifications to your mobile device via Discord. Say goodbye to generic platitudes and hello to AI-crafted inspiration, all while keeping your data private and your processing local.

## ✨ Features

*   **Local LLM Power:** Leverages local LLMs (like Gemma 3, Llama 3, etc. via Ollama) for privacy-preserving, on-device motivation generation. No cloud APIs, no data sharing.
*   **Discord Push Notifications:** Utilizes Discord webhooks to send motivational messages directly to your phone (or any Discord-enabled device), ensuring timely delivery.
*   **Simple & Lightweight:** A compact Python script designed for easy deployment and minimal resource consumption.
*   **Cron Job Ready:** Perfect for scheduling daily motivational pushes on your home server or any Linux environment.

## 🛠️ How It Works

1.  **Local LLM Interaction:** The Python script connects to your local Ollama instance, feeding a prompt to the chosen LLM (e.g., Gemma 2B) to generate a short, motivational statement.
2.  **Discord Webhook:** The generated motivation is then sent as a payload to a Discord webhook URL, which you've configured in your Discord server.
3.  **Mobile Notification:** Discord, in turn, pushes this message as a notification to your linked mobile device.
4.  **Cron Scheduling:** A cron job on your Linux server handles the automatic execution of the script at your desired time (e.g., every morning).

## 🚀 Getting Started

Follow these steps to set up your Daily Dose of Motivation:

### 1. Install Ollama and Download a Model

First, you need to have Ollama installed and a local LLM model downloaded.

*   **Install Ollama:** Follow the official instructions to install Ollama for your operating system: [https://ollama.com/download](https://ollama.com/download)
*   **Download a Model:** For this project, we recommend a lightweight model like Gemma3 4B for quick responses. Open your terminal and run:
    ```bash
    ollama run gemma3:4b
    ```

### 2. Set up a Discord Webhook

1.  **Create a Discord Server (if you don't have one):** Or use an existing one where you want to receive notifications.
2.  **Create a Text Channel:** Right-click on a server, then click "Create Channel". Choose "Text Channel".
3.  **Get Webhook URL:**
    *   Hover over the newly created channel, click the "Edit Channel" gear icon.
    *   Go to "Integrations" -> "Webhooks" -> "New Webhook".
    *   Give it a name (e.g., "Motivation Bot").
    *   Click "Copy Webhook URL". Keep this URL handy; you'll need it in the next step.

### 3. Project Setup

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your-username/daily-motivation.git
    cd daily-motivation
    ```

2.  **Create a Virtual Environment:** It's good practice to isolate your project dependencies.
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create `.env` File:** Create a file named `.env` in the root of your project directory and add the following:
    ```dotenv
    DISCORD_WEBHOOK_URL="YOUR_DISCORD_WEBHOOK_URL_HERE"
    OLLAMA_MODEL="gemma3:4b" # Or your downloaded model
    ```
    **Remember to replace `"YOUR_DISCORD_WEBHOOK_URL_HERE"` with the actual webhook URL you copied from Discord.**

5.  **Run the Script Manually (Test):**
    ```bash
    python3 src/main.py
    ```
    You should see the motivational message printed in your terminal and also appear as a notification in your Discord channel!

### 4. Schedule with Cron (Linux Server)

This is where the magic happens for daily, automated messages.

1.  **Open Crontab Editor:**
    ```bash
    crontab -e
    ```

2.  **Add a Cron Job Entry:** Add the following line to the end of the file. This example schedules the script to run every day at 7:00 AM.

    ```cron
    0 7 * * * /usr/bin/python3 /path/to/your/daily-motivation/src/main.py >> /path/to/your/daily-motivation/cron.log 2>&1
    ```
    *   `/usr/bin/python3`: The full path to your Python 3 executable. You can find this by running `which python3`.
    *   `/path/to/your/daily-motivation/src/main.py`: **Crucially, replace this with the absolute path to your `main.py` script!**

That's it! Your Linux server will now automatically run the `motivate.py` script at the scheduled time, providing you with a fresh dose of AI-powered motivation every day.
