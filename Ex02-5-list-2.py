append()
insert()
remove()
pop()
clear()

starter_pokemon = ['피카유', '파이리', '꼬부기']
starter_pokemon.append('이상해씨')
print('스타터 포켓몬:', starter_pokemon)

starter_pokemon.insert('index 1', '잠만보')
print('삽입된 포켓몬:', starter_pokemon)

lengendary_pokemon = ['그라도', '가이오가', '레쿠자', '히드런']
print('전설의 포켓몬:', lengendary_pokemon)

lengendary_pokemon.remove('히드런')
print('방출후:', lengendary_pokemon)


# 4. 세트 제거 메서드
water_type = {'꼬부기', '잉어킹', '라프라스'}
water_type.remove('잉어킹')
print('remove 후):' water_type)

water_type.discard('라프라스')
print('discard 후:' water_type)

water_type.pop()   # 임의 제거
print('pop 후:', water_type)

# water_type.pop()  # 값이 없으면 에러 발생 KeyError: 'pop from an empty

new_type = {'메가이브이', '뮤'}
new_type.clear()   # 전체 제거
print('clear 후:', new_type)





