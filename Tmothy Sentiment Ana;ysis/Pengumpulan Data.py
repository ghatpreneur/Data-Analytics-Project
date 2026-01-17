from googleapiclient.discovery import build
import pandas as pd
import sys # Buat maksa encoding aman 

#  KONFIGURASI 
API_KEY = 'AIzaSyCi1bphee2q4mpfSA5OdzhxhXZNG7K5Osk' 
VIDEO_ID = 'EbLJ6qZLkrA'
LIMIT = None

def get_all_comments(api_key, video_id, limit_count=None):
    youtube = build('youtube', 'v3', developerKey=api_key)
    
    comments = []
    next_page_token = None
    
    # Hapus emoji roket, ganti text biasa
    print(f"[START] Mulai mengambil komentar dari video: {video_id}...")
    
    while True:
        try:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                textFormat="plainText",
                pageToken=next_page_token
            )
            response = request.execute()
            
            for item in response['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                author = item['snippet']['topLevelComment']['snippet']['authorDisplayName']
                comments.append([author, comment])
            
            # Hapus emoji centang
            print(f"[PROGRESS] Berhasil ambil {len(comments)} komentar...")
            
            if 'nextPageToken' in response:
                next_page_token = response['nextPageToken']
            else:
                print("[INFO] Halaman habis! Semua komentar sudah terambil.")
                break
                
            if limit_count and len(comments) >= limit_count:
                print(f"[STOP] Mencapai batas limit {limit_count} komentar.")
                break
                
        except Exception as e:
            print(f"[ERROR] Terjadi kesalahan: {e}")
            break

    df = pd.DataFrame(comments, columns=['User', 'Comment'])
    return df

# EKSEKUSI
# Panggil fungsi
df_hasil = get_all_comments(API_KEY, VIDEO_ID, LIMIT)

# Simpan CSV
filename = 'data_timothy_lengkap.csv'
# encoding='utf-8-sig' 
df_hasil.to_csv(filename, index=False, encoding='utf-8-sig')

print(f"[SUKSES] {len(df_hasil)} komentar tersimpan di '{filename}'")