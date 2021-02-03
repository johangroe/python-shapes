import math
import tkinter as tk
import time

string_error = False

def tkinter_berechnen():
    
    
    global a_input
    global b_input
    global c_input

    global al_input
    global be_input
    global ga_input

    global nachkommastellen

    global error

    global string_error

    
    global flaecheninhalt
    global hoehe_a
    global hoehe_b
    global hoehe_c
    global seitenhalbierende_a
    global seitenhalbierende_b
    global seitenhalbierende_c
    global winkelhalbierende_a
    global winkelhalbierende_b
    global winkelhalbierende_c
    global inkreisradius
    global umkreisradius

    reset()

    if len(e1.get()) == 0:
        a_input = None
    else:
        try:
            a_input = float(e1.get())
        except ValueError:
            string_error = True
            a_input = None
    

    if len(e2.get()) == 0:
        b_input = None
    else:
        try:
            b_input = float(e2.get())
        except ValueError:
            string_error = True
            b_input = None


    if len(e3.get()) == 0:
        c_input = None
    else:
        try:
            c_input = float(e3.get())
        except ValueError:
            string_error = True
            c_input = None
        
   

    if len(e4.get()) == 0:
        al_input = None
    else:
        try:
            al_input = float(e4.get())
        except ValueError:
            string_error = True
            al_input = None
    

    if len(e5.get()) == 0:
        be_input = None
    else:
        try:
            be_input = float(e5.get())
        except ValueError:
            string_error = True
            be_input = None

    if len(e6.get()) == 0:
        ga_input = None
    else:
        try:
            ga_input = float(e6.get())
        except ValueError:
            string_error = True
            ga_input = None


    if len(e7.get()) == 0:
        nachkommastellen = None
    else:
        try:
            nachkommastellen = round(float(e7.get()))
        except ValueError:
            string_error = True
            nachkommastellen = None
    
    

    final_function()

    label1.config(text=a_output)
    label2.config(text=b_output)
    label3.config(text=c_output)
    label4.config(text=al_output)
    label5.config(text=be_output)
    label6.config(text=ga_output)
    error_label.config(text=error)

    label7.config(text=flaecheninhalt)
    label8.config(text=hoehe_a)
    label9.config(text=hoehe_b)
    label10.config(text=hoehe_c)
    label11.config(text=seitenhalbierende_a)
    label12.config(text=seitenhalbierende_b)
    label13.config(text=seitenhalbierende_c)
    label14.config(text=winkelhalbierende_a)
    label15.config(text=winkelhalbierende_b)
    label16.config(text=winkelhalbierende_c)
    label17.config(text=inkreisradius)
    label18.config(text=umkreisradius)

    #if error == "":
    #    print("fehlerfrei")
    
   
    
    




a_input = None    #5
b_input = None   #6
c_input = None    #5

al_input = None   #53.1
be_input = None   #73.7
ga_input = None   #53.1'''
nachkommastellen = 1
###


seiten = 0
winkel = 0


gesucht_eins = None
gesucht_zwei = None
gesucht_drei = None
gesucht = []
gegeben_seiten = []
gesucht_winkel_wsw = None
gegeben_seite_wsw = None
gesucht_seite_SsW = None
gegeben_seiten_name = []

kombi_alpha = False
kombi_beta = False
kombi_gamma = False

kombi_sws_alpha = False
kombi_sws_beta = False
kombi_sws_gamma = False
winkel_gesamt = None

flaecheninhalt = None
hoehe_a = None
hoehe_b = None
hoehe_c = None
seitenhalbierende_a = None
seitenhalbierende_b = None
seitenhalbierende_c = None
winkelhalbierende_a = None
winkelhalbierende_b = None
winkelhalbierende_c = None
inkreisradius = None
umkreisradius = None

error = None

###

