import justpy as jp
import layout
class About:
    path="/about"

    def serve(self):
        wp=jp.QuasarPage(tailwind=True)
        lay=layout.DefaultLayout(a=wp)
        container=jp.QPageContainer(a=lay)
        div=jp.Div(a=container,classes="bg-gray-200 h-screen")
        jp.Div(a=div,text="This is the about page!",classes="text-4xl m-2")
        jp.Div(a=div,text="""Hi this is an introduction """,classes="text-lg")
        return wp
