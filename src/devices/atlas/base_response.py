#!/usr/bin/python

from .constants import AtlasResponseCodes

class BaseResponse:
    def __init__(self, status_code: AtlasResponseCodes = AtlasResponseCodes.UNDEFINED, response_data: str = None):
        self.status_code = status_code
        self.response_data = response_data

    @property
    def status_code(self) -> AtlasResponseCodes:
        return self.status_code

    @property
    def response_data(self) -> str:
        return self.response_data
    