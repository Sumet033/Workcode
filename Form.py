import flet
import os
import csv
from flet import (
    Page,
    TextField,
    ElevatedButton,
    Column,
    Text,
    Container,
    Colors,
    border_radius,
    BoxShadow,
)

def main(page: Page):
    # ตั้งค่าหน้า
    page.title = "ฟอร์มรับสมัคร"
    page.window_width = 500
    page.window_height = 400
    page.padding = 0
    page.bgcolor = Colors.BLUE_GREY_50
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    # ฟิลด์กรอกข้อมูล
    name_field = TextField(
        label="ชื่อ-สกุล",
        width=350,
        text_style={"size": 16},
        border_color=Colors.BLUE_GREY_200,
        focused_border_color=Colors.BLUE_300,
        label_style={"color": Colors.BLACK},
    )
    phone_field = TextField(
        label="หมายเลขโทรศัพท์",
        width=350,
        keyboard_type="phone",
        text_style={"size": 16},
        border_color=Colors.BLUE_GREY_200,
        focused_border_color=Colors.BLUE_300,
    )
    team_field = TextField(
        label="ชื่อทีม",
        width=350,
        text_style={"size": 16},
        border_color=Colors.BLUE_GREY_200,
        focused_border_color=Colors.BLUE_300,
    )
    status = Text(value="", size=14, color=Colors.RED_700)

    # ฟังก์ชันบันทึก CSV
    def save_csv(e):
        name = name_field.value.strip()
        phone = phone_field.value.strip()
        team = team_field.value.strip()

        if not name or not phone or not team:
            status.value = "❗ กรุณากรอกข้อมูลให้ครบทุกช่อง"
            page.update()
            return

        filename = "registration.csv"
        file_exists = os.path.isfile(filename)

        with open(filename, mode="a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            if not file_exists:
                writer.writerow(["ชื่อ-สกุล", "หมายเลขโทรศัพท์", "ชื่อทีม"])
            writer.writerow([name, phone, team])

        status.value = f"✅ บันทึกสำเร็จ ({filename})"
        name_field.value = ""
        phone_field.value = ""
        team_field.value = ""
        page.update()

    # ปุ่มบันทึกตกแต่ง
    save_button = ElevatedButton(
        text="บันทึกข้อมูล",
        on_click=save_csv,
        width=200,
        height=45,
    )

    # กล่องฟอร์มหลัก
    form_card = Container(
        content=Column(
            controls=[
                Text("แบบฟอร์มรับสมัคร", size=24, weight="bold", color=Colors.BLUE_800),
                name_field,
                phone_field,
                team_field,
                save_button,
                status,
            ],
            alignment="center",
            tight=True,
            spacing=15,
        ),
        padding=20,
        bgcolor=Colors.WHITE,
        border_radius=border_radius.all(10),
        shadow=BoxShadow(
            color=Colors.BLACK26, blur_radius=8, offset=(0, 4)
        ),
        width=400,
    )

    page.add(form_card)

import os
import csv
from flet import BoxShadow

flet.app(target=main, view=flet.WEB_BROWSER)
