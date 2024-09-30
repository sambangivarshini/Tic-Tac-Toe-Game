import tkinter as tk
from PIL import Image, ImageTk  

# All my functions are written below

def checkifxwon():
    if(board[0]==board[1]) and (board[1]==board[2]) and (board[2]==1):
        xwon()
        return True
    elif(board[3]==board[4]) and (board[4]==board[5]) and (board[5]==1):
        xwon()
        return True
    elif(board[6]==board[7]) and (board[7]==board[8]) and (board[8]==1):
        xwon()
        return True
    elif(board[0]==board[3]) and (board[3]==board[6]) and (board[6]==1):
        xwon()
        return True
    elif(board[1]==board[4]) and (board[4]==board[7]) and (board[7]==1):
        xwon()
        return True
    elif(board[2]==board[5]) and (board[5]==board[8]) and (board[8]==1):
        xwon()
        return True
    elif(board[0]==board[4]) and (board[4]==board[8]) and (board[8]==1):
        xwon()
        return True
    elif(board[2]==board[4]) and (board[4]==board[6]) and (board[6]==1):
        xwon()
        return True
    return False
    
    
def checkifywon():
    if(board[0]==board[1]) and (board[1]==board[2]) and (board[2]==0):
        owon()
        return True
    elif(board[3]==board[4]) and (board[4]==board[5]) and (board[5]==0):
        owon()
        return True
    elif(board[6]==board[7]) and (board[7]==board[8]) and (board[8]==0):
        owon()
        return True
    elif(board[0]==board[3]) and (board[3]==board[6]) and (board[6]==0):
        owon()
        return True
    elif(board[1]==board[4]) and (board[4]==board[7]) and (board[7]==0):
        owon()
        return True
    elif(board[2]==board[5]) and (board[5]==board[8]) and (board[8]==0):
        owon()
        return True
    elif(board[0]==board[4]) and (board[4]==board[8]) and (board[8]==0):
        owon()
        return True
    elif(board[2]==board[4]) and (board[4]==board[6]) and (board[6]==0):
        owon()
        return True
    return False

def xwon():
    # Background image needs to be placed first
    bg_image = Image.open("draw.jpg")  
    bg_image = bg_image.resize((612, 344)) 
    global bg_image_tk2
    bg_image_tk2 = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(mainscreen, image=bg_image_tk2)
    background_label.place(x=61.2, y=0, relwidth=0.8, relheight=1)
    
    win_frame = tk.Frame(mainscreen)
    win_frame.place(relx=0.5, rely=0.5, anchor='center')

    win_label = tk.Label(win_frame, text="Player X Wins!", font=("Arial", 24))
    win_label.pack(pady=10)

    replay_button = tk.Button(win_frame, text="Replay", command=game_screen)
    replay_button.pack(side='left', padx=10)

    close_button = tk.Button(win_frame, text="Close", command=mainscreen.destroy)
    close_button.pack(side='right', padx=10)

def owon():
    # Background image needs to be placed first
    bg_image = Image.open("draw.jpg")  
    bg_image = bg_image.resize((612, 344)) 
    global bg_image_tk2
    bg_image_tk2 = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(mainscreen, image=bg_image_tk2)
    background_label.place(x=61.2, y=0, relwidth=0.8, relheight=1)
    
    win_frame = tk.Frame(mainscreen)
    win_frame.place(relx=0.5, rely=0.5, anchor='center')

    win_label = tk.Label(win_frame, text="Player O Wins!", font=("Arial", 24))
    win_label.pack(pady=10)

    replay_button = tk.Button(win_frame, text="Replay", command=game_screen)
    replay_button.pack(side='left', padx=10)

    close_button = tk.Button(win_frame, text="Close", command=mainscreen.destroy)
    close_button.pack(side='right', padx=10)

def gametie():
    # Background image needs to be placed first
    bg_image = Image.open("draw.jpg")  
    bg_image = bg_image.resize((612, 344)) 
    global bg_image_tk2
    bg_image_tk2 = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(mainscreen, image=bg_image_tk2)
    background_label.place(x=61.2, y=0, relwidth=0.8, relheight=1)   
    
    tie_frame = tk.Frame(mainscreen)
    tie_frame.place(relx=0.5, rely=0.5, anchor='center')

    tie_label = tk.Label(tie_frame, text="It's a Tie!", font=("Arial", 24))
    tie_label.pack(pady=10)

    replay_button = tk.Button(tie_frame, text="Replay", command=game_screen)
    replay_button.pack(side='left', padx=10)

    close_button = tk.Button(tie_frame, text="Close", command=mainscreen.destroy)
    close_button.pack(side='right', padx=10)


# This function marks X or O depending on whose chance
def markit(button_id):
    global chance
    victory = False
    if buttons[button_id - 1]['text'] == "":
        if chance % 2 == 1:
            buttons[button_id - 1].config(text="X")
            board[button_id - 1]=1
            victory = checkifxwon()
        else:
            buttons[button_id - 1].config(text="O")
            board[button_id - 1]=0
            victory = checkifywon()
        
        chance += 1
        if(victory==False): 
            update_heading()
        if(chance==10):
            gametie()


