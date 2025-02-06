from typing import List
from dataclasses import dataclass

from data.insee_codes import INSEE_CODES

@dataclass(repr=True, eq=True)
class Insee:
    __VALID_CODES = [insee for insee in INSEE_CODES]

    code: int

    def __post__init__(self):
        self.insee_codes: List[int] = [insee for insee in INSEE_CODES]
        # validate
        if not (0000 <= self.code > 9999):
            raise ValueError(f'Insee codes must be a value between 0001 and 9999')
        if self.code not in self.__VALID_CODES:
            raise ValueError(f'Insee Code {self.code} is not  in the valid code list')
        
    # TODO : add usefull methods
    @classmethod
    def get_all_codes(cls):
        """Return list of all valid codes"""
        return cls.__VALID_CODES.copy()
    
    @classmethod
    def is_valid_code(cls, code: int) -> bool:
        """Validate a code"""
        return code in cls.__VALID_CODES
    # - get one -get all - as dict - order by ??
    
@dataclass(repr=True, eq=True)
class Command:
    argument: int
    id: int

@dataclass(repr=True, eq=True)
class WCSCommandPayload:
    clientType: int
    clientPriority: int
    contractType: int
    buildingType: int
    contractRateCode: int
    customerGroupNumberOne: int
    customerGroupNumberTwo: int
    useType: int
    countyCode: int
    townCode: int
    districtCode: int
    command: Command

@dataclass(repr=True, eq=True)
class OctoWCSPayload:
    name: str
    description: str
    insee_codes: List[int]
    command_payload: WCSCommandPayload
    is_enabled: bool
    execution_time: str
