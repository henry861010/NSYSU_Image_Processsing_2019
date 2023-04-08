import numpy as np         
import cv2                 
import tkinter as tk
from PIL import ImageTk, Image
from scipy import ndimage
##########################
love=1
class black():        
      def __init__(self,image):
           self.image=image
      def upatenewimageintoobject(self,photo):          #把資料傳送到物件中的method
          self.image=photo
      def aaaa(self,cdf):
          self.image=self.image.astype(int)
          self.image=cdf[self.image]

      def homomorphicfilter(self,rl,rh,do,c):
            f=photo
            f=f+0.1
            z=np.log(f)
            zft = np.fft.fft2(z)
            zft=np.fft.fftshift(zft)
            sft=np.zeros((zft.shape[0],zft.shape[1]))
            for i in range(0,zft.shape[0]):
                 for j in range(0,zft.shape[1]):
                      u=i-zft.shape[0]/2
                      v=j-zft.shape[1]/2
                      sft[i,j]=((rh-rl)*(1-np.exp(-c*(u**2+v**2)/do**2))+rl)
            sft=sft*zft
            sft=np.fft.ifftshift(sft)
            s=np.fft.ifft2(sft)
            s=np.real(s)
            g=np.exp(s)/1
            for i in range(0,zft.shape[0]):
                 for j in range(0,zft.shape[1]):
                      if g[i,j]>255:
                           g[i,j]=255
                      elif g[i,j]<0:
                           g[i,j]=0
            self.image=g.astype(np.uint8)



#-------------------------
window=tk.Tk()
window.title('影像處理_hw1_b053022040')
window.geometry('1300x600')

imgcv=np.array([[1]])#初始的圖片,並把他轉為PIL接受的形式
photo1 = ImageTk.PhotoImage(image = Image.fromarray(np.uint8(imgcv)))
canvas = tk.Canvas(window)                                  
ii=canvas.create_image(0, 0, image=photo1,anchor=tk.NW)         
canvas.place(x=300,y=30)
canvas1 = tk.Canvas(window)                                  
iii=canvas1.create_image(0, 0, image=photo1,anchor=tk.NW)        
canvas1.place(x=600,y=30)
IMAGE=black(photo1)
#---------------------------
def update():                                                  #將影像更新為所輸入地址影像
     global photo  
     global img
     global abcd    
     photo=cv2.imread(entry.get(),cv2.IMREAD_GRAYSCALE)
     abcd=int(photo.shape[1]/photo.shape[0]*250)
     photo=cv2.resize(photo,(abcd,250))
     img=ImageTk.PhotoImage(image=Image.fromarray(np.uint8(photo)))
     canvas.config(heigh=abcd,width=250)
     canvas.itemconfig(ii,image =img,anchor=tk.NW)
     canvas1.config(heigh=abcd,width=250)
     canvas1.itemconfig(iii,image =img,anchor=tk.NW)
     IMAGE.upatenewimageintoobject(photo)
def newimageupdate():                                          #把畫布中的姿影像更改為新調整的影像
      global imgg
      imgg = ImageTk.PhotoImage(image=Image.fromarray(IMAGE.image))
      canvas1.config(heigh=abcd,width=250)
      canvas1.itemconfig(ii,image = imgg)
entry=tk.Entry(window)    
entry.place(x=50,y=20,width=130)            
button=tk.Button(window,text="OPEN",command=update)
button.place(x=185,y=20)
xxxxxxx= tk.Label(window,text='black')
xxxxxxx.place(x=10,y=20)
#----------------------------
def aaa(love):
     rl=rlscale.get()
     rh=rhscale.get()
     do=doscale.get()
     c=cscale.get()
     IMAGE.homomorphicfilter(rl,rh,do,c)
     newimageupdate()   
rlscale=tk.Scale(window, from_=0, to=10, orient=tk.HORIZONTAL,showvalue=1,resolution=0.1,command=aaa)
rlscale.place(x=50,y=70)
rlleble = tk.Label(window,text='Rl',font=('Arial', 12),width=2, height=2)
rlleble.place(x=25,y=80)
rhscale=tk.Scale(window, from_=0, to=10, orient=tk.HORIZONTAL,showvalue=1,resolution=0.1,command=aaa)
rhscale.place(x=50,y=110)
rhleble = tk.Label(window,text='Rh',font=('Arial', 12),width=2, height=2)
rhleble.place(x=25,y=120)
doscale=tk.Scale(window, from_=1, to=100, orient=tk.HORIZONTAL,showvalue=1,resolution=1,command=aaa)
doscale.place(x=50,y=150)
doleble = tk.Label(window,text='D0',font=('Arial', 12),width=2, height=2)
doleble.place(x=25,y=160)
cscale=tk.Scale(window, from_=1, to=40, orient=tk.HORIZONTAL,showvalue=1,resolution=1,command=aaa)
cscale.place(x=50,y=190)
cleble = tk.Label(window,text='C',font=('Arial', 12),width=2, height=2)
cleble.place(x=25,y=200)
################################################################################################################################

