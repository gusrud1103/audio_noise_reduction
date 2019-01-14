import os
from tqdm import tqdm


os.chdir('/Users/jw/Downloads/noise_reduction-master/01_samples_trimmed_noise_reduced_taeyon/')


# 파일 삭제 
for i in tqdm(range(559,3557)):
	try:
		os.remove('taeyun_'+str(i)+'_ctr_mb.wav')
	except:
		print(str(i)+'_ctr_mb.wav')
		continue
	try:
		os.remove('taeyun_'+str(i)+'_ctr_s.wav')
	except:
		print(str(i)+'_ctr_s.wav')
		continue
	try:
		os.remove('taeyun_'+str(i)+'_median.wav')
	except:
		print(str(i)+'_median.wav')
		continue
	try:
		os.remove('taeyun_'+str(i)+'_mfcc_down.wav')
	except:
		print(str(i)+'_mfcc_down.wav')
		continue
	try:
		os.remove('taeyun_'+str(i)+'_mfcc_up.wav')
	except:
		print(str(i)+'_mfcc_up.wav')
		continue
	try:
		os.remove('taeyun_'+str(i)+'_org.wav')
	except:
		print(str(i)+'_org.wav')
		continue



# 파일명 변경 taeyun -> taeyon
import os 
path = '/Users/jw/Downloads/noise_reduction-master/01_samples_trimmed_noise_reduced_taeyon/'

for filename in tqdm(os.listdir(path)): 
	try:
		newname = filename.replace('u','o')
		os.rename(path+filename, path+newname)
	except:
		pass