# models.py

from typing import List, Optional, Union
from pydantic import BaseModel, Field
from datetime import date


class DataValueInformation(BaseModel):
    name: str = Field(
        ...,
        description="The name of the input or output, must be unique,\
will be used to identify the input or output",
        example="my_data_01",
    )
    type: str = Field(
        ...,
        description="The type of the input or output, only string, number,\
boolean and array are supported",
        example="string",
        enum=["string", "number", "boolean", "array"],
    )
    description: Optional[str] = Field(
        None,
        description="The description of the input or output",
        example="This data is used to do something",
    )


class ValueInformationString(DataValueInformation):
    type: str = Field("string", Literal=True, example="string", enum=["string"])
    availableValues: Optional[List[str]] = Field(
        None,
        description="The list of available values for this input",
        example=["my value", "my other value"],
    )
    default: Optional[str] = Field(
        None, description="The default value for this input", example="my value"
    )


class ValueInformationNumber(DataValueInformation):
    type: str = Field("number", Literal=True, example="number", enum=["number"])
    availableValues: Optional[List[float]] = Field(
        None,
        description="The list of available values for this input",
        example=[1, 2, 3],
    )
    min: Optional[float] = Field(
        None, description="The minimum value for this input", example=0
    )
    max: Optional[float] = Field(
        None, description="The maximum value for this input", example=10
    )
    default: Optional[float] = Field(
        None, description="The default value for this input", example=5
    )


class ValueInformationBoolean(DataValueInformation):
    type: str = Field("boolean", Literal=True, example="boolean", enum=["boolean"])
    default: Optional[bool] = Field(
        None, description="The default value for this input", example=True
    )


class ValueInformationArray(DataValueInformation):
    type: str = Field("array", Literal=True, example="array", enum=["array"])
    arrayType: str = Field(
        ...,
        description="Specify type of the array, only string, number and\
boolean supported",
        example="string",
        enum=["string", "number", "boolean", "dict", "array"],
    )
    lengthMin: Optional[int] = Field(
        None, description="The minimum length of the array", example=0
    )
    lengthMax: Optional[int] = Field(
        None, description="The maximum length of the array", example=10
    )


InputOutputType = Union[
    ValueInformationString,
    ValueInformationNumber,
    ValueInformationBoolean,
    ValueInformationArray,
]


class Algorithm(BaseModel):
    id: str = Field(
        ...,
        description="The id of the algorithm, must be unique, will be used\
to identify the algorithm",
        example="my-algorithm-01",
    )
    name: Optional[str] = Field(
        None, description="The name of the algorithm", example="My algorithm 01"
    )
    description: Optional[str] = Field(
        None,
        description="The description of the algorithm",
        example="This algorithm is used to do something",
    )
    tags: Optional[List[str]] = Field(
        None, description="The list of tags of the algorithm", example=["tag1", "tag2"]
    )
    author: Optional[str] = Field(
        None, description="The author of the algorithm", example="Ada Lovelace"
    )
    creationDate: date = Field(
        ...,
        description="The creation date of the algorithm, ISO 8601 format, YYYY-MM-DD",
        example="2023-01-01",
    )
    updateDate: Optional[date] = Field(
        None,
        description="The last algorithm update date, ISO 8601 format, YYYY-MM-DD",
        example="2023-03-20",
    )
    version: str = Field(
        ..., description="The version of the algorithm", example="0.1.0"
    )
    inputs: List[InputOutputType] = Field(
        ..., description="The list of inputs of the algorithm"
    )
    outputs: List[InputOutputType] = Field(
        ..., description="The list of outputs of the algorithm"
    )
