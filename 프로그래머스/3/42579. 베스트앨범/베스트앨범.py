def solution(genres, plays):
    genre_rank = {}  # 장르별 총 재생 횟수 저장
    genre_songs = {}  # 장르별 (재생 수, 인덱스) 저장
    
    # 장르별 데이터 정리
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_rank:
            genre_rank[genre] = 0
            genre_songs[genre] = []
        
        genre_rank[genre] += play  # 장르별 총 재생 수 누적
        genre_songs[genre].append((play, idx))  # (재생 수, 인덱스) 저장
    
    # 장르별 총 재생 수를 기준으로 정렬 (내림차순)
    sorted_genres = sorted(genre_rank.keys(), key=lambda x: genre_rank[x], reverse=True)
    
    answer = []
    for genre in sorted_genres:
        # 해당 장르의 곡들을 재생 수, 인덱스 순으로 정렬 (재생 수 내림차순, 인덱스 오름차순)
        songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        
        # 최대 두 곡 선택
        answer.extend([idx for _, idx in songs[:2]])
    
    return answer