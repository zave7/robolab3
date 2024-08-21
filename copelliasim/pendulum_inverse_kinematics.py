import math
import numpy as np

# 시뮬레이션 총 시간 설정
T_end = 10
# 원의 반지름 설정 (엔드 이펙터로부터 x방향으로 -0.5만큼 떨어진 위치)
r = 0.5

def curve(t):
    # 원운동의 각속도 계산
    f = 2*math.pi/T_end
    
    # 시간 t에 따른 목표 x, y 좌표 계산
    x_ref = x_center + r*math.cos(f*t)
    y_ref = y_center + r*math.sin(f*t)
    
    return x_ref, y_ref

def sysCall_init():
    sim = require('sim')  # CoppeliaSim API 불러오기
    global joint1, joint2, end_effect, end_effect_trace, x_center, y_center
    
    # 시뮬레이션 내 객체들의 핸들 가져오기
    joint1 = sim.getObject("/Joint1")
    joint2 = sim.getObject("/Joint2")
    
    # 엔드 이펙터의 궤적을 그리기 위한 드로잉 객체 생성
    end_effect_trace = sim.addDrawingObject(sim.drawing_linestrip, 5, 0, -1, 100_000, [1,0,0])
    
    end_effect = sim.getObject("/EndEff")
    
    # 엔드 이펙터의 초기 위치 가져오기
    end_effect_position = sim.getObjectPosition(end_effect, sim.handle_world)
    x = end_effect_position[0]
    y = end_effect_position[1]
    
    # 원의 중심 좌표 계산 (엔드 이펙터로부터 x방향으로 -r만큼 이동)
    x_center = x-r
    y_center = y

def sysCall_actuation():
    # 현재 조인트 각도 가져오기
    theta1 = sim.getJointPosition(joint1)
    theta2 = sim.getJointPosition(joint2)
    print(f"join1: {theta1}, joint2: {theta2}")
    
    l = 1  # 링크 길이 (각 링크가 1이라고 가정)
    
    # 자코비안 행렬 계산
    J = np.array([[l*(np.cos(theta1) + np.cos(theta1 + theta2)), l*np.cos(theta1 + theta2)], \
                  [l*(np.sin(theta1) + np.sin(theta1 + theta2)), l*np.sin(theta1 + theta2)]])
    
    # 자코비안 역행렬 계산
    Jinv = np.linalg.inv(J)
    
    # 현재 시뮬레이션 시간 가져오기
    t = sim.getSimulationTime()
    
    # 현재 시간에 대한 목표 위치 계산
    x_ref, y_ref = curve(t)
    
    # 현재 엔드 이펙터의 위치 가져오기
    end_effect_position = sim.getObjectPosition(end_effect, sim.handle_world)
    x = end_effect_position[0]
    y = end_effect_position[1]
    
    # 목표 위치와 현재 위치의 차이 계산
    dr = [x_ref - x, y_ref - y]
    
    # 역운동학을 통해 필요한 조인트 각도 변화량 계산
    dq = Jinv.dot(dr)
    
    # 조인트 각도 업데이트
    theta1 += dq[0]
    theta2 += dq[1]
    
    # 새로운 조인트 각도 설정
    sim.setJointTargetPosition(joint1, theta1)
    sim.setJointTargetPosition(joint2, theta2)
    
    # 시뮬레이션 종료 조건 확인
    if (t>T_end):
        sim.stopSimulation()

def sysCall_sensing():
    # 엔드 이펙터의 현재 위치 가져오기
    end_effect_pos = sim.getObjectPosition(end_effect, sim.handle_world)
    # 엔드 이펙터의 궤적 그리기
    sim.addDrawingObjectItem(end_effect_trace, end_effect_pos)

def sysCall_cleanup():
    # 정리 작업 수행 (현재는 비어있음)
    pass