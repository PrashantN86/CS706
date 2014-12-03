from Tkinter import *
import Image,ImageDraw
from classify import predict_image
import argparse
import threading

HISTOGRAMS_FILE = 'testdata.svm'
CODEBOOK_FILE = 'codebook.file'
MODEL_FILE = 'trainingdata.svm.model'
LABEL_MAPPING = 'label_mapping.txt'
PREDICTION_FILE = 'trainingdata.svm.prediction'

canvas_width = 1111
canvas_height = 1111
white = (255, 255, 255)
black = (0,0,0)
points=[]

image1 = Image.new("RGB", (canvas_width, canvas_height), white)
draw = ImageDraw.Draw(image1)

def parse_arguments():
    parser = argparse.ArgumentParser(description='classify images with a visual bag of words model')
    parser.add_argument('-c', help='path to the codebook file', required=False, default=CODEBOOK_FILE)
    parser.add_argument('-m', help='path to the model  file', required=False, default=MODEL_FILE)
    parser.add_argument('-p', help='path to the prediction file', required=False, default=PREDICTION_FILE)
    parser.add_argument('-l', help='path to the label mapping file', required=False, default=LABEL_MAPPING)
    args = parser.parse_args()
    return args
    
def getpoints( event ):
	global points
	points.append(event.x)
	points.append(event.y)
   
def paint( event ):
	global model_file,codebook_file,label,cats
	global points,draw
	getpoints(event)
	#x1, y1 = ( event.x - 1 ), ( event.y - 1 )
	#x2, y2 = ( event.x + 1 ), ( event.y + 1 )
	w.create_line(points,width=4)
	draw.line(points, black,width=4)
	points=[]
	filename = "test.png"
	image1.save(filename)
	with open(prediction,'r') as f:
		labels=f.readline().split()[1:]
		categ_order=f.readline().split()[1:]
		labelorder=[x for (y,x) in sorted(zip(categ_order,labels),reverse=True)]
	text=""
	print labelorder
	for i in labelorder:
		text=text+" "+cats[int(i)]	
	label.config(text=str(text))
	thr = threading.Thread(target=predict_image, args=(model_file,codebook_file,[filename]), kwargs={})
	thr.start()
	
if __name__=="__main__":
	args = parse_arguments()
	model_file = args.m
	codebook_file = args.c
	prediction=args.p
	label_mapping=args.l
	master = Tk()
	master.title( "Sketch recognition" )
	label = Label(master,height=1,font = "Verdana 10 bold",width=canvas_width,pady=10)
	label.config(text="Start Sketching")
	label.pack()
	with open(label_mapping, 'r') as inp:
		cats=dict(((int(value), key) for key, value in (line.split(' ') for line in inp)))
	w = Canvas(master, 
			   width=canvas_width, 
			   height=canvas_height,
			   bg='white')

	w.pack(expand = YES, fill = BOTH)
	w.bind( '<B1-Motion>', getpoints )
	w.bind( '<ButtonRelease-1>', paint )


	message = Label( master, text = "Press and Drag the mouse to draw" )
	message.pack( side = BOTTOM )
		
	mainloop()
