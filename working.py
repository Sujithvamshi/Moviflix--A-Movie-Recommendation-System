def posters_list(json_data):
    posters = []
    names=[]
    for i in json_data:
        if i == 'results':
            for j in json_data[i]:
                posters.append(j['poster_path'])
                names.append(j['original_title'])
    return posters,names