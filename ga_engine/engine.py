from ._send import Send
from typing_extensions import deprecated

@deprecated("Use au_engines instead")
class GaEngine(Send): ...