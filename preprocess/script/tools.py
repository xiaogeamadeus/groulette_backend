import json
import os, glob, pickle

# This files contains useful functions

def json2dict(filename,key):
    """json2dict _summary_
    jsonファイルをdict型に変換し、特定のkeyのデータを返す

    Args:
        filename (String): ファイル名
        key (String): jsonのkey

    Returns:
        list: [{店舗情報のdict},{},...]
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    return data[key]

def getfiles(dir="./groulette_backend/restaurantData/", suffix='json'):
    """getfiles _summary_
    dirにあるfiletypeで終わるファイル名のリストを獲得
    Args:
        dir (str, optional): ファイルが入っているフォルダ. Defaults to "./groulette_backend/restaurantData/".
        filetype (str, optional): . Defaults to 'json'.

    Returns:
        List: ファイル名が入ってるList
    """

    files = glob.glob(dir+'*.{}'.format(suffix))
    return files

def txt2list(filename):
    """txt2list _summary_
    txtファイル内のplace_idをlistとして読み込み
    Args:
        filename (String): ファイル名

    Returns:
        List: place_idのlist
    """
    with open(filename, 'r') as f:
        data = f.read()
        data2list = data.split('\n')
        return data2list

def getplaceid():
    path = './groulette_backend/restaurantData/'
    save_path = './groulette_backend/restaurantPlaceid/'
    files = getfiles()
    key = 'results'
    for filename in files:
        res = json2dict(filename, key)
        ids = [store['place_id'].encode('ascii') for store in res]
        # ids = [store['place_id'] for store in res]
        save_filename = os.path.splitext(filename)[0].split('/')[-1]
        with open(save_path+save_filename+'.txt', 'wb') as f:
            for id in ids:
                f.write("%s\n" % id)



if __name__ == '__main__':
    files = getfiles()
    restaurants = [[] for i in range(8)]
    genre_id = {'Asian':0, 'Chinese1':0, 'Chinese2':0,'Family':7, 'Fast':3, 'Franch':5, 'Gyudon':4, 'Health':7, 'Humberger':3, 'Italian':5, 'Izakaya':6, 'Korean':0, 'Pasta':5, 'Pizza':3, 'Ramen':2, 'Sushi':4, 'Syokudo':4, 'Teishoku':4, 'Tempura':4, 'Udon':4, 'Vegan':7, 'Yakiniku':1, 'Yakitori':6, 'cafe': 7}
    keys = ['rating', 'user_ratings_total', 'name', 'place_id', 'vicinity', 'location']
    for filename in files:
        res = json2dict(filename, 'results')
        genre_name = os.path.splitext(filename)[0].split('/')[-1]
        if genre_name == 'Noodles': continue
        id = genre_id[genre_name] # genre_id
        for store in res:
            cur = {'genre':id}
            for key in keys:
                if key == 'location':
                    cur[key] = '{},{}'.format(store['geometry']['location']['lat'],store['geometry']['location']['lng'])
                else:
                    cur[key] = store[key]
            restaurants[id].append(cur)
        # print(f'{genre_name} finished')

    for i in range(8): 
        print(f'total number of genre {i}: {len(restaurants[i])}')
        print('Sample:')
        print(restaurants[i][0])
        print('==========================================================')
        
    dump_flag = False
    if dump_flag:
        with open('groulette_backend/restaurantDB/restaurant.pkl', 'wb') as f:
            pickle.dump(restaurants, f)       


'''
  - genre
  - rating
  - user_ratings_total
  - name
  - place_id
  - vicinity
  - location
'''