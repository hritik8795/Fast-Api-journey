from pydantic import BaseModel

class DashboardReport(BaseModel):
    total_users: int
    # total_blogs: int
    # total_comments: int

    class Config:
        orm_mode = True
        