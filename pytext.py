#importing libraries

import wikipedia
import pyttsx3
from flet import (
            FilledButton,
            TextField,
            Page,
            app,
            Text,
            alignment,
            colors,
            Image,
            ScrollMode,
            Container,
            IconButton,
            Row,
            FloatingActionButton
            )

#creating page in flet library

def main(page:Page):
    #styling page
    page.title = "adipedia"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"
    page.window_bgcolor = "black"
    page.bgcolor=colors.BLUE_600
    page.scroll=ScrollMode.ALWAYS

    #importing logo image
    img = Image(
         src="/photos/ak_logo.png",
        #styling image
         border_radius= 90,
         opacity=0.92
        )
    
    #creating search bar in page
    search = TextField(
        label="Enter here! That you want to know",
        color="black",
        icon="search",
        width=700
        )
    
    #creating title of app
    title = Text(
         #styling title
        value="Welcome to ADIPEDIA",
        text_align=alignment.top_center,
        size=50,
        color="black",
        weight=20,
        semantics_label= "aditya's wikipedia" 
        )
    
    #creating a function of search and speech named wiki
    def wiki(e):
        #importing speech function
        engine = pyttsx3.init()
        #changing the voice of computer
        voices = engine.getProperty("voices")
        engine.setProperty('voice',voices[1].id)

        #creating text to speech function
        s = "say"       
        if s in search.value:
                engine.say(search.value[3:])
                engine.runAndWait()          
            

        else:
            try:
                if search.value == "pass code":
                    engine.say("11111100111")
                    engine.runAndWait()
                else:
                    result = wikipedia.summary(search.value, sentences = 4)
                    rtext = Container(
                        Text(
                            "Question: "+search.value+":\nAnswer: "+result,
                            color="black",
                            size=20
                        ),               
                        bgcolor=colors.BLUE_300,
                        margin=10,
                        border_radius=4
                    )
         
                    page.add(rtext)
                    page.update()

                    engine.say(result)
                    engine.runAndWait()
            
            except:
                engine.say("Sorry,i don't know.please ask another thing to me")
                engine.runAndWait()

        Text(
        value="Welcome to ADIPEDIA",
        text_align=alignment.top_center,
        size=50,
        color="black",
        weight=20
        )      

    
    
    btn=FilledButton(

        text="Search Now",
        on_click=lambda e:wiki(e),
        height=60,
        width=230,

        )
    def clear(e):
        search.value = ""
        page.update()
    
    clsbtn= IconButton(
        icon="clear",
        on_click=lambda e:clear(e),
        )
    

    
    

    page.add(
        img,
        title,
        Row(
         controls=[
            search,
            clsbtn
            ],
            alignment="center"
        ),
        
        btn,

    )

app(target=main)
