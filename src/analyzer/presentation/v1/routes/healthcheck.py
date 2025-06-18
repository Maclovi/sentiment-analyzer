from fastapi import APIRouter, status

router = APIRouter(
    prefix="/healthcheck",
    tags=["Healthcheck"],
    include_in_schema=True,
)


@router.get("", status_code=status.HTTP_200_OK)
async def get_status() -> dict[str, str]:
    return {"message": "ok", "status": "success"}
