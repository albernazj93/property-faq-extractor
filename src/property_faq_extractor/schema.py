# This holds the JSON schema that the LLM should return. It uses Pydantic.

from pydantic import BaseModel

class FAQ(BaseModel):
    question: str
    answer: str
    citation: list[str]