from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivy.uix.textinput import TextInput

class Conteiner(BoxLayout):
    def table( self, item ):
        self.lenn = len(Case.dict_name)
        self.tables.clear_widgets( )
        self.it_for_calc_doc = iter( Case.dict_doc )
        self.it_for_calc_sklad = iter( Case.dict_sklad )
        self.it_name = iter( Case.dict_name )
        self.it_doc = iter( Case.dict_doc )
        self.it_sklad = iter( Case.dict_sklad )
        self.tables.add_widget(
            ItemTable(
                name = str( "Наименование" ),
                base = str( "Документально" ),
                stock = str( "На складе" ),
                write = str( "Подлежит списанию" )
            )
        )


        for i in range(self.lenn):

            self.tables.add_widget(
                ItemTable(
                    name = str( Case.name( self ) ),
                    base = str( Case.doc( self ) ),
                    stock =str(Case.sklad( self )),
                    write = str(Case.calc( self )),
                    butts = str("Изменить"),
                    itemes = str(i+1)
                    )
            )



    def text_input( self):

        self.text_fild.clear_widgets()
        self.text_inputs1 =MDTextField(
            pos_hint= { "center_y": .2 },
            text= "Наименование"
        )
        self.text_inputs2 = MDTextField(
            pos_hint = { "center_y": .6 },
            text = "Документально"
        )
        self.text_inputs3 = MDTextField(
            pos_hint = { "center_y": .4 },
            text = "На складе"
        )
        self.text_fild.add_widget(
            self.text_inputs1
        )
        self.text_fild.add_widget(
            self.text_inputs2
        )
        self.text_fild.add_widget(
            self.text_inputs3
        )
        self.text_fild.add_widget(
            Button(
                size_hint_y = None,
                text= "Добавить",
                padding= "40dp",
                height= dp(30),


                on_press = self.appendes
            )
        )

    def on_text( self, instance, value ):
        self.on_text.text = print( self.on_text )
    def appendes( self, instance ):
        Case.dict_name.append(self.text_inputs1.text)
        Case.dict_doc.append( self.text_inputs2.text )
        Case.dict_sklad.append( self.text_inputs3.text )


    def text_del( self ):



        self.text_fild1.clear_widgets()
        self.text_inputs4 = MDTextField(
            pos_hint = { "center_y": .4 },
            text = "Наимнование"

        )
        self.text_fild1.add_widget(
            self.text_inputs4
        )
        self.text_fild1.add_widget(
            Button(
                size_hint_y = None,
                text = "Удалить",
                padding = "40dp",
                height = dp( 30 ),
                on_press = self.dell


            )
        )
    def dell( self, *args ):

        if self.text_inputs4.text in Case.dict_name:
            index = Case.dict_name.index(self.text_inputs4.text)
            del Case.dict_name[index]
            del Case.dict_doc[ index ]
            del Case.dict_sklad[index]
        else:
            self.text_inputs4.text = "Такого наименования нету"

    def edit_text( self, *args ):
        self.text_fild2.clear_widgets( )
        self.text_inputs8 = MDTextField(
            pos_hint = { "center_y": .2 },
            text = "Наименование старое"
        )
        self.text_inputs5 = MDTextField(
            pos_hint = { "center_y": .8 },
            text = "Наименование новое"
        )
        self.text_inputs6 = MDTextField(
            pos_hint = { "center_y": .6 },
            text = "Документально"
        )
        self.text_inputs7 = MDTextField(
            pos_hint = { "center_y": .4 },
            text = "На складе"
        )
        self.text_fild2.add_widget(
            self.text_inputs8
        )
        self.text_fild2.add_widget(
            self.text_inputs5
        )
        self.text_fild2.add_widget(
            self.text_inputs6
        )
        self.text_fild2.add_widget(
            self.text_inputs7
        )
        self.text_fild2.add_widget(
            Button(
                size_hint_y = None,
                text = "Изменить",
                padding = "40dp",
                height = dp( 30 ),

                on_press = self.dell
            )
        )
    def dell(self, *args):

        if self.text_inputs8.text in Case.dict_name:
            index = Case.dict_name.index( self.text_inputs8.text )
            Case.dict_name[index] = self.text_inputs5.text
            Case.dict_doc[index] = self.text_inputs6.text
            Case.dict_sklad[index] = self.text_inputs7.text


        else:
            self.text_inputs8.text = "Такого наименования нету"





















class ManipulationText(MDRelativeLayout):

    qwe = None





class ItemTable( BoxLayout):
    itemes = StringProperty()

    butts = StringProperty()
    name = StringProperty( )
    base = StringProperty( )
    stock = StringProperty( )
    write = StringProperty( )
    def find( self, item):
        print(item)
        if item == str(2):

            self.mdists.add_widget(
                clean(

                )
            )
class clean(BoxLayout):
    qwe = None


class Case:
    dict_name = []
    dict_doc = []
    dict_sklad = []

    x = ""
    def sklad( self, *args ):
        item = next( self.it_sklad )
        return item
    def doc( self, *args ):
        item = next( self.it_doc )
        return item

    def name( self, *args ):
        item = next( self.it_name)
        return item
    def calc( self, *args ):
        item = int(next(self.it_for_calc_doc)) - int(next(self.it_for_calc_sklad))
        return item



class BarAPP( MDApp ):

    def build( self ):
        self.theme_cls.material_style = "M3"
        self.theme_cls.theme_style = "Dark"

        return Conteiner( )


if __name__ == "__main__":
    BarAPP( ).run( )