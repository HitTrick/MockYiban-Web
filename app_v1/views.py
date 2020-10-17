from datetime import datetime
import random

from django.shortcuts import render
from django.views.generic.base import View

from .forms import InputForm


class SubmitForm(View):
    def post(self, request, *args, **kwargs):
        input_form = InputForm(request.POST)
        if input_form.is_valid():
            in_out = input_form.cleaned_data["in_out"]
            stu_name = input_form.cleaned_data["stu_name"]
            stu_id = input_form.cleaned_data["stu_id"]
            gate = input_form.cleaned_data["gate"]

            now_time = datetime.now()

            records = [
                {
                    "in_out": in_out,
                    "stu_name": stu_name,
                    "stu_id": stu_id,
                    "record_time": now_time.strftime("%Y-%m-%d %H:%M:%S"),
                    "gate": gate,
                }
            ]

            if now_time.hour > 12:
                random_record = {
                    "in_out": in_out,
                    "stu_name": stu_name,
                    "stu_id": stu_id,
                    "record_time": "",
                    "gate": "",
                }

                if random.randint(0, 1) == 0:
                    random_record["gate"] = "南门"
                else:
                    random_record["gate"] = "西门"

                random_time = datetime(now_time.year, now_time.month, now_time.day, random.randint(7, 11),
                                                random.randint(0, 59), random.randint(0, 59))
                random_record["record_time"] = random_time.strftime("%Y-%m-%d %H:%M:%S")

                records.append(random_record)

            return render(request, "display.html", {
                "records_form": records
            })

        return render(request, "error.html")
