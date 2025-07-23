from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ActionProvideDoctorInfo(Action):
    def name(self) -> str:
        return "action_provide_doctor_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: DomainDict) -> list:
        doctor_name = tracker.get_slot("doctor_name")

        # Ví dụ: Tạo thông tin bác sĩ giả định
        doctor_info_db = {
            "bác sĩ an": "Bác sĩ An là chuyên gia nội khoa, làm việc tại bệnh viện A.",
            "bác sĩ bình": "Bác sĩ Bình chuyên khoa nhi, hiện đang công tác tại bệnh viện B.",
            "bác sĩ cường": "Bác sĩ Cường là chuyên gia về tim mạch, lịch làm việc từ thứ 2 đến thứ 6."
        }

        # Chuẩn hóa tên để dễ tra cứu (ví dụ: viết thường)
        doctor_name_lower = doctor_name.lower() if doctor_name else ""

        info = doctor_info_db.get(doctor_name_lower, "Xin lỗi, tôi không tìm thấy thông tin về bác sĩ đó.")

        dispatcher.utter_message(text=info)

        return []
