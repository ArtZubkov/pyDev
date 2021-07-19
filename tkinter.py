from tkinter import *
root=Tk()
canv = Canvas(root, width = 750, height = 750, bg = 'white', cursor = 'pencil')
canv.create_rectangle(0,0,750,250,fill="darkblue")

canv.create_polygon([1000,250],[350,250],[300,300],[275,375],[250,450],[350,500],[375,525],[750,550],fill='blue',smooth=1)





    
                    
canv.pack()
root.mainloop()

