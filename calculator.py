import flet
from flet import (
    Page,
    TextField,
    ElevatedButton,
    Row,
    Column,
    Colors,
    MainAxisAlignment,
    CrossAxisAlignment,
    RoundedRectangleBorder,
    border,
)

def main(page: Page):
    # --- Window setup ---
    page.title               = "Flet Calculator"
    page.window_resizable    = True
    page.window_min_width    = 300
    page.window_min_height   = 500
    page.bgcolor             = Colors.WHITE
    page.vertical_alignment   = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER

    # --- Display ---
    WIDTH = 280          # ความกว้างคงที่สำหรับ display และกริดปุ่ม
    display = TextField(
        value="0",
        read_only=True,
        width=WIDTH,
        height=80,
        expand=False,
        text_align="right",
        text_style={"font_size": 40},
        border=border.all(1, Colors.GREY_400),
        border_radius=8,
    )
    error = False

    def format_result(x):
        s = str(x)
        return s.replace(".", ",") if "." in s else s

    def update(val: str):
        nonlocal error
        display.value = val
        error = (val == "Error")
        page.update()

    def button_click(e):
        lbl = e.control.data
        v = display.value

        if lbl == "C":
            update("0"); return

        if lbl in ("+/-", "%"):
            try:
                num = float(v.replace(",", "."))
                res = -num if lbl == "+/-" else num/100
                update(format_result(res))
            except:
                update("0")
            return

        if lbl == "=":
            try:
                expr = (
                    v.replace(",", ".")
                     .replace("×", "*")
                     .replace("÷", "/")
                     .replace("−", "-")
                )
                res = eval(expr)
                update(format_result(res))
            except:
                update("Error")
            return

        # ต่อท้ายตัวเลข/จุลภาค/เครื่องหมาย
        if error or v == "0":
            v = ""
        if lbl == "," and "," in v:
            return
        v += lbl
        update(v)

    # --- Buttons config (4 คอลัมน์) ---
    btn_cfg = [
        [("C", Colors.GREY_200), ("+/-", Colors.GREY_200), ("%", Colors.GREY_200), ("÷", Colors.ORANGE_300)],
        [("7", Colors.GREY_100), ("8", Colors.GREY_100), ("9", Colors.GREY_100), ("×", Colors.ORANGE_300)],
        [("4", Colors.GREY_100), ("5", Colors.GREY_100), ("6", Colors.GREY_100), ("−", Colors.ORANGE_300)],
        [("1", Colors.GREY_100), ("2", Colors.GREY_100), ("3", Colors.GREY_100), ("+", Colors.ORANGE_300)],
        [("0", Colors.GREY_100), (",", Colors.GREY_100), ("=", Colors.ORANGE_300)],
    ]

    rows = []
    for row in btn_cfg:
        cells = []
        for lbl, bg in row:
            w = WIDTH/2 if lbl == "0" else WIDTH/4 - 8   # ปุ่ม 0 กินสองช่อง
            cells.append(
                ElevatedButton(
                    lbl,
                    data=lbl,
                    width=w,
                    height=60,
                    bgcolor=bg,
                    color=Colors.BLACK,
                    scale=RoundedRectangleBorder(radius=30),
                    on_click=button_click,
                    elevation=0,
                )
            )
        rows.append(Row(
            cells,
            alignment=MainAxisAlignment.CENTER,
            spacing=8
        ))

    # --- รวม display + ปุ่ม ใน Column เดียว จัดกึ่งกลางแนวตั้งและแนวนอน ---
    page.add(
        Column(
            [display] + rows,
            spacing=12,
            alignment=MainAxisAlignment.CENTER,        # จัดแนวตั้ง กึ่งกลาง
            horizontal_alignment=CrossAxisAlignment.CENTER,  # จัดแนวนอน กึ่งกลาง
            expand=False,
        )
    )

flet.app(target=main)
