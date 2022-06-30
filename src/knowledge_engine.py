from experta import *

#----------
# Variables
#----------

class DiagnosisOfDepressiveDisorder(KnowledgeEngine):

    @DefFacts()
    def _initial_action(self):
        print("This is expert system do you have some of the next symptoms?")
        yield Fact(action="find_depressive_disorder")

    #---------------------------------------------------------------------
    # Symptom questions and y/n answers
    #---------------------------------------------------------------------
    
    def iniciar(self, rpta):{}

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_1=W())), salience=37)
    def symptom_1(self, rpta):
        print("1. ¿Estás deprimido (a) por alguna situación de tu vida?")
        self.declare(Fact(question_1 = rpta))
        print("rpta1: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_2=W())), salience=36)
    def symptom_2(self, rpta):
        print("2. ¿Tienes muy poco sueño?")
        self.declare(Fact(question_2 = rpta))
        print("rpta2: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_3=W())), salience=35)
    def symptom_3(self, rpta):
        print("3. ¿Sientes fatiga o pierdes la energía casi a diario?")
        self.declare(Fact(question_3 = rpta))
        print("rpta3: " + rpta)

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_4=W())), salience=34)
    def symptom_4(self, rpta):
        print("¿Tienes baja autoestima?: ")
        self.declare(Fact(question_4 = rpta))
        print("rpta4: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_5=W())), salience=33)
    def symptom_5(self, rpta):
        print("5. ¿Comes muy poco?:")
        self.declare(Fact(question_5 = rpta))
        print("rpta5: " + rpta)

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_6=W())), salience=32)
    def symptom_6(self, rpta):
        print("6. ¿Tienes problemas de memoria, atención y concentración?")
        self.declare(Fact(question_6 = rpta))
        print("rpta6: " + rpta)

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_7=W())), salience=31)
    def symptom_7(self, rpta):
        print("7. ¿Tienes pensamiento de que todo sale mal?")
        self.declare(Fact(question_7 = rpta))
        print("rpta7: " + rpta)

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_8=W())), salience=30)
    def symptom_8(self, rpta):
        print("8. ¿Ves el futuro negativamente?: ")
        self.declare(Fact(question_8 = rpta))
        print("rpta8: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_9=W())), salience=29)
    def symptom_9(self, rpta):
        print("9. ¿Tienes pensamientos negativos?")
        self.declare(Fact(question_9 = rpta))
        print("rpta9: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_10=W())), salience=28)
    def symptom_10(self, rpta):
        print("10. ¿Te desanimas con facilidad?:")
        self.declare(Fact(question_10 = rpta))
        print("rpta10: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_11=W())), salience=27)
    def symptom_11(self, rpta):
        print("11. ¿Tienes pensamientos suicidas?:")
        self.declare(Fact(question_11 = rpta))
        print("rpta11: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_12=W())), salience=26)
    def symptom_12(self, rpta):
        print("12. ¿Tienes pensamientos de hacerte daño?")
        self.declare(Fact(question_12 = rpta))
        print("rpta12: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_13=W())), salience=25)
    def symptom_13(self, rpta):
        print("13. ¿No quieres conversar con nadie?:")
        self.declare(Fact(question_13 = rpta))
        print("rpta13: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_14=W())), salience=24)
    def symptom_14(self, rpta):
        print("14. ¿No quieres salir a ningún lado?:")
        self.declare(Fact(question_14 = rpta))
        print("rpta14: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_15=W())), salience=23)
    def symptom_15(self, rpta):
        print("15. ¿Te sientes triste o vacío?:")
        self.declare(Fact(question_15 = rpta))
        print("rpta15: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_16=W())), salience=22)
    def symptom_16(self, rpta):
        print("16. ¿Te sientes a veces o siempre irritable?")
        self.declare(Fact(question_16 = rpta))
        print("rpta16: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_17=W())), salience=21)
    def symptom_17(self, rpta):
        print("17. ¿Has perdido o aumentado 5'%' de tu peso corporal?")
        self.declare(Fact(question_17 = rpta))
        print("rpta17: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_18=W())), salience=20)
    def symptom_18(self, rpta):
        print("18. ¿Presentas insomnio casi a diario?:")
        self.declare(Fact(question_18 = rpta))
        print("rpta18: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_19=W())), salience=19)
    def symptom_19(self, rpta):
        print("19. ¿Te agitas en actividades psicomotoras?:")
        self.declare(Fact(question_19 = rpta))
        print("rpta19: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_20=W())), salience=18)
    def symptom_20(self, rpta):
        print("20. ¿Presentas sensación de inutilidad y confusión?")
        self.declare(Fact(question_20 = rpta))
        print("rpta20: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_21=W())), salience=17)
    def symptom_21(self, rpta):
        print("21. ¿Has perdido a un ser querido recientemente?:")
        self.declare(Fact(question_21 = rpta))
        print("rpta21: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_22=W())), salience=16)
    def symptom_22(self, rpta):
        print("22. ¿Tienes alucinaciones?:")
        self.declare(Fact(question_22 = rpta))
        print("rpta22: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_23=W())), salience=15)
    def symptom_23(self, rpta):
        print("23. ¿Estás pasando por algún problema?:")
        self.declare(Fact(question_23 = rpta))
        print("rpta23: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_24=W())), salience=14)
    def symptom_24(self, rpta):
        print("24. ¿Piensas que no tienes suerte en tu vida?:")
        self.declare(Fact(question_24 = rpta))
        print("rpta24: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_25=W())), salience=13)
    def symptom_25(self, rpta):
        print("25. ¿Todos los síntomas se presentan de vez en cuando?:")
        self.declare(Fact(question_25 = rpta))
        print("rpta25: " + rpta)

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_26=W())), salience=12)
    def symptom_26(self, rpta):
        print("26. ¿Todos los síntomas se presentan todos los días?:")
        self.declare(Fact(question_26 = rpta))
        print("rpta26: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_27=W())), salience=11)
    def symptom_27(self, rpta):
        print("27. ¿Estás muy estresado?")
        self.declare(Fact(question_27 = rpta))
        print("rpta27: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_28=W())), salience=10)
    def symptom_28(self, rpta):
        print("28. ¿Sientes que tu vida no tiene sentido?")
        self.declare(Fact(question_28 = rpta))
        print("rpta28: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_29=W())), salience=9)
    def symptom_29(self, rpta):
        print("29. ¿Te sientes agotado y con miedo?")
        self.declare(Fact(question_29 = rpta))
        print("rpta29: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_30=W())), salience=8)
    def symptom_30(self, rpta):
        print("30. ¿Sufres de falta de motivación para realizar tus cosas cotidianas?")
        self.declare(Fact(question_30 = rpta))
        print("rpta30: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_31=W())), salience=7)
    def symptom_31(self, rpta):
        print("31. ¿No tienes pasión por nada?")
        self.declare(Fact(question_31 = rpta))
        print("rpta31: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_32=W())), salience=6)
    def symptom_32(self, rpta):
        print("32. ¿Tienes ganas de dormir en el día?")
        self.declare(Fact(question_32 = rpta))
        print("rpta32: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_33=W())), salience=5)
    def symptom_33(self, rpta):
        print("33. ¿Te encuentras en un estado de ilusión?")
        self.declare(Fact(question_33 = rpta))
        print("rpta33: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_34=W())), salience=4)
    def symptom_34(self, rpta):
        print("34. ¿Escuchas voces en la cabeza?")
        self.declare(Fact(question_34 = rpta))
        print("rpta34: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_35=W())), salience=3)
    def symptom_35(self, rpta):
        print("35. ¿Eres muy impulsivo (a)?: ")
        self.declare(Fact(question_35 = rpta))
        print("rpta35: " + rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_36=W())), salience=2)
    def symptom_36(self, rpta):
        print("36. ¿Eres muy nervioso (a)?")
        self.declare(Fact(question_36 = rpta))
        print("rpta36: " + rpta)

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_37=W())), salience=1)
    def symptom_37(self, rpta):
        print("37. ¿Tienes sentimiento de miedo e inseguridad?:")
        self.declare(Fact(question_37 = rpta))
        print("rpta37: " + rpta)
    



    #---------------------------------------------------------------------------------------
    # Response validation to find the depression disorder
    #---------------------------------------------------------------------------------------


    @Rule(Fact(action="find_depressive_disorder"), Fact(question_1="si"), Fact(question_2="si"), Fact(question_3="si"), Fact(question_4="si"), Fact(question_5="si"))
    def disorder_1(self):
        self.declare(Fact(disorder="Depresión distimia leve"))
        return "Depresión distimia levelll"

    @Rule(Fact(action="find_depressive_disorder"), Fact(question_6="si"), Fact(question_7="si"), Fact(question_8="si"), Fact(question_9="si"), Fact(question_10="si"))
    def disorder_2(self):
        self.declare(Fact(disorder="Depresión distimia moderado"))
        return("Depresión distimia moderado")
        
    @Rule(Fact(action="find_depressive_disorder"), Fact(question_1="si"), Fact(question_2="si"), Fact(question_3="si"), Fact(question_4="si"), Fact(question_5="si"), Fact(question_6="si"), Fact(question_7="si"), Fact(question_8="si"), Fact(question_9="si"), Fact(question_10="si"))
    def disorder_3(self):
        self.declare(Fact(disorder="Depresión distimia moderado"))
        return("Depresión distimia moderado")
    

    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_1="si"), 
        Fact(question_2="si"), 
        Fact(question_3="si"), 
        Fact(question_4="si"), 
        Fact(question_5="si"), 
        Fact(question_6="si"), 
        Fact(question_7="si"), 
        Fact(question_8="si"), 
        Fact(question_9="si"), 
        Fact(question_10="si"),
        Fact(question_11="si"),
        Fact(question_12="si"),
        Fact(question_13="si"),
        Fact(question_14="si"))
    def disorder_4(self):
        self.declare(Fact(disorder="Depresión Distimia Grave"))
        return("Depresión Distimia Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_11="si"), 
        Fact(question_12="si"), 
        Fact(question_13="si"), 
        Fact(question_14="si"))
    def disorder_5(self):
        self.declare(Fact(disorder="Depresión Distimia Grave"))
        return("Depresión Distimia Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_3="si"), 
        Fact(question_15="si"), 
        Fact(question_16="si"), 
        Fact(question_19="si"))
    def disorder_6(self):
        self.declare(Fact(disorder="Depresión Mayor Leve"))
        return("Depresión Mayor Leve")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_3="si"), 
        Fact(question_15="si"), 
        Fact(question_16="si"), 
        Fact(question_18="si"),
        Fact(question_19="si"),
        Fact(question_20="si"))
    def disorder_7(self):
        self.declare(Fact(disorder="Depresión Mayor Moderado"))
        return("Depresión Mayor Moderado")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_18="si"),
        Fact(question_20="si"))
    def disorder_8(self):
        self.declare(Fact(disorder="Depresión Mayor Moderado"))
        return("Depresión Mayor Moderado")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_3="si"), 
        Fact(question_6="si"), 
        Fact(question_11="si"), 
        Fact(question_15="si"),
        Fact(question_16="si"),
        Fact(question_17="si"),
        Fact(question_18="si"),
        Fact(question_19="si"),
        Fact(question_20="si"),
        Fact(question_21="si"),
        Fact(question_22="si"))
    def disorder_9(self):
        self.declare(Fact(disorder="Depresión Mayor Grave"))
        return("Depresión Mayor Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_6="si"),
        Fact(question_11="si"),
        Fact(question_17="si"),
        Fact(question_21="si"),
        Fact(question_22="si"))
    def disorder_10(self):
        self.declare(Fact(disorder="Depresión Mayor Grave"))
        return("Depresión Mayor Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_7="si"),
        Fact(question_9="si"),
        Fact(question_23="si"),
        Fact(question_24="si"),
        Fact(question_25="si"))
    def disorder_11(self):
        self.declare(Fact(disorder="Depresión Neurótica Moderado"))
        return("Depresión Neurótica Moderado")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_7="si"),
        Fact(question_9="si"),
        Fact(question_23="si"),
        Fact(question_24="si"),
        Fact(question_25="si"),
        Fact(question_26="si"),
        Fact(question_27="si"))
    def disorder_12(self):
        self.declare(Fact(disorder="Depresión Neurótica Grave"))
        return("Depresión Neurótica Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_26="si"),
        Fact(question_27="si"))
    def disorder_13(self):
        self.declare(Fact(disorder="Depresión Neurótica Grave"))
        return("Depresión Neurótica Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_28="si"),
        Fact(question_29="si"),
        Fact(question_30="si"),
        Fact(question_31="si"),
        Fact(question_32="si"))
    def disorder_14(self):
        self.declare(Fact(disorder="Depresión Existencial"))
        return("Depresión Existencial")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_22="si"),
        Fact(question_33="si"),
        Fact(question_34="si"),
        Fact(question_35="si"),
        Fact(question_36="si"))
    def disorder_15(self):
        self.declare(Fact(disorder="Depresión Psicótica"))
        return("Depresión Psicótica")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_2="si"),
        Fact(question_3="si"),
        Fact(question_4="si"),
        Fact(question_5="si"),
        Fact(question_6="si"),
        Fact(question_9="si"),
        Fact(question_15="si"),
        Fact(question_27="si"),
        Fact(question_37="si"))
    def disorder_16(self):
        self.declare(Fact(disorder="Depresión Endógena"))
        return("Depresión Endógena")
engine = DiagnosisOfDepressiveDisorder()



    #---------------------------------------------------------------------
    # Rules to find depressive disorder: Symptom questions and y/n answers
    #---------------------------------------------------------------------




    # esto es de lo anterior
'''
    @Rule(Fact(action='greetj'),
        NOT(Fact(patient_name=W())))
    def ask_patient_name(self):
        self.declare(Fact(patient_name=input("Patient's name? ")))

    @Rule(Fact(action='greet'),
        NOT(Fact(psychologist_name=W())))
    def ask_psychologist_name(self):
        self.declare(Fact(psychologist_name=input("Doctor's name? ")))


    @Rule(Fact(action='greet'),
        Fact(patient_name=MATCH.patient_name),
        Fact(psychologist_name=MATCH.psychologist_name))
    def greet(self, patient_name, psychologist_name):
        print("Hi %s! I'm %s your psychologist and I'll be helping you" % (patient_name, psychologist_name))
    
'''
