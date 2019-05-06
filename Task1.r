setwd('D:/Uni/DM873 DL/Project')

#PART ONE---------------------------------------------------------------

  
pap <- list.files("dataset/1 Papilionidae")
pie <- list.files("dataset/2 Pieridae")

valid_pap <- sample(pap,1000)
valid_pie <- sample(pie,1000)

train_pap <- sample(pap[which(!pap %in% valid_pap)],2000)
train_pie <- sample(pie[which(!pie %in% valid_pie)],2000)

sapply(train_pap, function(t){
  file.copy(paste0("dataset/1 Papilionidae/",t), paste0("Task1/Train/1 Papilionidae/"))
})

sapply(valid_pap, function(t){
  file.copy(paste0("dataset/1 Papilionidae/",t), paste0("Task1/Validation/1 Papilionidae/"))
})


sapply(train_pie, function(t){
  file.copy(paste0("dataset/2 Pieridae/",t), paste0("Task1/Train/2 Pieridae/"))
})

sapply(valid_pie, function(t){
  file.copy(paste0("dataset/2 Pieridae/",t), paste0("Task1/Validation/2 Pieridae/"))
})



#PART TWO------------------------------------------------------------------------


lyc <- list.files("dataset/4 Lycaenidae")
nym <- list.files("dataset/3 Nymphalidae")

train_lyc <- sample(lyc,250)
train_nym <- sample(nym,250)

valid_lyc <- sample(lyc[which(!lyc %in% train_lyc)],500)
valid_nym <- sample(nym[which(!nym %in% train_nym)],500)

sapply(train_lyc, function(t){
  file.copy(paste0("dataset/4 Lycaenidae/",t), paste0("Task2/Train/4 Lycaenidae/"))
})

sapply(valid_lyc, function(t){
  file.copy(paste0("dataset/4 Lycaenidae/",t), paste0("Task2/Validation/4 Lycaenidae/"))
})


sapply(train_nym, function(t){
  file.copy(paste0("dataset/3 Nymphalidae/",t), paste0("Task2/Train/3 Nymphalidae/"))
})

sapply(valid_nym, function(t){
  file.copy(paste0("dataset/3 Nymphalidae/",t), paste0("Task2/Validation/3 Nymphalidae/"))
})


#PART THREE------------------------------------------------------------------------


hes <- list.files("dataset/5 Hesperiidae")

train_pap <- sample(pap,1000)
train_pie <- sample(pie,1000)
train_lyc <- sample(lyc,1000)
train_nym <- sample(nym,1000)
train_hes <- sample(hes,1000)

valid_pap <- sample(pap[which(!pap %in% train_pap)],700)
valid_pie <- sample(pie[which(!pie %in% train_pie)],700)
valid_lyc <- sample(lyc[which(!lyc %in% train_lyc)],700)
valid_nym <- sample(nym[which(!nym %in% train_nym)],700)
valid_hes <- sample(hes[which(!hes %in% train_hes)],700)


sapply(train_pap, function(t){
  file.copy(paste0("dataset/1 Papilionidae/",t), paste0("Task3/Train/1 Papilionidae/"))
})

sapply(valid_pap, function(t){
  file.copy(paste0("dataset/1 Papilionidae/",t), paste0("Task3/Validation/1 Papilionidae/"))
})

sapply(train_pie, function(t){
  file.copy(paste0("dataset/2 Pieridae/",t), paste0("Task3/Train/2 Pieridae/"))
})

sapply(valid_pie, function(t){
  file.copy(paste0("dataset/2 Pieridae/",t), paste0("Task3/Validation/2 Pieridae/"))
})

sapply(train_lyc, function(t){
  file.copy(paste0("dataset/4 Lycaenidae/",t), paste0("Task3/Train/4 Lycaenidae/"))
})

sapply(valid_lyc, function(t){
  file.copy(paste0("dataset/4 Lycaenidae/",t), paste0("Task3/Validation/4 Lycaenidae/"))
})

sapply(train_nym, function(t){
  file.copy(paste0("dataset/3 Nymphalidae/",t), paste0("Task3/Train/3 Nymphalidae/"))
})

sapply(valid_nym, function(t){
  file.copy(paste0("dataset/3 Nymphalidae/",t), paste0("Task3/Validation/3 Nymphalidae/"))
})

sapply(train_hes, function(t){
  file.copy(paste0("dataset/5 Hesperiidae/",t), paste0("Task3/Train/5 Hesperiidae/"))
})

sapply(valid_hes, function(t){
  file.copy(paste0("dataset/5 Hesperiidae/",t), paste0("Task3/Validation/5 Hesperiidae/"))
})

