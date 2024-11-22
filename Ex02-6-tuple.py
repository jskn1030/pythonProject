'''
파일명: Ex02-6-tuple.py

튜플(Tuple)
    - 읽기 전용 리스트
    - 수정 불가능 순서가 있는 자료구조
    - 소괄호() 사용
'''

# 1. 튜플 생성과 기본 조작
game_starter = ('파이리', '이상해씨', '꼬부기')
print('스타터 포겟몬:', game_starter)
print('첫번째 스타터:', game_starter[0])
print('마지막 스타터:', game_starter[-1])
print('전체 스타터수:', len(game_starter))

legendary_birds = ('프리쳐', '썬더', '파이어', '루기아')
print('전설의 새:', legendary_birds[1:3])

evolve_chain = ('치코타', '베이리프', '리코타')

evolve_chain[1] = '메가페이리프'
print('튜플 수정 테스트:', evolve_chain)

gym_leader = ('지우', '음', '로이', '로사')
(leader1, leader2, leader3, leader4) = gym_leader
print('체육관 1번관장:', leader1)
print('체육관 2번관장:', leader2)
print('체육관 3번관장:', leader3)
print('체육관 4번관장:', leader4)