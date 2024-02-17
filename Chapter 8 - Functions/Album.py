def make_album(artist_name, album_title, number_of_tracks=''):
    album_info = {
        'artist name': artist_name,
        'album title': album_title
    }

    if number_of_tracks:
        album_info['number of tracks'] = number_of_tracks

    return album_info

while True:
    artist = input("Enter the name of the Artist (Enter 'q' to exit): ")
    if artist.lower() == 'q':
        break

    title = input("Enter the name of the Album (Enter 'q' to exit): ")
    if title.lower() == 'q':
        break
    tracks = input("Enter the number of tracks, (Enter 'q' if you want to omit): ")

    if tracks.lower() == 'q':
        info = make_album(artist, title)
    else:
        info = make_album(artist, title, number_of_tracks=tracks)
    print(info)

    break