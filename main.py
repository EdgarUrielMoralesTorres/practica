import flet as ft

TEST = "admin@gmail.com"
TEST1 = "1234"

def main(page: ft.Page):
    page.title = "Practica"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    titulo = ft.Text("Iniciar Sesion", size=30)

    corr = ft.TextField(
        label="Ingresar el correo del usuario ",
        hint_text="correo",
        border=ft.InputBorder.NONE,
        margin=ft.Margin(top=15),
        value="",
        icon=ft.Icons.EMAIL
    )

    cont = ft.TextField(
        label="Ingresa la contraseña",
        hint_text="Contraseña",
        border=ft.InputBorder.NONE,
        value="",
        password=True,
        can_reveal_password=True,
        margin=ft.Margin(top=15),
        icon=ft.Icons.PASSWORD
    )

    


    def cell(e):
        ale.open = False
        page.update()

    ale = ft.AlertDialog(
        title=ft.Text("Error"),
        content=ft.Text("Tus datos son incorrectos"),
        actions=[
            ft.TextButton("Cerrar", on_click=cell)
        ]
    )
    
    
    menCo = ft.Text("Correo para recuperar enviado",
        color=ft.Colors.WHITE,
        bgcolor=ft.Colors.BLACK,
        visible=False
    )
    
    def mosMen(e):
        menCo.visible = True
        page.update()

    def cam(e):
        print("donde andas:", e.control.selected_index)

    barra = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.GPS_FIXED, label="Explorar"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ],
        on_change=cam
    )

    def entrar(e):
        usuario = corr.value
        contra = cont.value

        if usuario == TEST and contra == TEST1:

            page.clean()

            bienvenida = ft.Text(
                "Pantalla de inicio",
                size=30,
                weight=ft.FontWeight.BOLD
            )
            
            sub = ft.Text(
                "erasing me, erasing you",
                size=15,
                color=ft.Colors.RED,
                weight=ft.FontWeight.BOLD
            )

            page.navigation_bar = barra
            page.add(bienvenida,
                     sub)

        else:
            page.dialog = ale
            ale.open = True

        page.update()

    bot = ft.Button(
        content="Iniciar",
        bgcolor=ft.Colors.BLACK,
        color=ft.Colors.WHITE,
        on_click=entrar
    )

    olv = ft.TextButton(
        content="Olvidaste la contraseña?",
        margin=ft.Margin(top=15),
        on_click=mosMen
    )

    page.add(
        titulo,
        corr,
        cont,
        olv,
        bot,
        menCo,
        ale
    )

ft.run(main)
