from django.core.management.base import BaseCommand
from mcp.server.mcp_server import McpServer


class Command(BaseCommand):
    help = "Start the server MCP"

    def handle(self, *args, **kwargs):
        servidor = McpServer()
        servidor.handle()
