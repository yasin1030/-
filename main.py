import flet as ft

def main(page: ft.Page):
    # تنظیمات اولیه صفحه
    page.title = "محاسبه‌گر ابجد"
    page.scroll = "adaptive"  # اگر جدول طولانی شد، صفحه اسکرول بخورد

    # دیکشنری ابجد
    abjad_table = {
        'ا': 1, 'إ': 1, 'أ': 1, 'ء': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ؤ': 6, 'ز': 7, 'ح': 8, 'ط': 9,
        'ی': 10, 'ک': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80,
        'ص': 90, 'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600,
        'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000, 'گ': 20, 'ژ': 7, 'پ': 2, 'چ': 3, 'ئ':10, 'ة':400
    }

    input_text = ft.TextField(label="کلمه خود را وارد کنید")
    result_text = ft.Text(value="مقدار نهایی: 0", size=20, weight="bold")

    # ساختار جدول (ستون‌ها)
    data_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("حرف")),
            ft.DataColumn(ft.Text("مقدار")),
        ],
        rows=[] # ردیف‌ها فعلاً خالی هستند
    )

    def calculate(e):
        word = input_text.value
        total = 0
        
        # پاک کردن جدول قبلی برای محاسبه جدید
        data_table.rows.clear()

        # حلقه برای خواندن حروف و پر کردن جدول
        for char in word:
            value = abjad_table.get(char, 0)
            total += value
            
            # اضافه کردن سطر جدید به جدول
            data_table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(char)),
                    ft.DataCell(ft.Text(str(value))),
                ])
            )

        result_text.value = f"مقدار نهایی: {total}"
        page.update() # صفحه را به‌روزرسانی کن تا تغییرات اعمال شود

    page.add(input_text, ft.ElevatedButton("محاسبه", on_click=calculate), result_text, data_table)

ft.app(target=main)
