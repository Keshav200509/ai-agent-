"""Unit tests for agent/discord_bot.py — DiscordBot class."""

from agent.discord_bot import DiscordBot


def test_discord_bot_init_defaults():
    """DiscordBot can be instantiated with default arguments."""
    bot = DiscordBot()
    assert isinstance(bot, DiscordBot)


def test_discord_bot_init_with_params():
    """DiscordBot stores token and webhook_url when provided."""
    bot = DiscordBot(token="tok-123", webhook_url="https://hook.example.com")
    assert isinstance(bot, DiscordBot)


def test_post_summary_returns_none_for_stub():
    """post_summary is a stub that returns None (no implementation yet)."""
    bot = DiscordBot()
    result = bot.post_summary("chan1", "Title", "Summary text", "http://link")
    assert result is None


def test_register_command_returns_none_for_stub():
    """register_command is a stub that returns None."""
    bot = DiscordBot()
    result = bot.register_command("test_cmd", lambda: None)
    assert result is None
