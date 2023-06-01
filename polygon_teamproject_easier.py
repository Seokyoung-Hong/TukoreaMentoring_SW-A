class Polygon:
    def __init__(self, number, shape_type, first_vertex, second_vertex, third_vertex):
        self.number = number
        self.shape_type = shape_type
        self.first_vertex = first_vertex
        self.second_vertex = second_vertex
        self.third_vertex = third_vertex
    
    # 좌표를 리스트로 반환
    def vertex_list(self):
        return [self.first_vertex, self.second_vertex, self.third_vertex]

    # 다각형의 정보를 문자열로 반환
    def vertex_info(self):
        return(f"[{self.number}] {self.shape_type} {self.vertex_list()}")

    # 다각형의 선분 길이의 합을 반환
    def length(self):
        distance_list = []
        for i in range(-1, len(self.vertex_list())-1):
            # 두 점 사이의 거리를 모두 구하여 리스트에 추가
            temp = Polygon.distance(*self.vertex_list()[i], *self.vertex_list()[i+1])
            distance_list.append(temp)
        return sum(distance_list)
    
    # 좌표의 x값만 리스트로 반환
    def x_list(self):
        return [i for i,j in self.vertex_list()]

    # 좌표의 y값만 리스트로 반환
    def y_list(self):
        return [j for i,j in self.vertex_list()]

    # 두 점 사이의 거리를 반환
    @staticmethod
    def distance(x,y,x2,y2):
        return ((x-x2)**2+(y-y2)**2)**0.5



class Rectangle(Polygon):
    def __init__(self, number, shape_type, first_vertex, second_vertex, third_vertex, fourth_vertex):
        super().__init__(number, shape_type, first_vertex, second_vertex, third_vertex)
        # 사각형의 4번째 점을 추가
        self.fourth_vertex = fourth_vertex

    # 좌표를 리스트로 반환하되 기본적인 점 3개에 4번째 점인 fourth_vertex를 추가
    def vertex_list(self):
        return super().vertex_list() + [self.fourth_vertex]

    # 다각형의 넓이를 반환
    def area(self):
        # x값의 최대값에서 최소값을 빼고 y값의 최대값에서 최소값을 빼서 곱하면 사각형의 넓이를 구할 수 있음
        return (max(self.x_list())-min(self.x_list()))*(max(self.y_list())-min(self.y_list()))

class Triangle(Polygon):
    def __init__(self, number, shape_type, first_vertex, second_vertex, third_vertex):
        super().__init__(number, shape_type, first_vertex, second_vertex, third_vertex)
    
    # 다각형의 넓이를 반환
    def area(self):
        for i in range(-1,2):
            # 삼각형의 높이를 구하기 위해 y값이 같은 두 점을 찾고 그 점 사이의 거리를 밑변으로 설정
            if self.vertex_list()[i][1] == self.vertex_list()[i+1][1]:
                base = abs(self.vertex_list()[i][0]-self.vertex_list()[i+1][0]) # 밑변

                # y값은 2개의 종류만 갖기 때문에 가장 큰 값에서 가장 작은 값을 빼면 높이를 구할 수 있음
                height = max(self.y_list())-min(self.y_list()) # 높이
                break
        return base*height/2

polygons = []

# 다각형의 정보를 출력
def print_vertex_info(polygons):
    output = ''
    for polygon in polygons:
        output += polygon.vertex_info() + '\t' # 다각형의 정보를 문자열로 반환
    print(output)

times=0
while True:
    a=int(input('(명령) (1) 다각형 입력 (2) 다각형 나열 (3) 선분 길이구하기 (4) 면적 구하기 (9) 종료 : '))

    # 다각형을 생성
    if a==1:
        vertex_count = int(input("꼭지점 수 : "))

        # 꼭지점 수가 3이나 4일 경우에만 다각형을 생성
        if vertex_count in [3,4]:
            vertex_list = []
            
            # 꼭지점의 개수만큼 꼭지점의 좌표를 입력받아 리스트에 추가
            for i in range(vertex_count):
                vertex = tuple(map(int,input("꼭지점 x,y좌표:").split()))
                vertex_list.append(vertex)
            
            # 꼭지점의 개수에 따라 삼각형 또는 사각형 생성
            if vertex_count == 3:
                polygons.append(Triangle(times, "triangle", *vertex_list))
            else:
                polygons.append(Rectangle(times, "rectangle", *vertex_list))
            
            # 다각형의 개수를 1 증가시키고 다각형의 정보를 출력
            times+=1
            print(polygons[-1].vertex_info())

        else:
            print("잘못된 꼭지점 개수입니다.")
            

    # 다각형의 정보를 출력
    elif a==2:
        print_vertex_info(polygons=polygons)

    # 선분 길이의 합을 출력
    elif a==3:
        print_vertex_info(polygons=polygons)
        num=int(input("선분 길이를 구할 다각형의 번호를 입력하세요 : "))
        print(f'{polygons[num].vertex_info()}의 선분 길이의 합은 {polygons[num].length()}')
    
    # 면적을 출력
    elif a==4:
        print_vertex_info(polygons=polygons)
        num=int(input("면적을 구할 다각형의 번호를 입력하세요 : "))
        print(f'{polygons[num].vertex_info()}의 면적은 {polygons[num].area()}')

    # 종료
    elif a==9:
        break