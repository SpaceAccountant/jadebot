from abc import ABC, abstractmethod
from typing import Type

from jadebot.client import Client

class Provider( ABC ):
  """The interface for the provider of a Jadebot framework
     implementation.
  """

  @property
  @abstractmethod
  def client( self ) -> Type[Client]:
    """The client type for the provider.
    """

    pass