class color():        
      def __init__(self,image):
           self.image=image
      def upatenewimageintoobject(self,photo):          #把資料傳送到物件中的method
          self.image=photo
      def aaaa(self,cdf):
          self.image=self.image.astype(int)
          self.image=cdf[self.image]
      def r(self):
            red=colorphoto
            imagered=np.zeros([colorphoto.shape[0],colorphoto.shape[1],3])
            imageredmask=np.array([1,0,0])
            imagered=np.multiply(red,imageredmask)
            self.image=imagered.astype(np.uint8)
            
      def g(self):
            green=colorphoto
            imagegreen=np.zeros([colorphoto.shape[0],colorphoto.shape[1],3])
            imagegreenmask=np.array([0,1,0])
            imagegreen=np.multiply(green,imagegreenmask)
            self.image=imagegreen.astype(np.uint8)            
      def b(self):
            blue=colorphoto
            imageblue=np.zeros([colorphoto.shape[0],colorphoto.shape[1],3])
            imagebluemask=np.array([0,0,1])
            imageblue=np.multiply(blue,imagebluemask)
            self.image=imageblue.astype(np.uint8)
            
      def h(self):
            imagergbx=colorphoto
            imagehsv = cv2.cvtColor(imagergbx, cv2.COLOR_RGB2HSV)#rgb to hsv
            h,s,v = cv2.split(imagehsv)
            self.image=h
      def s(self):
            imagergbx=colorphoto
            imagehsv = cv2.cvtColor(imagergbx, cv2.COLOR_RGB2HSV)#rgb to hsv
            h,s,v = cv2.split(imagehsv)
            self.image=s
      def v(self):
            imagergbx=colorphoto
            imagehsv = cv2.cvtColor(imagergbx, cv2.COLOR_RGB2HSV)#rgb to hsv
            h,s,v = cv2.split(imagehsv)
            self.image=v

      def complement(self):
            xxx=colorphoto
            complement=np.ones([colorphoto.shape[0],colorphoto.shape[1],3])*255
            xxx=complement-xxx
            self.image=xxx.astype(np.uint8)


      def smoothing(self,gradient):
            smimagehsv=cv2.cvtColor(colorphoto, cv2.COLOR_RGB2HSV)
            smhue,smsaturation,smvalue=cv2.split(smimagehsv)
            imagenew=np.zeros((colorphoto.shape[0],colorphoto.shape[1]))
            laplacian=np.array(np.ones([gradient*2+1,gradient*2+1]))/(gradient*2+1)**2
            for i in range(0,colorphoto.shape[0]):
                 for j in range(0,colorphoto.shape[1]):
                      pixel=0
                      for x in range(-gradient,gradient+1):
                           for y in range(-gradient,gradient+1):
                                if i+x>=0 and j+y>=0 and x+i<colorphoto.shape[0] and y+j<colorphoto.shape[1]:
                                     a=x+gradient
                                     b=y+gradient
                                     pixel=pixel+laplacian[a,b]*smvalue[x+i,y+j]
                      imagenew[i,j]=pixel/1

                      if imagenew[i,j]<0:
                           imagenew[i,j]=0
                      elif imagenew[i,j]>255:
                           imagenew[i,j]=255
            smvalue=imagenew
            smvalue=smvalue.astype(np.uint8)
            smimagehsv=cv2.merge([smhue,smsaturation,smvalue])
            self.image=cv2.cvtColor(smimagehsv, cv2.COLOR_HSV2RGB)

      def sharpening(self,gradient):
            shimagehsv=cv2.cvtColor(colorphoto, cv2.COLOR_RGB2HSV)
            shhue,shsaturation,shvalue=cv2.split(shimagehsv)
            shimagenew=np.zeros((colorphoto.shape[0],colorphoto.shape[1]))
            shlaplacian=np.array([[0,0,1,0,0],[0,1,2,1,0],[1,2,-16,2,1],[0,1,2,1,0],[0,0,1,0,0]])
            for i in range(0,colorphoto.shape[0]):
                 for j in range(0,colorphoto.shape[1]):
                      shpixel=0
                      for x in range(-2,3):
                           for y in range(-2,3):
                                if i+x>=0 and j+y>=0 and x+i<colorphoto.shape[0] and y+j<colorphoto.shape[1]:
                                     a=x+2
                                     b=y+2
                                     shpixel=shpixel+shlaplacian[a,b]*shvalue[x+i,y+j]
                      shimagenew[i,j]=shvalue[i,j]-shpixel*gradient

                      if shimagenew[i,j]<0:
                           shimagenew[i,j]=0
                      elif shimagenew[i,j]>255:
                           shimagenew[i,j]=255
            shvalue=shimagenew
            shvalue=shvalue.astype(np.uint8)
            shimagehsv=cv2.merge([shhue,shsaturation,shvalue])
            self.image=cv2.cvtColor(shimagehsv, cv2.COLOR_HSV2RGB)
      def same(self):
            self.image=COLORIMAGE1.image

      def segment(self):
            imagehsv=cv2.cvtColor(colorphoto,cv2.COLOR_RGB2HSV)
            hue,saturation,value=cv2.split(imagehsv)
            for i in range(0,hue.shape[0]):
                 for j in range(0,hue.shape[1]):
                      if hue[i,j]<110 or hue[i,j]>158 or saturation[i,j]<0 :
                           value[i,j]=0
            #laplacian=np.ones([4,4])/16
            #value=cv2.filter2D(value,-1,laplacian)
            #value=value.astype(np.uint8)
            #value=cv2.medianBlur(value,5)
            value=value.astype(np.uint8)
            imagehsv=cv2.merge([hue,saturation,value])
            self.image=cv2.cvtColor(imagehsv, cv2.COLOR_HSV2RGB)
      def segment1(self):
            imagehsv=cv2.cvtColor(colorphoto, cv2.COLOR_RGB2HSV)
            hue,saturation,value=cv2.split(imagehsv)
            for i in range(0,hue.shape[0]):
                 for j in range(0,hue.shape[1]):
                      if hue[i,j]<110 or hue[i,j]>158:
                           value[i,j]=0
            value=value.astype(np.uint8)
            imagehsv=cv2.merge([hue,saturation,value])
            self.image=cv2.cvtColor(imagehsv, cv2.COLOR_HSV2RGB)     
      def segment2(self):
            imagehsv=cv2.cvtColor(colorphoto, cv2.COLOR_RGB2HSV)
            hue,saturation,value=cv2.split(imagehsv)
            for i in range(0,hue.shape[0]):
                 for j in range(0,hue.shape[1]):
                      if hue[i,j]<110 or hue[i,j]>158:
                           value[i,j]=0
            value=value.astype(np.uint8)
            imagehsv=cv2.merge([hue,saturation,value])
            self.image=cv2.cvtColor(imagehsv, cv2.COLOR_HSV2RGB)     



