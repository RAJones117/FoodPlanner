import sqlite3
import pandas as pd
import pyforms
from   pyforms          import BaseWidget
from   pyforms.controls import ControlText
from   pyforms.controls import ControlButton
from   pyforms.controls import ControlList

MealPlanQuery = 'SELECT DISTINCT RECIPE FROM RECIPES ORDER BY RANDOM() LIMIT 5'

MPConn = sqlite3.connect(r"./pythonsqlite.db")

c = MPConn.cursor()
mealies = pd.read_sql_query(MealPlanQuery, MPConn)

print(mealies)

meals = str(mealies.values).replace('\n',',').replace('[','').replace(']','')
GroceryQuery = 'SELECT Ingredient, SUM(amount), Unit from Recipes where recipe in ('+meals+') group by Ingredient, Unit'
print(GroceryQuery)

groces = pd.read_sql_query(GroceryQuery, MPConn)

print(groces)

class RecipeShuffle(BaseWidget):

    def __init__(self):
        super(RecipeShuffle,self).__init__('Recipe Shuffle')

        self.formset = [ {
        'Grocery List': ['_GroceryList'],
        'Meal Plan':['_Monday','||','_Mondaybutton','=','_Tuesday','||','_Tuesdaybutton','=','_Wednesday','||','_Wednesdaybutton','=','_Thursday','||','_Thursdaybutton','=','_Friday','||','_Fridaybutton','=','_confirmButton']
    } ]

        #Definition of the forms fields
        self._Monday     = ControlText('Monday')
        self._Monday.value = mealies.values[0][0]
        self._Mondaybutton        = ControlButton('Shuffle')
        self._Tuesday    = ControlText('Tuesday')
        self._Tuesday.value = mealies.values[1][0]
        self._Tuesdaybutton        = ControlButton('Shuffle')
        self._Wednesday      = ControlText('Wednesday')
        self._Wednesday.value = mealies.values[2][0]
        self._Wednesdaybutton        = ControlButton('Shuffle')
        self._Thursday      = ControlText('Thursday')
        self._Thursday.value = mealies.values[3][0]
        self._Thursdaybutton        = ControlButton('Shuffle')
        self._Friday      = ControlText('Friday')
        self._Friday.value = mealies.values[4][0]
        self._Fridaybutton        = ControlButton('Shuffle')

        self._confirmButton = ControlButton('Confirm')
        self._GroceryList = ControlList('')

        self._Mondaybutton.value = self.__mondayButtonAction
        self._Tuesdaybutton.value = self.__tuesdayButtonAction
        self._Wednesdaybutton.value = self.__wednesdayButtonAction
        self._Thursdaybutton.value = self.__thursdayButtonAction
        self._Fridaybutton.value = self.__fridayButtonAction
        self._confirmButton.value = self.__confirmButtonAction

        

    def __mondayButtonAction(self):
        ignoreList = (self._Monday.value, self._Tuesday.value, self._Wednesday.value, self._Thursday.value, self._Friday.value)
        query = f"SELECT RECIPE FROM RECIPES WHERE RECIPE NOT IN {ignoreList} ORDER BY RANDOM() LIMIT 1"
        dl = pd.read_sql_query(query, MPConn)
        self._Monday.value = dl.values[0][0]
    def __tuesdayButtonAction(self):
        ignoreList = (self._Monday.value, self._Tuesday.value, self._Wednesday.value, self._Thursday.value, self._Friday.value)
        query = f"SELECT RECIPE FROM RECIPES WHERE RECIPE NOT IN {ignoreList} ORDER BY RANDOM() LIMIT 1"
        dl = pd.read_sql_query(query, MPConn)
        self._Tuesday.value = dl.values[0][0]
    def __wednesdayButtonAction(self):
        ignoreList = (self._Monday.value, self._Tuesday.value, self._Wednesday.value, self._Thursday.value, self._Friday.value)
        query = f"SELECT RECIPE FROM RECIPES WHERE RECIPE NOT IN {ignoreList} ORDER BY RANDOM() LIMIT 1"
        dl = pd.read_sql_query(query, MPConn)
        self._Wednesday.value = dl.values[0][0]
    def __thursdayButtonAction(self):
        ignoreList = (self._Monday.value, self._Tuesday.value, self._Wednesday.value, self._Thursday.value, self._Friday.value)
        query = f"SELECT RECIPE FROM RECIPES WHERE RECIPE NOT IN {ignoreList} ORDER BY RANDOM() LIMIT 1"
        dl = pd.read_sql_query(query, MPConn)
        self._Thursday.value = dl.values[0][0]
    def __fridayButtonAction(self):
        ignoreList = (self._Monday.value, self._Tuesday.value, self._Wednesday.value, self._Thursday.value, self._Friday.value)
        query = f"SELECT RECIPE FROM RECIPES WHERE RECIPE NOT IN {ignoreList} ORDER BY RANDOM() LIMIT 1"
        dl = pd.read_sql_query(query, MPConn)
        self._Friday.value = dl.values[0][0]

    def __confirmButtonAction(self):
        mealList = (self._Monday.value, self._Tuesday.value, self._Wednesday.value, self._Thursday.value, self._Friday.value)
        GroceryQuery = f'SELECT Ingredient, SUM(amount) as amount, Unit from Recipes where recipe in {mealList} group by Ingredient, Unit ORDER BY AMOUNT DESC'
        groces = pd.read_sql_query(GroceryQuery, MPConn)
        self._GroceryList.css = "table, th, td{border: 1px solid;}"
        self._GroceryList.__add__(groces.columns)
        for row in groces.values:
            self._GroceryList.__add__(row)
        #self._GroceryList.value = groces

        
#TO DO
#Make meal plan default page
#make confirm button switch to grocery list
        





        


#Execute the application
if __name__ == "__main__":   pyforms.start_app( RecipeShuffle )