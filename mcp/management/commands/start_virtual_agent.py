from django.core.management.base import BaseCommand
from mcp.virtual_agent import VirtualAgent


class Command(BaseCommand):
    help = "Start the Virtual Agent"

    def handle(self, *args, **kwargs):
        agent = VirtualAgent()
        agent.start()
