import flet as ft

def main(page: ft.Page):
    page.title = "📮 Formulário de Contato"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.START

    txt_nome  = ft.TextField(label="Nome",    width=300)
    txt_email = ft.TextField(label="Email",   width=300)
    txt_msg   = ft.TextField(label="Mensagem", multiline=True, width=300, height=100)
    txt_conf  = ft.Text()

    def enviar(e):
        nome  = txt_nome.value.strip()
        email = txt_email.value.strip()
        msg   = txt_msg.value.strip()
        if not nome or not email or not msg:
            txt_conf.value = "❗ Por favor, preencha todos os campos."
        else:
            txt_conf.value = f"✅ Obrigado, {nome}! Sua mensagem foi enviada."
            txt_nome.value = txt_email.value = txt_msg.value = ""
        page.update()

    btn = ft.ElevatedButton("Enviar", on_click=enviar)

    page.add(
        ft.Text("Formulário de Contato", style="headlineMedium"),
        txt_nome, txt_email, txt_msg, btn, txt_conf
    )

ft.app(target=main)