def gegeben_gesucht():
    
    global error
    global a_input
    global b_input
    global c_input

    global al_input
    global be_input
    global ga_input


    global seiten
    global winkel
    global gesucht_eins
    global gesucht_zwei
    global gesucht_drei
    global gesucht
    global kombi_alpha
    global kombi_beta
    global kombi_gamma
    global gegeben
    global gegeben_seiten
    global gesucht_winkel_wsw
    global gegeben_seite_wsw
    global gesucht_seite_SsW

    global kombi_sws_alpha
    global kombi_sws_beta
    global kombi_sws_gamma

    global winkel_gesamt

    global string_error
    
    #a_input = float(e1.get())
    #b_input = float(e2.get())
    #c_input = float(e3.get())

    #print("#######")
    #print(a_input)
    #print(b_input)
    #print(c_input)


    if a_input != None and al_input != None:
        kombi_alpha = True
    
    if b_input != None and be_input != None:
        kombi_beta = True
    
    if c_input != None and ga_input != None:
        kombi_gamma = True

    if b_input != None and c_input != None and al_input != None:
        kombi_sws_alpha = True

    if c_input != None and a_input != None and be_input != None:
        kombi_sws_beta = True

    if a_input != None and b_input != None and ga_input != None:
        kombi_sws_gamma = True

    if a_input != None:
        seiten = seiten + 1
        gegeben.append("a")
        gegeben_seiten.append(a_input)
        gegeben_seite_wsw = "a"
        gegeben_seiten_name.append("a")
    else:
        gesucht.append("a")
        #a_input = 0
        gesucht_seite_SsW = "a"


    if b_input != None:
        seiten = seiten + 1
        gegeben.append("b")
        gegeben_seiten.append(b_input)
        gegeben_seite_wsw = "b"
        gegeben_seiten_name.append("b")
    else:
        gesucht.append("b")
        #b_input = 0
        gesucht_seite_SsW = "b"

    if c_input != None:
        seiten = seiten + 1
        gegeben.append("c")
        gegeben_seiten.append(c_input)
        gegeben_seite_wsw = "c"
        gegeben_seiten_name.append("c")
    else:
        gesucht.append("c")
        #c_input = 0
        gesucht_seite_SsW = "c"

    if al_input != None:
        winkel = winkel + 1
        if winkel_gesamt == None:
            winkel_gesamt = al_input
        else:
            winkel_gesamt = winkel_gesamt + al_input
        gegeben.append("alpha")
    else:
        gesucht.append("alpha")
        gesucht_winkel_wsw = "alpha"
        #al_input = 0

    if be_input != None:
        winkel = winkel + 1
        if winkel_gesamt == None:
            winkel_gesamt = be_input
        else:
            winkel_gesamt = winkel_gesamt + be_input
        gegeben.append("beta")
    else:
        gesucht.append("beta")
        gesucht_winkel_wsw = "beta"
        #be_input = 0

    if ga_input != None:
        winkel = winkel + 1
        if winkel_gesamt == None:
            winkel_gesamt = ga_input
        else:
            winkel_gesamt = winkel_gesamt + ga_input
        gegeben.append("gamma")
    else:
        gesucht.append("gamma")
        gesucht_winkel_wsw = "gamma"
        #ga_input = 0

    #ERRORS
    #'''
    if seiten + winkel > 3:
        error = "FEHLER: Zu viele Daten eingetragen!"
        methode = None
    elif seiten + winkel < 3:
        error = "FEHLER: Zu wenige Daten eingetragen!"
        methode = None
    else:#'''
        gesucht_eins = gesucht[0]
        gesucht_zwei = gesucht[1]
        gesucht_drei = gesucht[2]

    

    ##### DEGUG-PRINTS #####

    #print(seiten,"seiten")
    #print(winkel,"winkel")
    #print("gesucht 1:",gesucht_eins)
    #print("gesucht 2:",gesucht_zwei)
    #print("gesucht 3:",gesucht_drei)
    #print("kombi a/alpha",kombi_alpha)
    #print("kombi b/beta",kombi_beta)
    #print("kombi c/gamma",kombi_gamma)
    #print("kombi sws alpha",kombi_sws_alpha)
    #print("kombi sws beta",kombi_sws_beta)
    #print("kombi sws gamma",kombi_sws_gamma)
    #if error != "":
    #    print("ERROR:",error)
    #print("gesucht:",gesucht)
    #print("seitenlängen:",gegeben_seiten)
    #print("a:",a_input) #,e1.get())
    #print("b:",b_input) #,e2.get())
    #print("c:",c_input) #,e3.get())
    #print("alpha:",al_input,e4.get())
    #print("beta:",be_input,e5.get())
    #print("gamma",ga_input,e6.get())
    #print("Innenwinkel:",winkel_gesamt)






methode = ""
gegeben = []

