setwd('D:/Uni/DM873 DL/Project')

data <- read.delim('dataset/butterflies.txt',header=FALSE)


count1 = 0;
count2 = 0;
count3 = 0;
count4 = 0;
count5 = 0;
for(i in 1:22765){
  if (data[i,5]==1) {
    file.copy(paste0('dataset/base_set/',data[i,1]),paste0('dataset/1 Papilionidae/'))
    count1 = count1 + 1;
    file.rename(paste0('dataset/1 Papilionidae/',substring(data[i,1],regexpr('/', data[i,1])+1)),paste0('dataset/1 Papilionidae/1_',count1,'.jpg'))
  }
  else if (data[i,5]==2) {
    file.copy(paste0('dataset/base_set/',data[i,1]),paste0('dataset/2 Pieridae/'))
    count2 = count2 + 1;
    file.rename(paste0('dataset/2 Pieridae/',substring(data[i,1],regexpr('/', data[i,1])+1)),paste0('dataset/2 Pieridae/2_',count2,'.jpg'))
  }
  else if (data[i,5]==3) {
    file.copy(paste0('dataset/base_set/',data[i,1]),paste0('dataset/3 Nymphalidae/'))
    count3 = count3 + 1;
    file.rename(paste0('dataset/3 Nymphalidae/',substring(data[i,1],regexpr('/', data[i,1])+1)),paste0('dataset/3 Nymphalidae/3_',count3,'.jpg'))
  }
  else if (data[i,5]==4) {
    file.copy(paste0('dataset/base_set/',data[i,1]),paste0('dataset/4 Lycaenidae/'))
    count4 = count4 +1;
    file.rename(paste0('dataset/4 Lycaenidae/',substring(data[i,1],regexpr('/', data[i,1])+1)),paste0('dataset/4 Lycaenidae/4_',count4,'.jpg'))
  }
  else if (data[i,5]==5) {
    file.copy(paste0('dataset/base_set/',data[i,1]),paste0('dataset/5 Hesperiidae/'))
    count5 = count5 +1;
    file.rename(paste0('dataset/5 Hesperiidae/',substring(data[i,1],regexpr('/', data[i,1])+1)),paste0('dataset/5 Hesperiidae/5_',count5,'.jpg'))
  }
}

