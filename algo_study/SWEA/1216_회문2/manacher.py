def manacher(s):
    s = '#' + '#'.join(s) + '#'

    N = len(s)
    cnt_list = [0] * N

    """
    r : 지금까지 확인한 회문들의 가장 먼 우측 idx
    p : 지금까지 확인한 회문들중 가장 긴 회문의 idx
    """

    r = p = 0
    for idx in range(N):
        if idx <= r:
            m_idx = 2 * p -idx

            # 남은 꽃길 길이만큼으로 갱신
            if cnt_list[m_idx] > r - idx:
                cnt_cnt[idx] = r - idx
            else: # 대척점 내용으로 갱신
                cnt_list[idx] = cnt_list[m_idx]


        """
        idx - cnt_list[idx] => 현 idx 기준으로 확보한 회문 좌측 끝
        idx + cnt_list[idx] => 현 idx 기준으로 확보한 회문 우측 끝
        idx - cnt_list[idx] - 1 => 미지의 왼쪽
        idx + cnt_list[idx] + 1 => 미지의 오른쪽
        """

        # 변수화하면 안됨 변수는 고정값이라 한가지 값으로 고정되서 반복됨

        while idx - cnt_list[idx] - 1 >= and idx + cnt_list[idx] + 1 < N and\
                s[idx - cnt_list[idx] - 1] == s[idx + cnt_list[idx] + 1]:
            cnt_list[idx] += 1


        if r < idx + cnt_list[idx]:
            r = idx + cnt_list[idx]
            p = idx # 중심점을 잡기 위해서 필요함.

    return max(cnt_list)