def rechenansatz():
    global methode

    global seiten
    global winkel

    global a_input
    global b_input
    global c_input

    global al_input
    global be_input
    global ga_input

    global gegeben_seiten_name

    global string_error

    

    if seiten == 0 and winkel == 3:
        error = "FEHLER: Das eingegebene Dreieck existiert nicht oder ist nicht eindeutig!"

    

    

    #sss
    if seiten == 3 and winkel == 0:
        methode = "sss"
        

    ###SsW
    if seiten == 2 and winkel == 1:
        if kombi_alpha == True or kombi_beta == True or kombi_gamma == True:

            if kombi_alpha == True:
                gegeben_seiten_name.remove("a")

                if gegeben_seiten_name[0] == "b":
                    if float(b_input) < float(a_input):
                        methode = "SsW"
                
                if gegeben_seiten_name[0] == "c":
                    if float(c_input) < float(a_input):
                        methode = "SsW"
                
                gegeben_seiten_name.append("a")

            if kombi_beta == True:
                gegeben_seiten_name.remove("b")

                if gegeben_seiten_name[0] == "a":
                    if float(a_input) < float(b_input):
                        methode = "SsW"
                
                if gegeben_seiten_name[0] == "c":
                    if float(c_input) < float(b_input):
                        methode = "SsW"
                
                gegeben_seiten_name.append("b")

            if kombi_gamma == True:
                gegeben_seiten_name.remove("c")

                if gegeben_seiten_name[0] == "a":
                    if float(a_input) < float(c_input):
                        methode = "SsW"
                
                if gegeben_seiten_name[0] == "b":
                    if float(b_input) < float(c_input):
                        methode = "SsW"
                gegeben_seiten_name.append("c")
                

            ###ssw

            if kombi_alpha == True:
                gegeben_seiten_name.remove("a")

                if gegeben_seiten_name[0] == "b":
                    if float(b_input) >= float(a_input):
                        methode = "SsW"
                
                if gegeben_seiten_name[0] == "c":
                    if float(c_input) >= float(a_input):
                        methode = "SsW"
                
                gegeben_seiten_name.append("a")
                

            if kombi_beta == True:
                gegeben_seiten_name.remove("b")

                if gegeben_seiten_name[0] == "a":
                    if float(a_input) >= float(b_input):
                        methode = "SsW"
                
                if gegeben_seiten_name[0] == "c":
                    if float(c_input) >= float(b_input):
                        methode = "SsW"
                
                gegeben_seiten_name.append("b")

            if kombi_gamma == True:
                gegeben_seiten_name.remove("c")

                if gegeben_seiten_name[0] == "a":
                    if float(a_input) >= float(c_input):
                        methode = "SsW"
                
                if gegeben_seiten_name[0] == "b":
                    if float(b_input) >= float(c_input):
                        methode = "SsW"
                
                gegeben_seiten_name.append("c")

        #sws
        if kombi_sws_alpha == True:
            methode = "sws"
        if kombi_sws_beta == True:
            methode = "sws"
        if kombi_sws_gamma == True:
            methode = "sws"
    #wsw
    if seiten == 1 and winkel == 2:
        methode = "wsw"
    
    if winkel_gesamt != None:
        if winkel_gesamt > 180:
            error = "FEHLER: Das eingegebene Dreieck existiert nicht!"
            methode = None
    


    #print("methode:",methode)
    #print("gegeben:",gegeben)
    

a_output = None
b_output = None
c_output = None

al_output = None
be_output = None
ga_output = None



def berechnung():
    global methode
    global gegeben_seiten
    global error
    global gegeben

    global a_output
    global b_output
    global c_output

    global al_output
    global be_output
    global ga_output

    global a_input
    global b_input
    global c_input

    global al_input
    global be_input
    global ga_input

    global kombi_alpha
    global kombi_beta
    global kombi_gamma

    global nachkommastellen

    global flaecheninhalt
    global hoehe_a
    global hoehe_b
    global hoehe_c
    global seitenhalbierende_a
    global seitenhalbierende_b
    global seitenhalbierende_c
    global winkelhalbierende_a
    global winkelhalbierende_b
    global winkelhalbierende_c
    global inkreisradius
    global umkreisradius

    global string_error

    if "a" in gegeben :
        a_output = a_input
    if "b" in gegeben :
        b_output = b_input
    if "c" in gegeben :
        c_output = c_input
    if "alpha" in gegeben :
        al_output = al_input
    if "beta" in gegeben :
        be_output = be_input
    if "gamma" in gegeben :
        ga_output = ga_input

