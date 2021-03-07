#!/usr/bin/python

from .constants import AtlasResponseCodes

class BaseResponse:
    def __init__(self, status_code: AtlasResponseCodes = AtlasResponseCodes.UNDEFINED, response_data: str = None):
        self._status_code = status_code
        self._response_data = response_data

    @property
    def status_code(self) -> AtlasResponseCodes:
        return self._status_code

    @property
    def response_data(self) -> str:
        return self._response_data
    
class SingleStringResponse(BaseResponse):
    def __init__(self, status_code: AtlasResponseCodes = AtlasResponseCodes.UNDEFINED, response_data: str = None):
        super().__init__(status_code, response_data)

    @property
    def response(self) -> str:
        return self.response_data

    
class SingleIntResponse(BaseResponse):
    def __init__(self, status_code: AtlasResponseCodes = AtlasResponseCodes.UNDEFINED, response_data: str = None):
        super().__init__(status_code, response_data)

    @property
    def response(self) -> int:
        return int(self.response_data)

    
class SingleFloatResponse(BaseResponse):
    def __init__(self, status_code: AtlasResponseCodes = AtlasResponseCodes.UNDEFINED, response_data: str = None):
        super().__init__(status_code, response_data)

    @property
    def response(self) -> float:
        return float(self.response_data)

class MultipleResponse(BaseResponse):
    def __init__(self, status_code: AtlasResponseCodes, response_data: str):
        super().__init__(status_code=status_code, response_data=response_data)

    @property
    def responses(self) -> list[str]:
        return str.split(self.response_data, ",")