class DiscordBot:
    def __init__(self, token=None, webhook_url=None):
        self.token = token
        self.webhook_url = webhook_url

    def post_summary(self, channel_id: str, title: str, summary_text: str, doc_link: str) -> dict:
        """Posts message + buttons (view doc, add to calendar)."""
        raise NotImplementedError("post_summary is not yet implemented")

    def register_command(self, command_name: str, callback):
        """Allow community members to invoke agent actions."""
        raise NotImplementedError("register_command is not yet implemented")