### sss

    if methode == "sss":
        ###existiert dreieck?
        gegeben_seiten.sort()
        biggest_edge = gegeben_seiten[-1]
        del gegeben_seiten[-1]
        second_edge = gegeben_seiten[-1]
        del gegeben_seiten[-1]
        third_edge = gegeben_seiten[-1]
        #print("seiten sortiert")
        if biggest_edge > second_edge + third_edge:
            error = "FEHLER: Das eingegebene Dreieck existiert nicht!"
            #print("Dreieck existiert nicht")
        
        else:
            #print("Dreieck existiert")
            #berechnung sss
            al_output = -(a_output**2 - b_output**2 - c_output**2)/(2*b_output*c_output)
            al_output = math.acos(al_output)
            al_output = math.degrees(al_output)

            be_output = (a_output**2 - b_output**2 + c_output**2)/(2*a_output*c_output)
            be_output = math.acos(be_output)
            be_output = math.degrees(be_output)

            ga_output = 180 - al_output - be_output


### sws       

    if methode == "sws":
        if kombi_sws_alpha == True:
            a_output = (b_output**2 + c_output**2 - 2*b_output*c_output* math.cos(math.radians(al_output)))
            a_output = math.sqrt(a_output)

            be_output = (a_output**2 - b_output**2 + c_output**2)/(2*a_output*c_output)
            be_output = math.acos(be_output)
            be_output = math.degrees(be_output)

            ga_output = 180 - al_output - be_output
        
        if kombi_sws_beta == True:
            b_output = (a_output**2 + c_output**2 - 2*a_output*c_output * math.cos(math.radians(be_output)))
            b_output = math.sqrt(b_output)

            al_output = -(a_output**2 - b_output**2 - c_output**2)/(2*b_output*c_output)
            al_output = math.acos(al_output)
            al_output = math.degrees(al_output)

            ga_output = 180 - al_output - be_output

            
        
        if kombi_sws_gamma == True:
            c_output = (b_output**2 + a_output**2 - 2*b_output*a_output* math.cos(math.radians(ga_output)))
            c_output = math.sqrt(c_output)

            al_output = -(a_output**2 - b_output**2 - c_output**2)/(2*b_output*c_output)
            al_output = math.acos(al_output)
            al_output = math.degrees(al_output)
            
            be_output = 180 - al_output - ga_output

            
### wsw

    if methode == "wsw":
        #print(gesucht_winkel_wsw)
        #print(gegeben_seite_wsw)
        if gesucht_winkel_wsw == "alpha":
            al_output = 180 - be_output - ga_output
        elif gesucht_winkel_wsw == "beta":
            be_output = 180 - al_output - ga_output
        elif gesucht_winkel_wsw == "gamma":
            ga_output = 180 - al_output - be_output

        if gegeben_seite_wsw == "a":
            b_output = (a_output * math.sin(math.radians(be_output)))/(math.sin(math.radians(al_output)))
            c_output = (a_output * math.sin(math.radians(ga_output)))/(math.sin(math.radians(al_output)))

        if gegeben_seite_wsw == "b":
            a_output = (b_output * math.sin(math.radians(al_output)))/(math.sin(math.radians(be_output)))
            c_output = (b_output * math.sin(math.radians(ga_output)))/(math.sin(math.radians(be_output)))
        
        if gegeben_seite_wsw == "c":
            a_output = (c_output * math.sin(math.radians(al_output)))/(math.sin(math.radians(ga_output)))
            b_output = (c_output * math.sin(math.radians(be_output)))/(math.sin(math.radians(ga_output)))

