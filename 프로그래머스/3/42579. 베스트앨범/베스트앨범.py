def solution(genres, plays):
    ans = []
    genre_total = dict()
    genre_ranks = dict()

    for i in range(len(genres)):
        genre_total[genres[i]] = genre_total.get(genres[i], 0) + plays[i]
        genre_ranks[genres[i]] = genre_ranks.get(genres[i], []) + [(plays[i], i)]

    genre_total = sorted(genre_total.items(), key=lambda x: -x[1])

    for genre, _ in genre_total:
        genre_ranks[genre] = sorted(genre_ranks[genre], key=lambda x: (-x[0], x[1]))
        ans += [idx for play, idx in genre_ranks[genre][:2]]

    return ans