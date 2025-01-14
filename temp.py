   #(version 1.0.0)
import dash             #(version 1.9.1) pip install dash==1.9.1
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests
import dash_bootstrap_components as dbc
import base64
import dash_table
import pandas as pd  


colors = {
    'background': '#007D99'}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
server = app.server

image_filename_1 = 'pinfo.jpeg'
image_filename_2 = 'resultt.jpeg'
encoded_image_1 = base64.b64encode(open(image_filename_1, 'rb').read())
encoded_image_2 = base64.b64encode(open(image_filename_2, 'rb').read())

image_filename_3= 'Hnet.com-image (1).png' # replace with your own image
encoded_image_3 = base64.b64encode(open(image_filename_3, 'rb').read())



#-------------------------style_header ={ 'border': '1px solid green' },

categories=["id","name"]

#def kick_Ace():
kick_requests = requests.get(
        "http://backend-test.northeurope.azurecontainer.io:4001/games?orderBy=name_ASC&limit=15"
    )
    
    
json_data = kick_requests.json()
df = pd.DataFrame(json_data)
data = []
for index, row in df.iterrows():
        id = row['id']
        url = f'http://backend-test.northeurope.azurecontainer.io:4001/game/{id}?orderBy=points_ASC&limit=15'
        response = requests.get(url)
        game_request = response.json()
        game_users_list = game_request['gameUsers']
        if len(game_users_list) > 0:
            game_users_data = []
            for item in game_users_list:
                game_users = []
                game_users.append(item['id'])
                game_users.append(item['shotsCount'])
                game_users.append(item['missedShotsCount'])
                game_users.append(item['hasNextShot'])
                game_users.append(item['user']['id'])
                game_users.append(item['user']['role'])
                game_users.append(item['user']['avatar'])
                game_users.append(item['user']['email'])
                game_users_data.append(game_users)
        
            result = pd.DataFrame(game_users_data)
            result['name'] = game_request['name']
            result.columns = ['name', 'game_user_id', 'shots_count', 
                              'missed_shots_count', 'has_next_shot', 
                              'id', 'role', 'avatar', 'email']
            
            data.append(rresultesult)
            
        else:
            pass
categories=["id","name"]

#def kick_Ace():
kick_requests = requests.get(
        "http://backend-test.northeurope.azurecontainer.io:4001/games?orderBy=name_ASC&limit=15"
    )
    
    
json_data = kick_requests.json()
df = pd.DataFrame(json_data)
data = []
for index, row in df.iterrows():
        id = row['id']
        url = f'http://backend-test.northeurope.azurecontainer.io:4001/game/{id}?orderBy=points_ASC&limit=15'
        response = requests.get(url)
        game_request = response.json()
        game_users_list = game_request['gameUsers']
        if len(game_users_list) > 0:
            game_users_data = []
            for item in game_users_list:
                game_users = []
                
                game_users.append(item['hasNextShot'])
                        
            result1 = pd.DataFrame(game_users_data)
            result1['name'] = game_request['name']
            result1.columns = ['has_next_shot']
            
            data.append(result1)
            
        else:
            pass
    
            
#-------------------------------------------------------------------------------

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.Header(children='', style={'textAlign': 'center', 'backgroundcolor': '#004d4d','font-weight': 'bold'} ), 
    
    html.Div([
    html.Img(src='data:Hnet.com-image (1)/png;base64,{}'.format(encoded_image_3.decode())
                    
)]),
    
    
    html.Div(children='''
             Explore your skills.
             ''', style={'color': 'white', 'font-weight': 'bold'}),
dbc.CardDeck( 
[              
     dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Video ",style={'color': 'white', 'font-weight': 'bold'}, className=""),
                    html.P(
                        "See recorded video here",style={'color': 'white', 'font-weight': 'bold'},
                        className="",
                    ),html.Iframe(src="https://www.youtube.com/embed/OQ2qYyZlqu0",
                style={"height": "500px", "width": "100%"}) 

                ]
                                  
                                  
            )
        ),
      dbc.Card(
            dbc.CardBody(
                
        
               
                  html.Div(children= dash_table.DataTable(
                        data=df.to_dict('records'), 
                        columns=[{"name": i, "id": i} for i in result1.columns],
                        
                        style_header={ 'backgroundColor': 'rgb(0, 125, 153)','border': '1px solid green' },
                        style_data={ 'border': '1px solid green' }, 
                        style_cell={
                            'backgroundColor': 'rgb(0, 125, 153)',
                            'color': 'white',
                            'textAlign': 'left',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            },
                        style_table={'overflowX': 'auto'},
              )
                                  
                                 
            )
      ) ),
             
dbc.Card(
            dbc.CardBody(
                [
                    html.H5("Results ",style={'color': 'white', 'font-weight': 'bold'}, className=""),
                    html.P(
                        "See results here",style={'color': 'white', 'font-weight': 'bold'},
                        className="",
                    ),
                    html.Div(children= dash_table.DataTable(
                        data=df.to_dict('records'), 
                        columns=[{"name": i, "id": i} for i in result.columns],
                        
                        style_header={ 'backgroundColor': 'rgb(0, 125, 153)','border': '1px solid green' },
                        style_data={ 'border': '1px solid green' }, 
                        style_cell={
                            'backgroundColor': 'rgb(0, 125, 153)',
                            'color': 'white',
                            'textAlign': 'left',
                            'whiteSpace': 'normal',
                            'height': 'auto',
                            },
                        style_table={'overflowX': 'auto'},
)
        )
     ])
     )
      
    ])
   ])        

#-------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)