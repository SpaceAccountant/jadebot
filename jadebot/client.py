from abc import ABC, abstractmethod

class Client( ABC ):
  """The interface for a Jadebot client.
  """

  @abstractmethod
  def run( self ) -> None:
    """Runs the client.
    """

    pass
