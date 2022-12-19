from datetime import datetime
from typing import Optional

from pydantic import BaseModel, validator

from elementary.utils.time import DATETIME_FORMAT, convert_local_time_to_timezone


class DataMonitoringFilter(BaseModel):
    invocation_id: Optional[str] = None
    invocation_time: Optional[str] = None
    last_invocation: Optional[bool] = False

    @validator("invocation_time", pre=True)
    def format_invocation_time(cls, invocation_time):
        if invocation_time:
            invocation_datetime = convert_local_time_to_timezone(
                datetime.fromisoformat(invocation_time)
            )
            return invocation_datetime.strftime(DATETIME_FORMAT)
        return None