### SsW

    if methode == "SsW":
        #print("gesuchte seite:",gesucht_seite_SsW)

        if kombi_alpha == True:
            gegeben_seiten_name.remove("a")
            if gegeben_seiten_name[0] == "b":
                be_output = (math.sin(math.radians(al_output)) * b_output)/a_output
                be_output = math.degrees(math.asin(be_output))

                ga_output = 180 - be_output - al_output

                c_output = (b_output * math.sin(math.radians(ga_output)))/(math.sin(math.radians(be_output)))
            
            if gegeben_seiten_name[0] == "c":
                ga_output = (math.sin(math.radians(al_output)) * c_output)/a_output
                ga_output = math.degrees(math.asin(ga_output))

                be_output = 180 - ga_output - al_output

                b_output = (c_output * math.sin(math.radians(be_output)))/(math.sin(math.radians(ga_output)))


        if kombi_beta == True:
            gegeben_seiten_name.remove("b")
            if gegeben_seiten_name[0] == "a":
               al_output = (math.sin(math.radians(be_output)) * a_output)/b_output
               al_output = math.degrees(math.asin(al_output))

               ga_output = 180 - be_output - al_output
               
               c_output = (b_output * math.sin(math.radians(ga_output)))/(math.sin(math.radians(be_output)))

            if gegeben_seiten_name[0] =="c":
                ga_output = (math.sin(math.radians(be_output)) * c_output)/b_output
                ga_output = math.degrees(math.asin(ga_output))

                al_output = 180 - ga_output - be_output

                a_output = (b_output * math.sin(math.radians(al_output)))/(math.sin(math.radians(be_output)))
        
        if kombi_gamma == True:
            gegeben_seiten_name.remove("c")
            if gegeben_seiten_name[0] == "a":
                al_output = (math.sin(math.radians(ga_output)) * a_output)/c_output
                al_output = math.degrees(math.asin(al_output))

                be_output = 180 - ga_output - al_output

                b_output = (c_output * math.sin(math.radians(be_output)))/(math.sin(math.radians(ga_output)))
            
            if gegeben_seiten_name[0] == "b":
                be_output = (math.sin(math.radians(ga_output)) * b_output)/c_output
                be_output = math.degrees(math.asin(be_output))

                al_output = 180 - be_output - ga_output

                a_output = (b_output * math.sin(math.radians(al_output)))/(math.sin(math.radians(be_output)))
    
    ###  ssw

    if methode == "ssw":
        if kombi_alpha == True:
            gegeben_seiten_name.remove("a")

            if gegeben_seiten_name[0] == "b":
                #print("b gefunden!")
                be_output = (math.sin(math.radians(al_output)) * b_output)/a_output
                if be_output > 1:
                    error = "FEHLER: Das eingegebene Dreieck existiert nicht oder ist nicht eindeutig!"
                    be_output = None
                else:
                    be_output = math.degrees(math.asin(be_output))

                    ga_output = 180 - be_output - al_output

                    c_output = (math.sin(math.radians(ga_output)) * b_output) / math.sin(math.radians(be_output))
            
            if gegeben_seiten_name[0] == "c":
                #print("c gefunden!")
                ga_output = (math.sin(math.radians(al_output)) * c_output) / a_output
                if ga_output > 1:
                    error = "FEHLER: Das eingegebene Dreieck existiert nicht oder ist nicht eindeutig!"
                    ga_output = None
                else:
                    ga_output = math.degrees(math.asin(ga_output))

                    be_output = 180 - ga_output - al_output

                    b_output = (math.sin(math.radians(be_output)) * c_output) / math.sin(math.radians(ga_output))

        if kombi_beta == True:
            gegeben_seiten_name.remove("b")
            if gegeben_seiten_name[0] == "a":
                #print("a gefunden!")
                al_output = (math.sin(math.radians(be_output)) * a_output) / b_output
                if al_output > 1:
                    error = "FEHLER: Das eingegebene Dreieck existiert nicht oder ist nicht eindeutig!"
                    al_output = None
                else:
                    al_output = math.degrees(math.asin(al_output))

                    ga_output = 180 - al_output - be_output

                    c_output = (math.sin(math.radians(ga_output)) * b_output) / math.sin(math.radians(be_output))

            if gegeben_seiten_name[0] == "c":
                #print("c gefunden!")
                ga_output = (math.sin(math.radians(be_output)) * c_output) / b_output
                if ga_output > 1:
                    error = "FEHLER: Das eingegebene Dreieck existiert nicht oder ist nicht eindeutig!"
                    ga_output = None
                else:
                    ga_output = math.degrees(math.asin(ga_output))

                    al_output = 180 - ga_output - be_output

                    a_output = (math.sin(math.radians(al_output)) * b_output) / math.sin(math.radians(be_output))

        if kombi_gamma == True:
            gegeben_seiten_name.remove("c")
            if gegeben_seiten_name[0] == "a":
                #print("a gefunden!")
                al_output = al_output = (math.sin(math.radians(ga_output)) * a_output) / c_output
                if al_output > 1:
                    error = "FEHLER: Das eingegebene Dreieck existiert nicht oder ist nicht eindeutig!"
                    al_output = None
                else: 
                    al_output = math.degrees(math.asin(al_output))

                    be_output = 180 - al_output - ga_output 

                    b_output = (math.sin(math.radians(be_output)) * c_output) / math.sin(math.radians(ga_output))
            
            if gegeben_seiten_name[0] == "b":
                #print("b gefunden!")
                be_output = (math.sin(math.radians(ga_output)) * b_output)/c_output
                if be_output > 1:
                    error = "FEHLER: Das eingegebene Dreieck existiert nicht oder ist nicht eindeutig!"
                    be_output = None
                else: 
                    be_output = math.degrees(math.asin(be_output))

                    al_output = 180 - be_output - ga_output

                    a_output = (math.sin(math.radians(al_output)) * b_output) / math.sin(math.radians(be_output))


    ###restliche berechnungen ###

    if methode != None:
        flaecheninhalt = (a_output * b_output * (math.sin(math.radians(ga_output))))

        hoehe_a = b_output * math.sin(math.radians(ga_output))

        hoehe_b = a_output * math.sin(math.radians(ga_output))

        hoehe_c = b_output * math.sin(math.radians(al_output))

        seitenhalbierende_a = b_output**2 + c_output**2 + (2 * b_output * c_output *(math.cos(math.radians(al_output))))
        seitenhalbierende_a = math.sqrt(seitenhalbierende_a) / 2

        seitenhalbierende_b = a_output**2 + c_output**2 + (2 * a_output * c_output *(math.cos(math.radians(be_output))))
        seitenhalbierende_b = math.sqrt(seitenhalbierende_b) / 2

        seitenhalbierende_c = a_output**2 + b_output**2 + (2 * a_output * b_output *(math.cos(math.radians(ga_output))))
        seitenhalbierende_c = math.sqrt(seitenhalbierende_c) / 2

        winkelhalbierende_a = (2 * b_output * c_output *(math.cos(math.radians(al_output / 2)))) / (b_output + c_output)
        
        winkelhalbierende_b = (2 * a_output * c_output *(math.cos(math.radians(be_output / 2)))) / (a_output + c_output)

        winkelhalbierende_c = (2 * a_output * b_output *(math.cos(math.radians(ga_output / 2)))) / (a_output + b_output)
        #print(winkelhalbierende_a,",",winkelhalbierende_b,",",winkelhalbierende_c)

        inkreisradius = (((a_output + b_output + c_output) / 2) - a_output) * math.tan(math.radians(al_output / 2))
        #print(inkreisradius)
        
        umkreisradius = a_output / (2 * math.sin(math.radians(al_output)))
        #print(umkreisradius)

    if methode == None:
        pass

    if string_error == True:
        error = "FEHLER: Keine numerischen Daten eingetragen!"

    if winkel_gesamt != None:
        if winkel_gesamt > 180:
            error = "FEHLER: Das eingegebene Dreieck existiert nicht!"

    if winkel + seiten > 3:
        error = "FEHLER: Zu viele Daten eingetragen!"




    
    #'''
    
    if error == None or error == "":
        a_output = round(a_output, nachkommastellen)
        b_output = round(b_output, nachkommastellen)
        c_output = round(c_output, nachkommastellen)
        al_output = round(al_output, nachkommastellen)
        be_output = round(be_output, nachkommastellen)
        ga_output = round(ga_output, nachkommastellen)
        flaecheninhalt = round(flaecheninhalt, nachkommastellen)
        hoehe_a = round(hoehe_a, nachkommastellen)
        hoehe_b = round(hoehe_b, nachkommastellen)
        hoehe_c = round(hoehe_c, nachkommastellen)
        seitenhalbierende_a = round(seitenhalbierende_a, nachkommastellen)
        seitenhalbierende_b = round(seitenhalbierende_b, nachkommastellen)
        seitenhalbierende_c = round(seitenhalbierende_c, nachkommastellen)
        winkelhalbierende_a = round(winkelhalbierende_a, nachkommastellen)
        winkelhalbierende_b = round(winkelhalbierende_b, nachkommastellen)
        winkelhalbierende_c = round(winkelhalbierende_c, nachkommastellen)
        inkreisradius = round(inkreisradius, nachkommastellen)
        umkreisradius = round(umkreisradius, nachkommastellen)
    
    #'''

    #print("größte seite:",biggest_edge)
    #print("zweitgrößte seite:",second_edge)
    #print("drittgrößte seite:",third_edge)


