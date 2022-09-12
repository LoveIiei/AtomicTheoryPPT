from tkinter import font
from tkinter.font import BOLD, families
from PIL import ImageTk, Image
import tkinter as tk
from tkinter.ttk import *
import os


path = os.getcwd()
#change the chemisty into the new folder name, 
#or comment next line in case a change occured. 
dirpath = "{}".format(path) + '/assets'
CitationPath = path + '/citations'
class Chemistry(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Main Page")
        self.master.geometry('1460x750+0+0')
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Made by Owen Hua & Ben Weber-Kramer", font=('Comic Sans MS',26), bg="green").pack(side="bottom")
        self.photo1 = ImageTk.PhotoImage(Image.open("{}/bg0.png".format(dirpath),"r"))
        tk.Label(self, image=self.photo1).pack(side="bottom", fill="both")
        tk.Button(self, text="Go to timeline", font=('Comic Sans MS',26), bg="orange", fg="green", padx=30, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=1035,y=250)
    

class menu(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Timeline")
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Timeline of Atomic Theories", font=('Comic Sans MS',32), fg="red").pack(side="top", fill="x", pady=10)
        self.photo2 = ImageTk.PhotoImage(Image.open("{}/bg3.png".format(dirpath)))
        tk.Label(self, image=self.photo2).pack(side="bottom", fill="both", expand='YES')
        tk.Button(self, text="Democritus", padx=20, pady=10,
                  command=lambda: master.switch_frame(Democritus)).place(x=20,y=520)
        self.photo3 = ImageTk.PhotoImage(Image.open("{}/demo1.png".format(dirpath)))
        tk.Label(self, image=self.photo3).place(x=0,y=100)
        tk.Label(self, text="450 BCE", font=('Comic Sans MS',26), bg="red").place(x=20,y=640)
        tk.Label(self, text=" -> ").place(x=147,y=650)
        tk.Button(self, text="John Dalton", padx=20, pady=10,
                  command=lambda: master.switch_frame(John_Dalton)).place(x=160,y=520)
        self.photo4 = ImageTk.PhotoImage(Image.open("{}/demo2.png".format(dirpath)))
        tk.Label(self, image=self.photo4).place(x=201,y=100)
        tk.Label(self, text="1808", font=('Comic Sans MS',26), bg="orange").place(x=190,y=640)
        tk.Label(self, text=" -> ").place(x=270,y=650)
        tk.Button(self, text="J.J.Thomson", padx=20, pady=10,
                  command=lambda: master.switch_frame(JJ_Thomson)).place(x=300,y=520)
        self.photo5 = ImageTk.PhotoImage(Image.open("{}/plum.jpeg".format(dirpath)))
        tk.Label(self, image=self.photo5).place(x=420,y=100)
        tk.Label(self, text="1895", font=('Comic Sans MS',26), bg="yellow").place(x=320,y=640)
        tk.Label(self, text=" -> ").place(x=412,y=650)
        tk.Button(self, text="Ernest Rutherford", padx=20, pady=10,
                  command=lambda: master.switch_frame(Ernest_Rutherford)).place(x=440,y=520)
        self.photo6 = ImageTk.PhotoImage(Image.open("{}/nuclear.jpeg".format(dirpath)))
        tk.Label(self, image=self.photo6).place(x=780,y=100)
        tk.Label(self, text="1903", font=('Comic Sans MS',26), bg="green").place(x=480,y=640)
        tk.Label(self, text=" -> ").place(x=585,y=650)
        tk.Button(self, text="Neils Bohr", padx=20, pady=10,
                  command=lambda: master.switch_frame(Neils_Bohr)).place(x=610,y=520)
        self.photo7 = ImageTk.PhotoImage(Image.open("{}/borh.png".format(dirpath)))
        tk.Label(self, image=self.photo7).place(x=1045,y=100)
        tk.Label(self, text="1913", font=('Comic Sans MS',26), bg="cyan").place(x=640,y=640)
        tk.Label(self, text=" -> ").place(x=715,y=650)
        tk.Button(self, text="James Chadwick", padx=20, pady=10,
                  command=lambda: master.switch_frame(James_Chadwick)).place(x=740,y=520)
        self.photo8 = ImageTk.PhotoImage(Image.open("{}/quantum.png".format(dirpath)))
        tk.Label(self, image=self.photo8).place(x=201,y=240)
        tk.Label(self, text="1932", font=('Comic Sans MS',26), bg="blue").place(x=785,y=640)
        tk.Label(self, text=" -> ").place(x=890,y=650)
        tk.Button(self, text="Louis de Broglie", padx=20, pady=10,
                  command=lambda: master.switch_frame(Louis_de_Broglie)).place(x=910,y=520)
        self.photo9 = ImageTk.PhotoImage(Image.open("{}/sequantum.png".format(dirpath)))
        tk.Label(self, image=self.photo9).place(x=360,y=240)          
        tk.Label(self, text="193O to present", font=('Comic Sans MS',26), bg="purple").place(x=940,y=640)
        tk.Label(self, text=" -> ").place(x=1165,y=650)
        tk.Label(self, text=" -> ").place(x=1275,y=650)
        tk.Label(self, text=" -> ").place(x=1380,y=650)
        tk.Button(self, text="Erwin Schrodinger", padx=20, pady=10,
                  command=lambda: master.switch_frame(Erwin_Schrodinger)).place(x=1073,y=520)
        tk.Button(self, text="Werner Heisenberg", padx=20, pady=10,
                  command=lambda: master.switch_frame(Werner_Heisenberg)).place(x=1250,y=520)

class Democritus(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Democritus")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self,  
        text="Democritus was living about 460 BCE - 380 BCE. He was a citizen of Abdera,"\
             "and once worked as a philosopher."\
             "\n"\
             "Democritus believed that atoms were uniform, solid, hard, incompressible,"\
             "\n"\
             "and indestructible and that they moved in infinite numbers through empty space"\
             " until stopped."\
             "\n"\
             "Differences in atomic shape and size determined the various properties of matter."\
             "\n"\
             "In Democritus's philosophy, atoms existed not only for matter"\
             "\n"\
             "but also for such qualities as perception and the human soul."\
             , font=('Comic Sans MS',22)).place(x=250, y=350)
        self.image10 = ImageTk.PhotoImage(Image.open("{}/apa1.png".format(CitationPath)))
        tk.Label(self, image=self.image10).place(x=50,y=550)
        self.image11 = ImageTk.PhotoImage(Image.open("{}/democr1.png".format(dirpath)))
        tk.Label(self, image=self.image11).place(x=50,y=25)
        self.image12 = ImageTk.PhotoImage(Image.open("{}/democr2.jpeg".format(dirpath)))
        tk.Label(self, image=self.image12).place(x=800,y=25)
        self.image13 = ImageTk.PhotoImage(Image.open("{}/democr3.jpeg".format(dirpath)))
        tk.Label(self, image=self.image13).place(x=1120,y=25)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Next Person", padx=20, pady=10,
                  command=lambda: master.switch_frame(John_Dalton)).place(x=1300, y=680)
        #tk.Button(self, text="Previous", padx=20, pady=10,
                  #command=lambda: master.switch_frame(John_Dalton)).place(x=20, y=680)
                
class John_Dalton(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("John Dalton")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self, 
        text=
        "John Dalton lived between 1766-1844, his father was a weaver, and he was once a teacher.\n"
        +"John Dalton is best known for what became known as Dalton's law, which concludes that the\n"
        +"total pressure of a gaseous mixture is equal to the sum of the partial pressures of the\n"
        +"individual component gasses, partial pressure being the pressure that each gas would exert\n"
        +"alone within the volume of the mixture at the same temperature. His model for that is called a\n" 
        +"Billiard ball which looks like a solid, hard sphere.\n\n"
        +"He also has an idea that like atoms repel one another, whereas unlike atoms appear to react\n"
        +"indifferently. Even though this is wrong, it still helps to explain why each gas acts independently\n"
        +"in a mixture and helps him with his law that all atoms are different. His other law of multiple\n"
        +"proportions is very critical because it states that when two elements form more than one compound, masses\n" 
        +"of one element that combine with a fixed mass of the other are in a ratio of small whole numbers." 
        ,font=('Comic Sans MS',22)).place(x=320,y=210)
        self.image14 = ImageTk.PhotoImage(Image.open("{}/apa2.png".format(CitationPath)))
        tk.Label(self, image=self.image14).place(x=175,y=20)
        self.image15 = ImageTk.PhotoImage(Image.open("{}/dal1.png".format(dirpath)))
        tk.Label(self, image=self.image15).place(x=10,y=170)
        self.image16 = ImageTk.PhotoImage(Image.open("{}/dal2.png".format(dirpath)))
        tk.Label(self, image=self.image16).place(x=10,y=450)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Next Person", padx=20, pady=10,
                  command=lambda: master.switch_frame(JJ_Thomson)).place(x=1300, y=680)
        tk.Button(self, text="Previous", padx=20, pady=10,
                  command=lambda: master.switch_frame(Democritus)).place(x=20, y=680)

