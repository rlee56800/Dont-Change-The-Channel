import tkinter

##################################################################################
# Code for remote
remote = tkinter.Tk(className = "Remote")

remote_canvas = tkinter.Canvas(remote)

up_img = tkinter.PhotoImage(master = remote_canvas, file = r'RemoteAssets/btn_up.png')
up = tkinter.Button(remote, image = up_img).pack(side = 'top')

left_img = tkinter.PhotoImage(master = remote_canvas, file = r'RemoteAssets/btn_left.png')
left = tkinter.Button(remote, image = left_img).pack(side = 'left')

right_img = tkinter.PhotoImage(master = remote_canvas, file = r'RemoteAssets/btn_right.png')
right = tkinter.Button(remote, image = right_img).pack(side = 'right')

down_img = tkinter.PhotoImage(master = remote_canvas, file = r'RemoteAssets/btn_down.png')
down = tkinter.Button(remote, image = down_img).pack(side = 'bottom')

##################################################################################
# Code for TV
tv = tkinter.Tk(className = "Television")

##################################################################################
# Code for TV guide(?)

##################################################################################
# Main
remote.mainloop()
tv.mainloop()