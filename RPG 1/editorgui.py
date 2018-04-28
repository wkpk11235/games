import tkinter,pygame,os
pygame.init()
scrwidth,scrheight=800,600

root = tkinter.Tk()

embed = tk.Frame(root, width = 800, height = 600)
embed.grid(columnspan = (600), rowspan = 500) #creates gridddddd?
embed.pack(side = tkinter.LEFT) #packs window to the left,which is not really prefered

buttonwin = tk.Frame(root, width = 75, height = 500) #say.. why height so high?
buttonwin.pack(side = tkinter.LEFT) #left too///

os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'

screen = pygame.display.set_mode((500,500))
screen.fill(255,255,255)

pygame.draw.circle(screen, (0,0,0), (250,250), 125) #testing code.... probably gonna work.

while True:
	pygame.display.update()
	root.update_idletasks()
	root.update()
