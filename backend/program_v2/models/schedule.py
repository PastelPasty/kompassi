from __future__ import annotations

from typing import TYPE_CHECKING

from django.db import models

from .program import Program

if TYPE_CHECKING:
    pass


class ScheduleItem(models.Model):
    id: int

    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name="schedule_items")
    subtitle = models.CharField(max_length=255, blank=True)
    start_time = models.DateTimeField()
    length = models.DurationField()

    # denormalized fields
    cached_end_time = models.DateTimeField()

    def __str__(self):
        return self.title

    @property
    def title(self):
        if self.subtitle:
            return f"{self.program.title}: {self.subtitle}"
        else:
            return self.program.title

    @property
    def end_time(self):
        return self.start_time + self.length