def update_heading():
    if chance % 2 == 1:
        heading_label.config(text="Player X's Turn")
    else:
        heading_label.config(text="Player O's Turn")


# Playing screen
def game_screen():
    global buttons, heading_label  # Declare buttons as global to access in markit
    
    # Background image needs to be placed first
    bg_image = Image.open("game.jpg")  
    bg_image = bg_image.resize((300, 344)) 
    global bg_image_tk2
    bg_image_tk2 = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(mainscreen, image=bg_image_tk2)
    background_label.place(x=61.2, y=0, relwidth=0.8, relheight=1)   

    close_button = tk.Button(mainscreen, text="Close", command=mainscreen.destroy)
    close_button.place(x=280, y=300)
    
    global chance, board
    chance = 1  # Initialize chance (1 for Player X, 2 for Player O)
    board=[-1,-1,-1,-1,-1,-1,-1,-1,-1]
    
    # Player heading
    heading_label = tk.Label(mainscreen, text="Player X's Turn", font=("Arial", 16))
    heading_label.place(x=240, y=0)

    # The game clicks
    buttons = []
    positions = [
        (206/612, 28.5/344), (276.5/612, 28.5/344), (347/612, 28.5/344),
        (206/612, 84/344), (276.5/612, 84/344), (347/612, 84/344),
        (206/612, 140/344), (276.5/612, 140/344), (347/612, 140/344)
    ]

    for i, pos in enumerate(positions):
        button = tk.Button(mainscreen, text="", command=lambda i=i: markit(i + 1), bg='lightblue', activebackground="lightblue", bd=0)
        button.place(relx=pos[0], rely=pos[1], relwidth=67/612, relheight=53/344)
        buttons.append(button)


# Function to save player names
def save_names():
    player1_name = player1_entry.get()
    player2_name = player2_entry.get()
    print(f"Player 1: {player1_name}, Player 2: {player2_name}")
    # You can save the names to a file or a database
    with open("player_names.txt", "w") as file:
        file.write(f"Player 1: {player1_name}\n")
        file.write(f"Player 2: {player2_name}\n")
        
    # Background image needs to be placed first
    bg_image = Image.open("game_starts.jpeg")  
    bg_image = bg_image.resize((612, 344)) 
    global bg_image_tk2
    bg_image_tk2 = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(mainscreen, image=bg_image_tk2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    game_screen()        
    
            
# This function for 2 player input window
def player_name_input():
    # Background image needs to be placed first
    bg_image = Image.open("players12.jpg")  
    bg_image = bg_image.resize((612, 344)) 
    global bg_image_tk2
    bg_image_tk2 = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(mainscreen, image=bg_image_tk2)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    heading = tk.Label(mainscreen, text="Let us Begin the feast;)", font=("Arial", 16))
    heading2 = tk.Label(mainscreen, text="Enter your names:", font=("Arial", 16))
    heading.place(x=200, y=0)
    heading2.place(x=220,y=75)

    quitbutton = tk.Button(mainscreen, text="Close", command=mainscreen.destroy)
    quitbutton.place(x=270, y=300)
    
    # Taking input values of names here
    global player1_entry, player2_entry
    player1_entry = tk.Entry(mainscreen,bg="yellow", fg="blue")
    player1_entry.place(x=80, y=200)
    player2_entry = tk.Entry(mainscreen,bg="yellow", fg="blue")
    player2_entry.place(x=400, y=200)
    
    # Save button to save names and starts the game
    save_button = tk.Button(mainscreen, text="Start Game", command=save_names)
    save_button.place(x=270, y=250)


# Functon for start screen
def start_screen():
    global mainscreen, bg_image_tk1, heading
    mainscreen = tk.Tk()
    mainscreen.geometry("612x344")
    mainscreen.title("Tic-Tac-Toe")

    bg_image = Image.open("startpage.jpg")  
    bg_image = bg_image.resize((612, 344)) 
    bg_image_tk1 = ImageTk.PhotoImage(bg_image)
    background_label = tk.Label(mainscreen, image=bg_image_tk1)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    heading = tk.Label(mainscreen, text="Welcome to Tic-Tac-Toe", bg='lightgrey', font=("Arial", 16))
    heading.place(x=200, y=0)

    playbutton = tk.Button(mainscreen, text='Play', width=25, activebackground="blue", activeforeground="white", command=player_name_input)
    playbutton.place(x=320, y=100)

    quitbutton = tk.Button(mainscreen, text="Quit", width=25, command=mainscreen.destroy, activebackground="blue", activeforeground="white")
    quitbutton.place(x=320, y=200)


# My infinite main looooooop
start_screen()
mainscreen.mainloop()
