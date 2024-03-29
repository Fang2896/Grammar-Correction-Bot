from token_config_manager import TokenConfigManager
from prompt_config_manager import PromptConfigManager
from gpt_client import GPTClient
from discord_bot import DiscordBot


def main():
  token_config_manager = TokenConfigManager()
  prompt_config_manager = PromptConfigManager('prompt_config.json')

  gpt_client = GPTClient(token_config_manager.get("OPENAI_KEY"))

  discord_bot = DiscordBot(token_config_manager.get("DISCORD_TOKEN"), 
                           token_config_manager.get("GROUP_ID"),
                           gpt_client, prompt_config_manager)
  discord_bot.run()

if __name__ == "__main__":
    main()