outputs_shown = False

def outputs():
    global outputs_shown
    global error

    global a_output
    global b_output
    global c_output

    global al_output
    global be_output
    global ga_output

    global flaecheninhalt
    global hoehe_a
    global hoehe_b
    global hoehe_c
    global seitenhalbierende_a
    global seitenhalbierende_b
    global seitenhalbierende_c
    global winkelhalbierende_a
    global winkelhalbierende_b
    global winkelhalbierende_c
    global inkreisradius
    global umkreisradius



    if error != "Kein Fehler aufgetreten!":
        outputs_shown = False
    if error == "Kein Fehler aufgetreten!" or error == None or error == "":
        outputs_shown = True
    
    if outputs_shown == False:
        a_output = "n.L."
        b_output = "n.L."
        c_output = "n.L."

        al_output = "n.L."
        be_output = "n.L."
        ga_output = "n.L."

        flaecheninhalt = "n.L."
        hoehe_a = "n.L."
        hoehe_b = "n.L."
        hoehe_c = "n.L."
        seitenhalbierende_a = "n.L."
        seitenhalbierende_b = "n.L."
        seitenhalbierende_c = "n.L."
        winkelhalbierende_a = "n.L."
        winkelhalbierende_b = "n.L."
        winkelhalbierende_c = "n.L."
        inkreisradius = "n.L."
        umkreisradius = "n.L."

        #print(error)
    
    elif outputs_shown == True:
        pass









