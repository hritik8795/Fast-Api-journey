from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from db.database import get_db
from schemas.report import DashboardReport


router = APIRouter(prefix="/reports", tags=["Reports"])
from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from schemas.report import DashboardReport


router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/dashboard", response_model=DashboardReport)
async def get_dashboard_report(
    db: AsyncSession = Depends(get_db)
):
    print("Fetching dashboard report...")
    result = await db.execute(
        text("select * from get_dashboard_report()")
    )

    row = result.fetchone()

    return DashboardReport(
        total_users=row.total_users,
        # total_blogs=row.total_blogs,
        # total_comments=row.total_comments
    )