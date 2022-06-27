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
    
        

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_1=W())), salience=37)
    def symptom_1(self, rpta):
        print("1. ¿Estás deprimido (a) por alguna situación de tu vida?")
        self.declare(Fact(question_1 = rpta))
        print("rpta1: "+ rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_2=W())), salience=36)
    def symptom_2(self, rpta):
        print("2. ¿Tienes muy poco sueño?: ")
        self.declare(Fact(question_2 = rpta))
        print("rpta2: "+ rpta)
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_3=W())), salience=35)
    def symptom_3(self):
        self.declare(Fact(question_3 = input("3. ¿Sientes fatiga o pierdes la energía casi a diario?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_4=W())), salience=34)
    def symptom_4(self):
        self.declare(Fact(question_4 = input("4. ¿Tienes baja autoestima?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_5=W())), salience=33)
    def symptom_5(self):
        self.declare(Fact(question_5 = input("5. ¿Comes muy poco?: ")))

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_6=W())), salience=32)
    def symptom_6(self):
        self.declare(Fact(question_6 = input("6. ¿Tienes problemas de memoria, atención y concentración?: ")))

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_7=W())), salience=31)
    def symptom_7(self):
        self.declare(Fact(question_7 = input("7. ¿Tienes pensamiento de que todo sale mal?: ")))

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_8=W())), salience=30)
    def symptom_8(self):
        self.declare(Fact(question_8 = input("8. ¿Ves el futuro negativamente?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_9=W())), salience=29)
    def symptom_9(self):
        self.declare(Fact(question_9 = input("9. ¿Tienes pensamientos negativos?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_10=W())), salience=28)
    def symptom_10(self):
        self.declare(Fact(question_10 = input("10. ¿Te desanimas con facilidad?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_11=W())), salience=27)
    def symptom_11(self):
        self.declare(Fact(question_11 = input("11. ¿Tienes pensamientos suicidas?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_12=W())), salience=26)
    def symptom_12(self):
        self.declare(Fact(question_12 = input("12. ¿Tienes pensamientos de hacerte daño?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_13=W())), salience=25)
    def symptom_13(self):
        self.declare(Fact(question_13 = input("13. ¿No quieres conversar con nadie?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_14=W())), salience=24)
    def symptom_14(self):
        self.declare(Fact(question_14 = input("14. ¿No quieres salir a ningún lado?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_15=W())), salience=23)
    def symptom_15(self):
        self.declare(Fact(question_15 = input("15. ¿Te sientes triste o vacío?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_16=W())), salience=22)
    def symptom_16(self):
        self.declare(Fact(question_16 = input("16. ¿Te sientes a veces o siempre irritable?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_17=W())), salience=21)
    def symptom_17(self):
        self.declare(Fact(question_17 = input("17. ¿Has perdido o aumentado 5'%' de tu peso corporal?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_18=W())), salience=20)
    def symptom_18(self):
        self.declare(Fact(question_18 = input("18. ¿Presentas insomnio casi a diario?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_19=W())), salience=19)
    def symptom_19(self):
        self.declare(Fact(question_19 = input("19. ¿Te agitas en actividades psicomotoras?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_20=W())), salience=18)
    def symptom_20(self):
        self.declare(Fact(question_20 = input("20. ¿Presentas sensación de inutilidad y confusión?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_21=W())), salience=17)
    def symptom_21(self):
        self.declare(Fact(question_21 = input("21. ¿Has perdido a un ser querido recientemente?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_22=W())), salience=16)
    def symptom_22(self):
        self.declare(Fact(question_22 = input("22. ¿Tienes alucinaciones?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_23=W())), salience=15)
    def symptom_23(self):
        self.declare(Fact(question_23 = input("23. ¿Estás pasando por algún problema?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_24=W())), salience=14)
    def symptom_24(self):
        self.declare(Fact(question_24 = input("24. ¿Piensas que no tienes suerte en tu vida?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_25=W())), salience=13)
    def symptom_25(self):
        self.declare(Fact(question_25 = input("25. ¿Todos los síntomas se presentan de vez en cuando?: ")))

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_26=W())), salience=12)
    def symptom_26(self):
        self.declare(Fact(question_26 = input("26. ¿Todos los síntomas se presentan todos los días?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_27=W())), salience=11)
    def symptom_27(self):
        self.declare(Fact(question_27 = input("27. ¿Estás muy estresado?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_28=W())), salience=10)
    def symptom_28(self):
        self.declare(Fact(question_28 = input("28. ¿Sientes que tu vida no tiene sentido?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_29=W())), salience=9)
    def symptom_29(self):
        self.declare(Fact(question_29 = input("29. ¿Te sientes agotado y con miedo?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_30=W())), salience=8)
    def symptom_30(self):
        self.declare(Fact(question_30 = input("30. ¿Sufres de falta de motivación para realizar tus cosas cotidianas?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_31=W())), salience=7)
    def symptom_31(self):
        self.declare(Fact(question_31 = input("31. ¿No tienes pasión por nada?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_32=W())), salience=6)
    def symptom_32(self):
        self.declare(Fact(question_32 = input("32. ¿Tienes ganas de dormir en el día?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_33=W())), salience=5)
    def symptom_33(self):
        self.declare(Fact(question_33 = input("33. ¿Te encuentras en un estado de ilusión?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_34=W())), salience=4)
    def symptom_34(self):
        self.declare(Fact(question_34 = input("34. ¿Escuchas voces en la cabeza?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_35=W())), salience=3)
    def symptom_35(self):
        self.declare(Fact(question_35 = input("35. ¿Eres muy impulsivo (a)?: ")))
    
    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_36=W())), salience=2)
    def symptom_36(self):
        self.declare(Fact(question_36 = input("36. ¿Eres muy nervioso (a)?: ")))

    @Rule(Fact(action='find_depressive_disorder'), NOT(Fact(question_37=W())), salience=1)
    def symptom_37(self):
        self.declare(Fact(question_37 = input("37. ¿Tienes sentimiento de miedo e inseguridad?: ")))
    



    #---------------------------------------------------------------------------------------
    # Response validation to find the depression disorder
    #---------------------------------------------------------------------------------------


    @Rule(Fact(action="find_depressive_disorder"), Fact(question_1="si"), Fact(question_2="si"), Fact(question_3="si"), Fact(question_4="si"), Fact(question_5="si"))
    def disorder_1(self):
        self.declare(Fact(disorder="Depresión distimia leve"))
        print("Depresión distimia levelll")

    @Rule(Fact(action="find_depressive_disorder"), Fact(question_6="si"), Fact(question_7="si"), Fact(question_8="si"), Fact(question_9="si"), Fact(question_10="si"))
    def disorder_2(self):
        self.declare(Fact(disorder="Depresión distimia moderado"))
        print("Depresión distimia moderado")
        
    @Rule(Fact(action="find_depressive_disorder"), Fact(question_1="si"), Fact(question_2="si"), Fact(question_3="si"), Fact(question_4="si"), Fact(question_5="si"), Fact(question_6="si"), Fact(question_7="si"), Fact(question_8="si"), Fact(question_9="si"), Fact(question_10="si"))
    def disorder_3(self):
        self.declare(Fact(disorder="Depresión distimia moderado"))
        print("Depresión distimia moderado")
    

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
        print("Depresión Distimia Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_11="si"), 
        Fact(question_12="si"), 
        Fact(question_13="si"), 
        Fact(question_14="si"))
    def disorder_5(self):
        self.declare(Fact(disorder="Depresión Distimia Grave"))
        print("Depresión Distimia Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_3="si"), 
        Fact(question_15="si"), 
        Fact(question_16="si"), 
        Fact(question_19="si"))
    def disorder_6(self):
        self.declare(Fact(disorder="Depresión Mayor Leve"))
        print("Depresión Mayor Leve")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_3="si"), 
        Fact(question_15="si"), 
        Fact(question_16="si"), 
        Fact(question_18="si"),
        Fact(question_19="si"),
        Fact(question_20="si"))
    def disorder_7(self):
        self.declare(Fact(disorder="Depresión Mayor Moderado"))
        print("Depresión Mayor Moderado")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_18="si"),
        Fact(question_20="si"))
    def disorder_8(self):
        self.declare(Fact(disorder="Depresión Mayor Moderado"))
        print("Depresión Mayor Moderado")


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
        print("Depresión Mayor Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_6="si"),
        Fact(question_11="si"),
        Fact(question_17="si"),
        Fact(question_21="si"),
        Fact(question_22="si"))
    def disorder_10(self):
        self.declare(Fact(disorder="Depresión Mayor Grave"))
        print("Depresión Mayor Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_7="si"),
        Fact(question_9="si"),
        Fact(question_23="si"),
        Fact(question_24="si"),
        Fact(question_25="si"))
    def disorder_11(self):
        self.declare(Fact(disorder="Depresión Neurótica Moderado"))
        print("Depresión Neurótica Moderado")


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
        print("Depresión Neurótica Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_26="si"),
        Fact(question_27="si"))
    def disorder_13(self):
        self.declare(Fact(disorder="Depresión Neurótica Grave"))
        print("Depresión Neurótica Grave")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_28="si"),
        Fact(question_29="si"),
        Fact(question_30="si"),
        Fact(question_31="si"),
        Fact(question_32="si"))
    def disorder_14(self):
        self.declare(Fact(disorder="Depresión Existencial"))
        print("Depresión Existencial")


    @Rule(Fact(action="find_depressive_disorder"), 
        Fact(question_22="si"),
        Fact(question_33="si"),
        Fact(question_34="si"),
        Fact(question_35="si"),
        Fact(question_36="si"))
    def disorder_15(self):
        self.declare(Fact(disorder="Depresión Psicótica"))
        print("Depresión Psicótica")


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
        print("Depresión Endógena")






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