def reset():
    global a_output
    global b_output
    global c_output
    global al_output
    global be_output
    global ga_output
    
    global seiten
    global winkel


    global gesucht_eins
    global gesucht_zwei
    global gesucht_drei
    global gesucht
    global gegeben_seiten
    global gesucht_winkel_wsw 
    global gegeben_seite_wsw
    global gesucht_seite_SsW
    global gegeben_seiten_name

    global kombi_alpha
    global kombi_beta
    global kombi_gamma

    global kombi_sws_alpha
    global kombi_sws_beta
    global kombi_sws_gamma
    global error

    global a_input
    global b_input
    global c_input
    global al_input
    global be_input
    global c_input

    global methode
    global gegeben

    global winkel_gesamt
    

    global flaecheninhalt
    global hoehe_a
    global hoehe_b
    global hoehe_c
    global seitenhalbierende_a
    global seitenhalbierende_b
    global seitenhalbierende_c
    global winkelhalbierende_a
    global winkelhalbierende_b
    global winkelhalbierende_c
    global inkreisradius
    global umkreisradius

    global string_error

    a_output = None
    b_output = None
    c_output = None
    al_output = None
    be_output = None
    ga_output = None


    seiten = 0
    winkel = 0


    gesucht_eins = None
    gesucht_zwei = None
    gesucht_drei = None
    gesucht.clear()
    gegeben_seiten.clear()
    gesucht_winkel_wsw = None
    gegeben_seite_wsw = None
    gesucht_seite_SsW = None
    gegeben_seiten_name.clear()

    kombi_alpha = False
    kombi_beta = False
    kombi_gamma = False

    kombi_sws_alpha = False
    kombi_sws_beta = False
    kombi_sws_gamma = False
    error = ""
    
    a_input = None
    b_input = None
    c_input = None
    al_input = None
    be_input = None
    c_input = None

    methode = None
    gegeben.clear()

    string_error = False

    winkel_gesamt = None

    flaecheninhalt = None

    hoehe_a = None
    hoehe_b = None
    hoehe_c = None
    seitenhalbierende_a = None
    seitenhalbierende_b = None
    seitenhalbierende_c = None
    winkelhalbierende_a = None
    winkelhalbierende_b = None
    winkelhalbierende_c = None
    inkreisradius = None
    umkreisradius = None








def final_function():

    

    gegeben_gesucht()

    rechenansatz()

    berechnung()

    outputs()
    '''
    if outputs_shown == True:

        print(" ")
        print("-----------OUTPUTS----------")
        print("a =",a_output)
        print("b =",b_output)
        print("c = ",c_output)
        print("alpha =",al_output)
        print("beta = ",be_output)
        print("gamma =",ga_output)
        print(" ")


    if outputs_shown == False:
        print("ERROR:",error)

    #'''


#final_function()




app = tk.Tk(className = " DREIECKS - BERECHNUNGEN :-)")





tk.Label(app, text = "Genau 3 Daten eingeben (Dezimalst. ausgenommen),").grid(row = 0, column = 2, sticky = "w")

tk.Label(app, text = "Kommazahlen mit Punkt statt Komma schreiben!").grid(row = 1, column = 2, sticky = "w")

