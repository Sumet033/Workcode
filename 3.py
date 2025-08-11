import flet as ft

def main(page: ft.Page):
    page.title = "ฟอร์มกรอกชื่อและเบอร์โทร"
    page.bgcolor = "#F8F9FA"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # ช่องกรอกข้อมูล
    name_input = ft.TextField(label="ชื่อ", width=300, border_radius=10)
    phone_input = ft.TextField(label="เบอร์โทร", width=300, border_radius=10)

    # ข้อความแสดงผล
    output_text = ft.Text(value="", size=16, color="green", text_align="center")

    # ฟังก์ชันเมื่อคลิกส่ง
    def handle_submit(e):
        name = name_input.value.strip()
        phone = phone_input.value.strip()

        if name and phone:
            output_text.value = f"✅ ชื่อ: {name}\n📞 เบอร์โทร: {phone}"
            output_text.color = "green"
        else:
            output_text.value = "⚠️ กรุณากรอกชื่อและเบอร์โทรให้ครบถ้วน"
            output_text.color = "red"
        page.update()

    # ปุ่มส่ง
    submit_button = ft.ElevatedButton(
        text="ยืนยันข้อมูล",
        on_click=handle_submit,
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10),
            padding=20,
        )
    )

    # Card ตกแต่งฟอร์ม
    form_card = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    ft.Text("📋 แบบฟอร์มลงชื่อ", size=20, weight="bold", text_align="center"),
                    name_input,
                    phone_input,
                    submit_button,
                    output_text
                ],
                spacing=20,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            padding=30,
            width=400,
            bgcolor="white",
            border_radius=15,
            shadow=ft.BoxShadow(blur_radius=20, color="#888888", offset=ft.Offset(2, 2)),
        )
    )

    page.add(form_card)

ft.app(target=main)
