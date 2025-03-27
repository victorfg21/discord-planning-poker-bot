# Discord Planning Poker Bot

A Discord bot designed to facilitate Planning Poker sessions within your server, aiding agile teams in estimating task complexities collaboratively.

## Features

- **Interactive Sessions**: Engage team members in real-time estimation discussions directly within Discord.
- **Customizable Settings**: Tailor the bot's behavior to fit your team's specific needs and workflows.
- **User-Friendly Commands**: Simple and intuitive commands to start, join, and manage Planning Poker sessions.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/victorfg21/discord-planning-poker-bot.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd discord-planning-poker-bot/src
   ```

3. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the project directory and add your Discord bot token:
   ```env
   DISCORD_TOKEN=your_discord_bot_token
   ```

5. **Run the Bot**:
   ```bash
   python bot.py
   ```

## Usage

Once the bot is running and added to your Discord server:

- **Start a Session**: Use the `!pokerstart` command in a text channel to initiate a Planning Poker session.
- **Join a Session**: Participants can join the session by reacting to the bot's prompt message.
- **Submit Estimates**: After the story or task is presented, participants send their estimates via direct message to the bot.
- **View Results**: Use the `!pokerresults` command in a text channel to end a Planning Poker session. The bot will compile and display all estimates in the channel after a set time, facilitating team discussion and consensus.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

*Note: This README provides a general overview based on standard features commonly found in Discord Planning Poker bots. For specific functionalities and command details, please refer to the source code or contact the repository maintainer.*

