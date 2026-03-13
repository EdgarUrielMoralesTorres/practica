import flet as ft

TEST = "admin@gmail.com"
TEST1 = "1234"

def main(page: ft.Page):
    page.title = "Practica"
    titulo=ft.Text("Iniciar Sesion", size=30)
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER
    
    corr=ft.TextField(
        label="Ingresar el correo del usuario ",
        hint_text="correo",
        border=ft.InputBorder.NONE,
        margin=ft.Margin(top=15),
        value="",
        icon=ft.Icons.EMAIL
        )
    
    cont=ft.TextField(
        label="Ingresa la contraseña",
        hint_text="Contraseña",
        border=ft.InputBorder.NONE,
        value="",
        password=True,
        can_reveal_password=True,
        margin=ft.Margin(top=15),
        icon=ft.Icons.PASSWORD
        )

    mensaje_texto = ft.Text("")
    
    mensaje = ft.Container(
        content=mensaje_texto,
        bgcolor=ft.Colors.TRANSPARENT,
        padding=10,
        margin=ft.Margin(top=15),
    )
    
    def entrar(e):
        usuario=corr.value
        contra=cont.value
        
        if usuario==TEST and contra==TEST1:
            mensaje_texto.value="Correcto"
            mensaje_texto.color=ft.Colors.WHITE
            mensaje.bgcolor=ft.Colors.GREEN
        else:
            mensaje_texto.value="Algo anda mal"
            mensaje_texto.color=ft.Colors.WHITE
            mensaje.bgcolor=ft.Colors.RED
        
        page.update()
    
    bot = ft.Button(
        content="Iniciar",
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        on_click=entrar
    )
    
    olv=ft.TextButton(
        content="Olvidastes la contraseña?",
        margin=ft.Margin(top=15),
    )
    
    
    barra=ft.NavigationBar(
    destinations=[
        ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
        ft.NavigationBarDestination(icon=ft.Icons.GPS_FIXED , label="Explorar"),
        ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
    ],
)

    page.add(
        titulo,
        corr,
        cont,
        olv,
        bot,
        mensaje,
        barra
    )

ft.run(main)
