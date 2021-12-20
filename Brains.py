import tkinter

##################################################################################
# Code for remote
remote = tkinter.Tk(className = "Remote")

remote_canvas = tkinter.Canvas(remote)

up_img = tkinter.PhotoImage(master = remote_canvas, file = r'btn_up.png')
up = tkinter.Button(remote, image = up_img).pack(side = 'top')

##################################################################################
# Code for TV
tv = tkinter.Tk(className = "Television")

##################################################################################
# Code for TV guide(?)

##################################################################################
# Main
remote.mainloop()
tv.mainloop()