class JJ_Thomson(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("J.J.Thomson")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self, text=
        "J.J.Thomson was living between 1856-1940, and he won a Noble prize in physics for the electrical\n"
        +"conductivity of gasses in 1906 and was knighted in 1908. In 1903, he suggested a discontinuous\n"
        +"theory of light, foreshadowing Albert Einstein's later theory of photons. He later discovered\n"
        +"isotopes and invented mass spectrometry.\n\n"
        +"J.J.Thomson did the cathode Ray Tube Experiment in which he found electrons using a cathode ray tube.\n"
        +"He zapped atoms with electricity and observed that negatively charged particles were removed.\n"
        +"He reasoned that atoms consisted of subatomic particles; electrons that were negatively charged particles.\n"
        +"Additionally, he also studied positively charged particles in neon gas.\n\n"
        +"J.J.Thomson has a model called the Plum Pudding Model, which states: The atom is a positively charged sphere, in which \n"
        +"negatively electrons are embedded. Basically, electrons are like blueberries inside a muffin, which represents protons."
        ,font=('Comic Sans MS',22)).place(x=20,y=200)
        self.image17 = ImageTk.PhotoImage(Image.open("{}/apa3.png".format(CitationPath)))
        tk.Label(self, image=self.image17).place(x=115,y=30)
        self.image18 = ImageTk.PhotoImage(Image.open("{}/jj2.jpeg".format(dirpath)))
        tk.Label(self, image=self.image18).place(x=1250,y=175)
        self.image19 = ImageTk.PhotoImage(Image.open("{}/jj1.png".format(dirpath)))
        tk.Label(self, image=self.image19).place(x=1250,y=460)
        self.image39 = ImageTk.PhotoImage(Image.open("{}/jj3.png".format(dirpath)))
        tk.Label(self, image=self.image39).place(x=250,y=570)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Next Person", padx=20, pady=10,
                  command=lambda: master.switch_frame(Ernest_Rutherford)).place(x=1300, y=680)
        tk.Button(self, text="Previous", padx=20, pady=10,
                  command=lambda: master.switch_frame(John_Dalton)).place(x=20, y=680)

