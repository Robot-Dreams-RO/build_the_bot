"""A simple Discord bot that fetches the top 5 stories from Hacker News."""
import os
import requests
import discord
from discord.ext import commands


def get_top_stories():
    """Request the latest 5 stories from hackernews.

    Args:
        None

    Returns:
        response (json): Latest 5 stories
    """
    url = "https://hacker-news.firebaseio.com/v0/topstories.json"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        return response.json()[:5]  # Return only the top 5 stories
    else:
        return None


def get_story_details(story_id):
    """Request the details from the story id from hackernews.

    Args:
        story_id (int)

    Returns:
        response (json): Details of a story
    """
    url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json"
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Bot instantiation
intents = discord.Intents.default()
intents.messages = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)


# Bot commands
@bot.command(name="ping")
async def ping(ctx):
    """Ping the bot to check if it's alive."""
    await ctx.send("Pong!")


@bot.command(name="hello")
async def hello(ctx):
    """Say hello to the bot."""
    await ctx.send("Hey! How are you?")


@bot.command(name="bye")
async def bye(ctx):
    """Say goodbye to the bot."""
    await ctx.send("Please don't leave me ...")


@bot.command(name="python")
async def bye(ctx):
    """Say goodbye to the bot."""
    await ctx.send("python is the best language ever!")


@bot.command(name="hn")
async def top_stories(ctx):
    """Fetch the top 5 stories from Hacker News."""
    story_ids = get_top_stories()
    if story_ids:
        for story_id in story_ids:
            story_details = get_story_details(story_id)
            if story_details:
                title = story_details.get("title")
                url = story_details.get("url")
                await ctx.send(f"{title}: {url}")
    else:
        await ctx.send("Failed to fetch the top stories from Hacker News.")


@bot.event
async def on_ready():
    """Print a message when the bot is connected to Discord."""
    print(f"Bot connected as {bot.user}")


if __name__ == "__main__":
    # Load your API key from an environment variable or secret management service
    bot.run(os.getenv("DISCORD_API_KEY"))
