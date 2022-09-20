from typing import Optional, Union, Literal
from pydantic import BaseModel
from datetime import datetime


class By(BaseModel):
    orgId: str
    userId: str


class Trigger(BaseModel):
    by: By
    origin: Union[Literal["UI"], Literal["API"]]
    at: datetime


class Context(BaseModel):
    blueprint: Optional[str]
    entity: Optional[str]
    runId: Optional[str]


class Before(BaseModel):
    identifier: str
    title: str
    blueprint: str
    properties: dict
    relations: dict
    createdAt: str
    createdBy: str
    updatedAt: str
    updatedBy: str


class After(BaseModel):
    identifier: str
    title: str
    blueprint: str
    properties: dict
    relations: dict
    createdAt: str
    createdBy: str
    updatedAt: str
    updatedBy: str


class Diff(BaseModel):
    before: Optional[Before]
    after: Optional[After]


class Webhook(BaseModel):
    action: Union[Literal["CREATE"], Literal["UPDATE"], Literal["DELETE"]]
    resourceType: Union[Literal["run"], Literal["entity"], Literal["blueprint"]]
    status: str
    trigger: Trigger
    context: Context
    diff: Diff