class Ernest_Rutherford(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Ernest Rutherford")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self, text=
        "Ernest Rutherford was born on August 30, 1871 in New Zealand and died on October 19, 1937. He graduated with\n"
        +"a M.A, with a double firsts in math and science in 1893. Because of his academic performance, he was awarded\n" 
        +"with the 1851 Exhibition Science Scholarship which allowing him to go to Trinity College to work under J.J. Thomson.\n\n"
        +"In 1911 he was experimenting with the scattering of alpha particles and rays. This led him to send a beam\n"
        +"of alpha particles through gold foil. Most of the particles passed through while some bounced back which\n"
        +"led him to believe that the atom is mostly empty space surrounding the nucleus.\n\n"
        +"His greatest contribution to science is that he found the nuclear model of the atom. Contained inside the\n"
        +"nuclear atom, are the protons and neutrons, which consist of nearly all of the mass of the atom, which are\n"
        +"located in the nucleus at the center of the atom. The electrons are placed around the nucleus and occupy most of the atom."
        ,font=('Comic Sans MS',22)).place(x=180,y=165)
        self.image20 = ImageTk.PhotoImage(Image.open("{}/apa4.png".format(CitationPath)))
        tk.Label(self, image=self.image20).place(x=180,y=25)
        self.image21 = ImageTk.PhotoImage(Image.open("{}/er4.png".format(dirpath)))
        tk.Label(self, image=self.image21).place(x=130,y=520)
        self.image22 = ImageTk.PhotoImage(Image.open("{}/er2.png".format(dirpath)))
        tk.Label(self, image=self.image22).place(x=5,y=250)
        self.image23 = ImageTk.PhotoImage(Image.open("{}/er3.png".format(dirpath)))
        tk.Label(self, image=self.image23).place(x=900,y=600)
        self.image40 = ImageTk.PhotoImage(Image.open("{}/er1.png".format(dirpath)))
        tk.Label(self, image=self.image40).place(x=1130,y=600)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Next Person", padx=20, pady=10,
                  command=lambda: master.switch_frame(Neils_Bohr)).place(x=1300, y=680)
        tk.Button(self, text="Previous", padx=20, pady=10,
                  command=lambda: master.switch_frame(JJ_Thomson)).place(x=20, y=680)

