from pydantic import BaseModel
class FolderRequest(BaseModel):
    name: str
    parent_id: int | None = None