from typing import List
import argparse
import importlib
import sys

arg_parser = argparse.ArgumentParser(
  usage='%(prog)s [PROVIDER]',
  description='Runs a Jadebot with the specified provider.'
)
arg_parser.add_argument( 'provider' )

provider_name = 'testing'
provider = importlib.import_module( f'providers.{provider_name}' ).instance
client = provider.client()
client.run()