class James_Chadwick(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("James Chadwick")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self, text=
        "James Chadwick was born in Cheshire England on October 20th 1891 and died on July 24, 1974. He attended\n"
        +"Manchester University and worked under Rutherford until 1913 when he got his M.Sc. degree, after WWI,\n" 
        +"he returned to England, and helped Rutherford with his work.\n\n"
        +"In 1932 he made the discovery of the neutron by using charged alpha rays which were repelled by the\n"
        +"electrical forces present in the nucleus. He used alpha particles from the natural radioactive decay\n"
        +"of Polonium on Beryllium. The resulting radiation showed high penetration through a lead shield.\n"
        +"This made him realize that a neutron does not have a charge at all. He also found that protons and\n"
        +"neutrons are held together by electrostatic forces (opposite charges attract). So he concluded that\n" 
        +"the nucleus contained both protons and neutrons.\n"
        ,font=('Comic Sans MS',22)).place(x=60,y=245)
        self.image24 = ImageTk.PhotoImage(Image.open("{}/apa5.png".format(CitationPath)))
        tk.Label(self, image=self.image24).place(x=75,y=60)
        self.image25 = ImageTk.PhotoImage(Image.open("{}/ja1.png".format(dirpath)))
        tk.Label(self, image=self.image25).place(x=1200,y=200)
        self.image26 = ImageTk.PhotoImage(Image.open("{}/ja2.jpeg".format(dirpath)))
        tk.Label(self, image=self.image26).place(x=1185,y=440)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Next Person", padx=20, pady=10,
                  command=lambda: master.switch_frame(Louis_de_Broglie)).place(x=1300, y=680)
        tk.Button(self, text="Previous", padx=20, pady=10,
                  command=lambda: master.switch_frame(Neils_Bohr)).place(x=20, y=680)

class Neils_Bohr(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Neils Bohr")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self, text=
        "Neils Bohr was born in 1885 October 7 in Copenhagen. Bohr went to Copengagen university\n"
        +"where he received a Masters in Physics in 1909, and a Doctor's degree in 1911. While\n"
        +"working he found some issues in Planck's quantum theory of radiation. With this information\n"
        +"he moved to Cambridge in 1911 and worked under J.J Thomson. Then in 1912 he worked\n"
        +"under Ernest Rutherford. In 1913 he took Planck's Quantum Theory and worked out a more\n"
        +"present picture of the atom. He received the Nobel Prize in 1922 along with a long list of\n"
        +"accolades as well. He died in 1962 on November 18.\n\n"
        +"Neils Bohr proposed a theory for the Hydrogen atom that was based on quantum theory that\n"
        +"some physical quantities only take discrete values. Electrons move around the nucleus but\n"
        +"only in prescribed orbits. Also if an electron jumps to a lower energy orbit the difference\n"
        +"is set out as radiation. Neils Bohr's model for the atom was the first model to use quantum\n"
        +"theory. He proposed that electrons could be in certain orbits around the nucleus. These electrons\n"
        +"were also very limited to the specific orbits around the nucleus as well."
        ,font=('Comic Sans MS',22)).place(x=340,y=210)
        self.image27 = ImageTk.PhotoImage(Image.open("{}/apa6.png".format(CitationPath)))
        tk.Label(self, image=self.image27).place(x=35,y=45)
        self.image28 = ImageTk.PhotoImage(Image.open("{}/ne1.png".format(dirpath)))
        tk.Label(self, image=self.image28).place(x=10,y=200)
        self.image29 = ImageTk.PhotoImage(Image.open("{}/ne2.png".format(dirpath)))
        tk.Label(self, image=self.image29).place(x=10,y=440)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Next Person", padx=20, pady=10,
                  command=lambda: master.switch_frame(James_Chadwick)).place(x=1300, y=680)
        tk.Button(self, text="Previous", padx=20, pady=10,
                  command=lambda: master.switch_frame(Ernest_Rutherford)).place(x=20, y=680)

