try:
    #gif background
    frame_count = 24
    frames = [PhotoImage(file='logo.gif',format = 'gif -index %i' %(i)) for i in range(frame_count)]

    #function to animate gif
    def backimg(ind):
        frame = frames[ind]
        ind += 1
        if ind == frame_count:
            ind = 0
        gif_label.configure(image=frame)
        root.after(100, backimg, ind)

    #label for gif background
    gif_label = Label(root)
    gif_label.place(x=-20,y=-50)
    root.after(0, backimg, 0)
except:
    pass

