import libsvm
import argparse
from cPickle import load
from learn import extractSift, computeHistograms, writeHistogramsToFile
import os

HISTOGRAMS_FILE = 'testdata.svm'
CODEBOOK_FILE = 'codebook.file'
MODEL_FILE = 'trainingdata.svm.model'


def parse_arguments():
    parser = argparse.ArgumentParser(description='classify images with a visual bag of words model')
    parser.add_argument('-c', help='path to the codebook file', required=False, default=CODEBOOK_FILE)
    parser.add_argument('-m', help='path to the model  file', required=False, default=MODEL_FILE)
    parser.add_argument('input_images', help='images to classify', nargs='+')
    args = parser.parse_args()
    return args

def predict_image(model_file,codebook_file,fnames):
	print str(fnames[0])+".sift"
	try:
		os.remove(str(fnames[0])+".sift")
	except OSError:
		pass
	# extract Sift features"
	all_files = []
	all_files_labels = {}
	all_features = {}

	print fnames
	try:
		all_features = extractSift(fnames)
		for i in fnames:
			all_files_labels[i] = 0  # label is unknown
			
		# loading codebook from codebook_file
		with open(codebook_file, 'rb') as f:
			codebook = load(f)

		# computing visual word histograms"
		all_word_histgrams = {}
		for imagefname in all_features:
			word_histgram = computeHistograms(codebook, all_features[imagefname])
			all_word_histgrams[imagefname] = word_histgram

		# write the histograms to file to pass it to the svm
		nclusters = codebook.shape[0]
		writeHistogramsToFile(nclusters,
							  all_files_labels,
							  fnames,
							  all_word_histgrams,
							  HISTOGRAMS_FILE)

		# test data with svm"
		print libsvm.test(HISTOGRAMS_FILE, model_file)
	except Exception as e:
		pass #Incase of error with sift extraction, just try again on next stroke
		
if __name__=="__main__":
	args = parse_arguments()
	model_file = args.m
	codebook_file = args.c
	fnames = args.input_images
	predict_image(model_file,codebook_file,fnames)