error_label = tk.Label(app, text = "")
error_label.grid(row = 21, column = 2)


tk.Label(app, text = "a :").grid(row = 2)
tk.Label(app, text = "b :").grid(row = 3)
tk.Label(app, text = "c :").grid(row = 4)
tk.Label(app, text = "alpha :").grid(row = 5)
tk.Label(app, text = "beta :").grid(row = 6)
tk.Label(app, text = "gamma :").grid(row = 7)
tk.Label(app, text = "Flächeninh.:").grid(row = 8)
tk.Label(app, text = "Höhe a:").grid(row = 9)
tk.Label(app, text = "Höhe b:").grid(row = 10)
tk.Label(app, text = "Höhe c:").grid(row = 11)
tk.Label(app, text = "Seitenhalb. a:").grid(row = 12)
tk.Label(app, text = "Seitenhalb. b:").grid(row = 13)
tk.Label(app, text = "Seitenhalb. c:").grid(row = 14)
tk.Label(app, text = "Winkelhalb. a:").grid(row = 15)
tk.Label(app, text = "Winkelhalb. b:").grid(row = 16)
tk.Label(app, text = "Winkelhalb. c:").grid(row = 17)
tk.Label(app, text = "Inkreisradius:").grid(row = 18)
tk.Label(app, text = "Umkreisradius:").grid(row = 19)

tk.Label(app, text = "Dezimalst.").grid(row = 20)

e1 = tk.Entry(app)
e2 = tk.Entry(app)
e3 = tk.Entry(app)
e4 = tk.Entry(app)
e5 = tk.Entry(app)
e6 = tk.Entry(app)
e7 = tk.Entry(app)


e1.grid(row = 2, column = 1)
e2.grid(row = 3, column = 1)
e3.grid(row = 4, column = 1)
e4.grid(row = 5, column = 1)
e5.grid(row = 6, column = 1)
e6.grid(row = 7, column = 1)
e7.grid(row = 20, column = 1)


label1 = tk.Label(app, text = a_input)
label2 = tk.Label(app, text = b_input)
label3 = tk.Label(app, text = c_input)
label4 = tk.Label(app, text = al_input)
label5 = tk.Label(app, text = be_input)
label6 = tk.Label(app, text = ga_input)

label7 = tk.Label(app, text = flaecheninhalt)
label8 = tk.Label(app, text = hoehe_a)
label9 = tk.Label(app, text = hoehe_b)
label10 = tk.Label(app, text = hoehe_c)
label11 = tk.Label(app, text = seitenhalbierende_a)
label12 = tk.Label(app, text = seitenhalbierende_b)
label13 = tk.Label(app, text = seitenhalbierende_c)
label14 = tk.Label(app, text = winkelhalbierende_a)
label15 = tk.Label(app, text = winkelhalbierende_b)
label16 = tk.Label(app, text = winkelhalbierende_c)
label17 = tk.Label(app, text = inkreisradius)
label18 = tk.Label(app, text = umkreisradius)



label1.grid(row = 2, column = 2, sticky = "w")
label2.grid(row = 3, column = 2, sticky = "w")
label3.grid(row = 4, column = 2, sticky = "w")
label4.grid(row = 5, column = 2, sticky = "w")
label5.grid(row = 6, column = 2, sticky = "w")
label6.grid(row = 7, column = 2, sticky = "w")

label7.grid(row = 8, column = 1)#, sticky = "w")
label8.grid(row = 9, column = 1)#, sticky = "w")
label9.grid(row = 10, column = 1)#, sticky = "w")
label10.grid(row = 11, column = 1)#, sticky = "w")
label11.grid(row = 12, column = 1)#, sticky = "w")
label12.grid(row = 13, column = 1)#, sticky = "w")
label13.grid(row = 14, column = 1)#, sticky = "w")
label14.grid(row = 15, column = 1)#, sticky = "w")
label15.grid(row = 16, column = 1)#, sticky = "w")
label16.grid(row = 17, column = 1)#, sticky = "w")
label17.grid(row = 18, column = 1)#, sticky = "w")
label18.grid(row = 19, column = 1)#, sticky = "w")



tk.Button(app, text = "Verlassen!", command = app.quit).grid(row = 21, column = 0)
tk.Button(app, text = "Berechnen!", command = tkinter_berechnen).grid(row = 21, column = 1)

tk.mainloop()