#-----------------------------------------------------------
canvasa = tk.Canvas(window)                                  
ii=canvasa.create_image(0, 0, image=photo1,anchor=tk.NW)         
canvasa.place(x=900,y=30)
canvasb = tk.Canvas(window)                                  
iii1=canvasb.create_image(0, 0, image=photo1,anchor=tk.NW)        
canvasb.place(x=300,y=300)
canvasc = tk.Canvas(window)                                  
iii2=canvasc.create_image(0, 0, image=photo1,anchor=tk.NW)        
canvasc.place(x=600,y=300)
canvasd = tk.Canvas(window)                                  
iii3=canvasd.create_image(0, 0, image=photo1,anchor=tk.NW)        
canvasd.place(x=900,y=300)
COLORIMAGE=color(photo1)#創四個物件分別用於四個框中
COLORIMAGE1=color(photo1)
COLORIMAGE2=color(photo1)
COLORIMAGE3=color(photo1)
#----------------------------------------------------------
def colorupdate():                                                  #將影像更新為所輸入地址影像
     global colorphoto  
     global colorimg
     global colorabcd    
     colorphoto=cv2.imread(colorentry.get())
     colorphoto = cv2.cvtColor(colorphoto, cv2.COLOR_BGR2RGB)
     colorabcd=int(colorphoto.shape[1]/colorphoto.shape[0]*250)#
     colorphoto=cv2.resize(colorphoto,(colorabcd,250))#
     colorimg=ImageTk.PhotoImage(image=Image.fromarray(np.uint8(colorphoto)))
     canvasa.config(heigh=colorabcd,width=250)#
     canvasa.itemconfig(ii,image =colorimg,anchor=tk.NW)
     canvasb.config(heigh=colorabcd,width=250)#
     canvasb.itemconfig(iii1,image =colorimg,anchor=tk.NW)
     canvasc.config(heigh=colorabcd,width=250)#
     canvasc.itemconfig(iii2,image =colorimg,anchor=tk.NW)
     canvasd.config(heigh=colorabcd,width=250)#
     canvasd.itemconfig(iii3,image =colorimg,anchor=tk.NW)
     COLORIMAGE.upatenewimageintoobject(colorphoto)#####
     COLORIMAGE1.upatenewimageintoobject(colorphoto)
     COLORIMAGE2.upatenewimageintoobject(colorphoto)
     COLORIMAGE3.upatenewimageintoobject(colorphoto)
