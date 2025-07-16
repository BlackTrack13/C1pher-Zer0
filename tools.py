def tkcenter(form):
    form.update()
    fw = form.winfo_width()
    fh  = form.winfo_height()
    sw = form.winfo_screenwidth() 
    sh  = form.winfo_screenheight()
    x    =  ( sw - fw ) / 2
    y    =  ( sh - fh ) / 2
    form.geometry( '%dx%d+%d+%d' % ( fw , fh , x , y ) )


# To call it use first :     ----->  import tools
# Second : -----> tools.tkcenter (  your form here ) after u make your frm.geometry( --- )