class Erwin_Schrodinger(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Erwin Schrodinger")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self, text=
        "Erwin Schrodinger was born on August 12 1887, in Vienna. From 1906-1910 he went to the\n"
        +"University of Vienna. It was here that he mastered eigenvalue problems in the physics\n"
        +"of continuous media, this helped him make his great discovery. Schrodinger was displeased\n"
        +"with Bohr's orbit theory and believed that atomic spectra should really be determined by\n"
        +"some eigenvalue problem. In 1926 he made a great discovery and formulated a wave equation.\n"
        +"In 1933 he received a Nobel Prize for his work. After he retired he went back to Vienna with\n"
        +"his wife where he died on January 4th, 1961.\n\n"
        +"Since Broglie proposed that electrons could have wave-like behavior, Erwin Schrodinger\n"
        +"theorized that the behavior of electrons could be explained by treating them mathematically\n"
        +"as matter waves. He then formulated a wave equation that would accurately calculate the\n"
        +"energy levels of electrons in atoms.\n\n"
        +"Erwin Schrödinger found that the quantization of the hydrogen atom's energy levels that\n"
        +"appeared in Bohr's atomic model could be found from his wave equation, which describes\n"
        +"how the wave function of a quantum mechanical system evolves."
        ,font=('Comic Sans MS',22)).place(x=85,y=170)
        self.image30 = ImageTk.PhotoImage(Image.open("{}/apa7.png".format(CitationPath)))
        tk.Label(self, image=self.image30).place(x=75,y=20)
        self.image31 = ImageTk.PhotoImage(Image.open("{}/sc1.jpeg".format(dirpath)))
        tk.Label(self, image=self.image31).place(x=1180,y=180)
        self.image32 = ImageTk.PhotoImage(Image.open("{}/sc2.png".format(dirpath)))
        tk.Label(self, image=self.image32).place(x=1165,y=420)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Next Person", padx=20, pady=10,
                  command=lambda: master.switch_frame(Werner_Heisenberg)).place(x=1300, y=680)
        tk.Button(self, text="Previous", padx=20, pady=10,
                  command=lambda: master.switch_frame(Louis_de_Broglie)).place(x=20, y=680)

class Louis_de_Broglie(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Louis de Broglie")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self, text=
        "Louis de Broglie was born on the 15th of August 1892 in France. Before he got to do anything\n"
        +"with his science degree he was enlisted in the war. He would often spend many nights during\n"
        +"his service theorizing and studying. When the war ended he went to the University of Paris.\n"
        +"He worked there where he developed an interest in experimental work. In 1924 he delivered\n"
        +"his quantum theory which gained him a Doctors degree. Throughout his life he continued\n"
        +"working on his theory and thesis. He received a Nobel Prize in 1929 along with many other\n"
        +"awards. His significance on quantum mechanics was monumental. He died March 19 in 1987.\n\n"
        +"In 1924 Louis de Broglie proposed his quantum theory. He said that electrons could not only\n"
        +"be a particle but also a wave. He wanted to describe electrons as particles and waves based\n"
        +"on the wave nature of an electron. He realized this when streams of electrons would be\n"
        +"reflected against crystals and spread onto thin metal foils.\n\n"
        +"In 1924 Broglie postulated wave particle duality for the electron, thereby providing the\n"
        +"opportunity to remove some of the things from Bohr's model. The de Broglie Bohr model of\n"
        +"the hydrogen atom treats the electron as a particle on a ring with wave like properties."
        ,font=('Comic Sans MS',22)).place(x=340,y=180)
        self.image33 = ImageTk.PhotoImage(Image.open("{}/apa8.png".format(CitationPath)))
        tk.Label(self, image=self.image33).place(x=35,y=40)
        self.image34 = ImageTk.PhotoImage(Image.open("{}/lo1.jpeg".format(dirpath)))
        tk.Label(self, image=self.image34).place(x=20,y=200)
        self.image35 = ImageTk.PhotoImage(Image.open("{}/lo2.jpeg".format(dirpath)))
        tk.Label(self, image=self.image35).place(x=20,y=440)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Next Person", padx=20, pady=10,
                  command=lambda: master.switch_frame(Erwin_Schrodinger)).place(x=1300, y=680)
        tk.Button(self, text="Previous", padx=20, pady=10,
                  command=lambda: master.switch_frame(James_Chadwick)).place(x=20, y=680)

