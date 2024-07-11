import justpy as jp
import layout

class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the home page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""Hi this is an introduction """, classes="text-lg")
        return wp
