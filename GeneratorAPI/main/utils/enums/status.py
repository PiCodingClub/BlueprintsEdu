from utils.enums.enum import Enum


class Status(Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    GENERATION_FAILED = "GENERATION_FAILED"
    PROJECT_REGISTRATION_FAILED = "PROJECT_REGISTRATION_FAILED"
    INVALID_API_CALL = "INVALID_API_CALL"
    NONE = "NONE"
    NOT_PROVIDED = "NOT_PROVIDED"
    PROJECT_REGISTERED = "PROJECT_REGISTERED"
    PROJECT_EXISTS = "PROJECT_EXISTS"
    NOT_FOUND = "NOT_FOUND"
    INVALID_DATA = "INVALID_DATA"
    BAD_REQUEST = "BAD_REQUEST"
    ACCESS_FAILED = "ACCESS_FAILED"