class Werner_Heisenberg(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Werner Heisenberg")
        tk.Frame.__init__(self, master, width=1460, height=780)
        tk.Label(self, text=
        "Werner Heisenbreg was born on December 5th in 1901, in Germany. After he got his Ph.D. in\n"
        +"University of Munich. In 1925 he worked with Neils Bohr at the University of Copenhagen.\n"
        +"Then in the same year he formulated a type of quantum mechanics based on matrices. Under\n"
        +"Bohr in 1927 he realized the uncertainty relation. He did all of this at 26. He received\n"
        +"a Nobel Prize for physics in 1932. He was married and had seven children and also loved\n"
        +"classical music. He passed away in 1976 on February 1st.\n\n"
        +"Werner Heisenberg contributed to atomic theory by formulating quantum mechanics in terms\n"
        +"of matrices and by finding the uncertainty principle. This stateed that a particle's position\n"
        +"and momentum cannot both be known exactly because of small errors on the human scale, but\n"
        +"these errors can't be ignored when studying the atom.\n\n"
        +"Heisenberg introduced that the electron's position and momentum can never be determined\n"
        +"accurately, this was called the uncertainty principle. This was in contradiction to Bohr's\n"
        +"theory. The uncertainty principle contributed to the development of quantum mechanics which\n"
        +"is why it is called the quantum mechanical model of the atom."
        ,font=('Comic Sans MS',22)).place(x=85, y=170)
        self.image36 = ImageTk.PhotoImage(Image.open("{}/apa9.png".format(CitationPath)))
        tk.Label(self, image=self.image36).place(x=60,y=20)
        self.image37 = ImageTk.PhotoImage(Image.open("{}/we1.png".format(dirpath)))
        tk.Label(self, image=self.image37).place(x=1180,y=180)
        self.image38 = ImageTk.PhotoImage(Image.open("{}/we2.jpeg".format(dirpath)))
        tk.Label(self, image=self.image38).place(x=1165,y=420)
        tk.Button(self, text="Return to timeline menu", padx=20, pady=10,
                  command=lambda: master.switch_frame(menu)).place(x=650, y=680)
        tk.Button(self, text="Quit", padx=20, pady=10,
                  command=self.master.destroy).place(x=1300, y=680)
        tk.Button(self, text="Citation", padx=20, pady=10, background="green",
                  command=lambda: master.switch_frame(Citation1)).place(x=1050, y=680)
        tk.Button(self, text="Previous", padx=20, pady=10,
                  command=lambda: master.switch_frame(Erwin_Schrodinger)).place(x=20, y=680)

class Citation1(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Citation")
        self.master.geometry('3840x2160+0+0')
        tk.Frame.__init__(self, master, width=3840, height=2160)
        self.image42 = ImageTk.PhotoImage(Image.open("{}/apa11.png".format(CitationPath)))
        tk.Label(self, image=self.image42).place(x=0,y=0)
        tk.Button(self, text="Next Page", padx=50, pady=50,
                  command=lambda: master.switch_frame(Citation2)).place(x=1350, y=750)
        tk.Button(self, text="Quit", padx=50, pady=50, fg="red", font=('Comic Sans MS',20),
                  command=self.master.destroy).place(x=1500, y=750)

class Citation2(tk.Frame):
    def __init__(self, master):
        self.master = master
        self.master.title("Citation")
        self.master.geometry('3840x2160+0+0')
        tk.Frame.__init__(self, master, width=3840, height=2160)
        self.image41 = ImageTk.PhotoImage(Image.open("{}/apa10.png".format(CitationPath)))
        tk.Label(self, image=self.image41).place(x=0,y=0)
        tk.Button(self, text="Quit", padx=50, pady=50, fg="red", font=('Comic Sans MS',26),
                  command=self.master.destroy).place(x=1500, y=750)


if __name__ == "__main__":
    app = Chemistry()
    app.mainloop()
