from dataclasses import dataclass

@dataclass(slots=True)
class DnevnikObj:
    ID:int = 0
    DatumCas:str = ""
    visina:float = 0.0
    teza:float = 0.0
    itm:float = 0.0