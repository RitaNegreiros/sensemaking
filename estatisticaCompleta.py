from numpy import zeros, linspace 
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import csv 
import json

def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.insert(0, row)

    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)
        
    def getTimeStep(data):
        step = data["Timestep"]
        return int(step)     

    def getLikes(data):
        likes = data["Likes"]
        return int(likes) 
    
    def getComments(data):
        comment = data["Comments"]
        return int(comment) 

    def getLoves(data):
        loves = data["Loves"]
        return int(loves) 
    
    def getShares(data):
        shares = data["Shares"]
        return int(shares) 
    
    def getPostViews(data):
        views = data["Post Views"]
        return int(views)  
       
    def getSads(data):
        sads = data["Sads"]
        return int(sads)  
    
    def getAngrys(data):
        anglys = data["Angrys"]
        return int(anglys) 
    
    def getHaHas(data):
        hahas = data["Hahas"]
        return int(hahas) 

    def getCares(data):
        cares = data["Cares"]
        return int(cares)  

    def getAllReactions(data):
        likes = data["Likes"]
        loves = data["Loves"]
        cares = data["Cares"]
        hahas = data["Hahas"]
        sads = data["Sads"]
        anglys = data["Angrys"]
        return int(int(likes) +  int(loves) + int(cares) + int(hahas) + int(sads) + int(anglys))  
    
    def getAsymptContaminated(data):
        views = data["Post Views"]
        shares = data["Shares"]
        return int(int(views) - int(shares))
      
    newTimesteps = list(map(getTimeStep, jsonArray))
    newLikes = list(map(getLikes, jsonArray))
    newComments = list(map(getComments, jsonArray))
    newLoves = list(map(getLoves, jsonArray))
    newShares = list(map(getShares, jsonArray))
    newPostViews = list(map(getPostViews, jsonArray))
    newSads = list(map(getSads, jsonArray))
    newAngrys = list(map(getAngrys, jsonArray))
    newHahas = list(map(getHaHas,jsonArray))
    newCares = list(map(getCares,jsonArray))
    newAllReactions = list(map(getAllReactions,jsonArray))
    newAsymptContaminated = list(map(getAsymptContaminated,jsonArray))

    # Build chart
    fig1, ax = plt.subplots(figsize=(10 , 5), constrained_layout=True)
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    plt.rcParams.update({'font.size': 12})
    plt.rc('axes', titlesize=24)

    plt.plot(newTimesteps,newLikes,color='green',label='likes')
    plt.plot(newTimesteps,newComments,color='maroon',label='coments')
    plt.plot(newTimesteps,newLoves,color='magenta',label='loves')
    plt.plot(newTimesteps,newShares,color='limeGreen',label='share')
    plt.plot(newTimesteps,newPostViews,color='purple',label='views')
    plt.plot(newTimesteps,newSads,color='blue',label='sad')
    plt.plot(newTimesteps,newAngrys,color='red',label='angry')
    plt.plot(newTimesteps,newHahas,color='seaGreen',label='smiles')
    plt.plot(newTimesteps,newCares,color='orange',label='care')
    
    plt.xlabel('Timestep') 
    plt.ylabel('Quantidade')
    plt.title(str(chartTitleReaction)) 
    plt.legend()
    plt.savefig('estatisticaReacoes.png')

    fig2, ax = plt.subplots(figsize=(10 , 5), constrained_layout=True)
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    plt.rcParams.update({'font.size': 12})
    plt.rc('axes', titlesize=24)

    plt.plot(newTimesteps,newPostViews,color='purple',label='infectados (visualizações)')
    plt.plot(newTimesteps,newAllReactions,color='lightBlue',label='recuperados (soma de reações)')
    plt.plot(newTimesteps,newAsymptContaminated,color='darkOliveGreen',label='contaminados assintomáticos (visualizaram mas não compartilharam)')
    plt.plot(newTimesteps,newShares,color='limeGreen',label='contaminados sintomáticos (compartilharam)')
   

    print("\nrecuperados (soma de reações): ",newAllReactions)
    print("\ninfectados (visualizações): ",newPostViews)
    print("\ncontaminados assintomáticos (visualizaram mas não compartilharam): ",newAsymptContaminated)
    print("\ncontaminados sintomáticos (compartilharam): ",newShares)

    plt.xlabel('Janela de Tempo - Minutos') 
    plt.ylabel('Quantidade')
    plt.title(str(chartTitleSenseMake)) 
    plt.legend()

    tex = "Seguidores:\n " + str(followings)
    ax.text(5, 300, tex, fontsize=16, va='center', color="blue")

    fig2.tight_layout()

    plt.savefig('estatisticaSentimentos.png')

    print("\nGráfico construido com sucesso!\n\n") 
    # print("Arquivo JSON criado:\n", jsonArray) 

    fig3, ax = plt.subplots(figsize=(10 , 5), constrained_layout=True)
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    plt.rcParams.update({'font.size': 12})
    plt.rc('axes', titlesize=24)

    plt.plot(newTimesteps,newComments,color='maroon',label='Comentários')
    plt.plot(newTimesteps,newShares,color='limeGreen',label='Compartilhamentos')
    plt.plot(newTimesteps,newPostViews,color='blue',label='Visualizações')
    plt.plot(newTimesteps,newAllReactions,color='magenta',label='Reações')
    
    print("\nGRÁFICO DE REAÇÕES 2: ")
    print("\nsoma de reações: ",newAllReactions)
    print("\ncomentarios: ",newComments)
    print("\ncompartilhamentos: ",newShares)
    print("\nvisualizações: ",newPostViews)


    plt.xlabel('Janela de Tempo - Minutos') 
    plt.ylabel('Quantidade')
    plt.title(str(chartTitleReaction)) 
    plt.legend()

    fig3.tight_layout()

    plt.savefig('reações2.png')

    print("\nGráfico construido com sucesso!\n\n") 
    # print("Arquivo JSON criado:\n", jsonArray) 

chartTitleReaction = input("Informe o título do gráfico de reações: ")
chartTitleSenseMake = input("Informe o título do gráfico de sentimentos: ")
followings = int(input("Informe o número de seguidores: "))

csvFilePath = r'post.csv'
jsonFilePath = r'data.json'
csv_to_json(csvFilePath, jsonFilePath)



 