def colornewimageupdate():                                          #把畫布中的姿影像更改為新調整的影像
      global colorimgg1
      global colorimgg2
      global colorimgg3
      colorimgg1 = ImageTk.PhotoImage(image=Image.fromarray(COLORIMAGE1.image))
      canvasb.config(heigh=colorabcd,width=250)#
      canvasb.itemconfig(iii1,image = colorimgg1)
      colorimgg2 = ImageTk.PhotoImage(image=Image.fromarray(COLORIMAGE2.image))
      canvasc.config(heigh=colorabcd,width=250)#
      canvasc.itemconfig(iii2,image = colorimgg2)
      colorimgg3 = ImageTk.PhotoImage(image=Image.fromarray(COLORIMAGE3.image))
      canvasd.config(heigh=colorabcd,width=250)#
      canvasd.itemconfig(iii3,image = colorimgg3)
colorentry=tk.Entry(window)    
colorentry.place(x=50,y=48,width=130)            
colorbutton=tk.Button(window,text="OPEN",command=colorupdate)
colorbutton.place(x=185,y=48)
xxxxxxxa= tk.Label(window,text='color')
xxxxxxxa.place(x=10,y=48)
#----------------------------------------------------------
def rgb():
      COLORIMAGE1.r()
      COLORIMAGE2.g()
      COLORIMAGE3.b()
      colornewimageupdate()      
rgbimage= tk.Label(window,text='RGB')
rgbimage.place(x=25,y=245)
buttonrgb= tk.Button(window, text='show',command=rgb)
buttonrgb.place(x=60,y=245)

def hsv():
      COLORIMAGE1.h()
      COLORIMAGE2.s()
      COLORIMAGE3.v()
      colornewimageupdate()      
hsvimage= tk.Label(window,text='HSV')
hsvimage.place(x=25,y=275)
buttonhsv= tk.Button(window, text='show',command=hsv)
buttonhsv.place(x=60,y=275)

def complement():
      COLORIMAGE1.complement()
      COLORIMAGE2.complement()
      COLORIMAGE3.complement()
      colornewimageupdate()      
complementimage= tk.Label(window,text='complement')
complementimage.place(x=25,y=305)
buttoncomplement= tk.Button(window, text='show',command=complement)
buttoncomplement.place(x=105,y=305)

def smoothing(love):
     gradient=smoothingscale.get()
     COLORIMAGE1.smoothing(gradient)
     COLORIMAGE2.same()
     COLORIMAGE3.same()
     colornewimageupdate()
smoothingscale=tk.Scale(window,label='smoothing', from_=0, to=4, orient=tk.HORIZONTAL,showvalue=1,resolution=1,command=smoothing)
smoothingscale.place(x=50,y=342)

def sharpening(love):
     gradient=sharpingscale.get()
     COLORIMAGE1.sharpening(gradient)
     COLORIMAGE2.same()
     COLORIMAGE3.same()
     colornewimageupdate()
sharpingscale=tk.Scale(window,label='sharpening', from_=0, to=10, orient=tk.HORIZONTAL,showvalue=1,resolution=1,command=sharpening)
sharpingscale.place(x=50,y=412)

def segment():
     COLORIMAGE1.segment1()
     COLORIMAGE2.segment2()
     COLORIMAGE3.segment()
     colornewimageupdate()
complementimage= tk.Label(window,text='segment')
complementimage.place(x=25,y=485)
buttoncomplement= tk.Button(window, text='show',command=segment)
buttoncomplement.place(x=85,y=485)






window.mainloop()
