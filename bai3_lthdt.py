
""""
Mã sinh viên: 202419031
Họ tên: Nguyễn Việt Anh 
Lớp: lập trình hướng đối tượng
Bài : 3
"""
# LỚP EMPLOYEE 
class Employee:
    def __init__(self, emp_id: str = "UNKNOWN", full_name: str = "Unnamed employee", base_salary: float = 0.0):
        self._id = emp_id
        self._full_name = full_name
        self._base_salary = float(base_salary)
        self.validate_attributes()

    def validate_attributes(self):
        if not self._id or not str(self._id).strip():
            raise ValueError("Lỗi: Mã nhân sự không được để rỗng!")
        if not self._full_name or not str(self._full_name).strip():
            raise ValueError("Lỗi: Họ tên nhân sự không được để rỗng!")
        if self._base_salary < 0:
            raise ValueError("Lỗi: Lương cơ bản không được âm!")

    @property
    def id(self) -> str:
        return self._id

    @property
    def full_name(self) -> str:
        return self._full_name

    @property
    def base_salary(self) -> float:
        return self._base_salary

    @base_salary.setter
    def base_salary(self, value: float):
        if value < 0:
            raise ValueError("Lỗi: Lương cơ bản không được âm!")
        self._base_salary = float(value)

    def increase_salary(self, value: float, by_percentage: bool = False):
        if value <= 0:
            print(f"[Lỗi increase_salary] Giá trị tăng lương ({value}) phải là số dương!")
            return False

        if by_percentage:
            increase_amount = self._base_salary * (value / 100.0)
            self._base_salary += increase_amount
            print(f"-> Đã tăng {value}% (+{increase_amount:,.2f} VNĐ) cho {self._full_name}. Lương mới: {self._base_salary:,.2f} VNĐ")
        else:
            self._base_salary += value
            print(f"-> Đã tăng {value:,.2f} VNĐ cho {self._full_name}. Lương mới: {self._base_salary:,.2f} VNĐ")
        return True

    def calculate_monthly_cost(self) -> float:
        return self._base_salary

    def display_info(self):
        print(f"Loại nhân sự  : Nhân sự thông thường")
        print(f"Mã nhân sự    : {self._id}")
        print(f"Họ và tên     : {self._full_name}")
        print(f"Lương cơ bản  : {self._base_salary:,.2f} VNĐ")
        print(f"Chi phí tháng : {self.calculate_monthly_cost():,.2f} VNĐ")

    def __del__(self):
        print(f" Hủy đối tượng Employee: {getattr(self, '_id', 'N/A')} - {getattr(self, '_full_name', 'N/A')}")
# LỚP SOFTWAREENGINEER
class SoftwareEngineer(Employee):
    def __init__(self, emp_id: str, full_name: str, base_salary: float = 0.0, 
                 primary_language: str = "C++", technical_allowance: float = 0.0):
        if isinstance(base_salary, str):
            technical_allowance = 0.0
            primary_language = base_salary
            base_salary = 0.0
        super().__init__(emp_id, full_name, base_salary)
        self._primary_language = primary_language
        self._technical_allowance = float(technical_allowance)
        self.validate_se_attributes()
    def validate_se_attributes(self):
        if not self._primary_language or not str(self._primary_language).strip():
            raise ValueError("Lỗi: Ngôn ngữ lập trình chính không được để rỗng!")
        if self._technical_allowance < 0:
            raise ValueError("Lỗi: Phụ cấp kỹ thuật không được âm!")

    @property
    def primary_language(self) -> str:
        return self._primary_language

    @property
    def technical_allowance(self) -> float:
        return self._technical_allowance
    def calculate_monthly_cost(self) -> float:
        return self._base_salary + self._technical_allowance
    def display_info(self):
        print(f"Loại nhân sự  : Kỹ sư phần mềm")
        print(f"Mã nhân sự    : {self._id}")
        print(f"Họ và tên     : {self._full_name}")
        print(f"Ngôn ngữ chính: {self._primary_language}")
        print(f"Lương cơ bản  : {self._base_salary:,.2f} VNĐ")
        print(f"Phụ cấp KT    : {self._technical_allowance:,.2f} VNĐ")
        print(f"Chi phí tháng : {self.calculate_monthly_cost():,.2f} VNĐ")
    def __del__(self):
        print(f"[Destructor SoftwareEngineer] Hủy đối tượng Kỹ sư: {getattr(self, '_id', 'N/A')} - {getattr(self, '_full_name', 'N/A')}")

# LỚP PROJECTTEAM 
class ProjectTeam:
    def __init__(self, project_code: str, project_name: str, leader: Employee = None):
        self._project_code = project_code
        self._project_name = project_name
        self._leader = None
        self._members = []
        if leader is not None:
            self._leader = leader
            self._members.append(leader)
    def contains(self, employee_id: str) -> bool:
        return any(m.id == employee_id for m in self._members)
    def add_member(self, employee: Employee, make_leader: bool = False) -> bool:
        if self.contains(employee.id):
            print(f"[Lỗi add_member] Nhân sự {employee.full_name} ({employee.id}) đã tồn tại trong nhóm!")
            return False
        self._members.append(employee)
        if make_leader:
            self._leader = employee
            print(f"-> Đã thêm {employee.full_name} và thiết lập làm TRƯỞNG NHÓM.")
        else:
            print(f"-> Đã thêm thành viên {employee.full_name} vào nhóm.")
        return True
    def change_leader(self, employee: Employee) -> bool:
        if not self.contains(employee.id):
            self.add_member(employee)
        self._leader = employee
        print(f"-> Đã đổi trưởng nhóm thành: {employee.full_name}")
        return True
    def remove_member(self, employee_id: str) -> bool:
        if self._leader is not None and self._leader.id == employee_id:
            print(f"Không thể xóa trưởng nhóm ({employee_id}) khi chưa chọn trưởng nhóm thay thế")
            return False
        for i, m in enumerate(self._members):
            if m.id == employee_id:
                removed_name = m.full_name
                del self._members[i]
                print(f"-> Đã xóa nhân sự ({removed_name}) ra khỏi nhóm {self._project_code}")
                return True
        print(f"Không tìm thấy nhân sự {employee_id} trong nhóm")
        return False
    def calculate_total_monthly_cost(self) -> float:
        return sum(m.calculate_monthly_cost() for m in self._members)
    def display_team(self):
        print(f"THÔNG TIN NHÓM DỰ ÁN: [{self._project_code}] {self._project_name}")
        leader_str = f"{self._leader.full_name} ({self._leader.id})" if self._leader else "Chưa có"
        print(f"Trưởng nhóm: {leader_str}")
        print(f"Số lượng thành viên: {len(self._members)}")
        for m in self._members:
            m.display_info()
        print(f"TỔNG CHI PHÍ HẰNG THÁNG CỦA NHÓM: {self.calculate_total_monthly_cost():,.2f} VNĐ")
    def __del__(self):
        print(f"[Destructor ProjectTeam] Hủy nhóm dự án: {getattr(self, '_project_code', 'N/A')} - {getattr(self, '_project_name', 'N/A')} (Các nhân sự bên trong không bị hủy)")

# KIỂM THỬ TRƯỜNG HỢP BIÊN 
def run_boundary_tests():
    print("BẮT ĐẦU KIỂM THỬ CÁC TRƯỜNG HỢP BIÊN")

    # 1. Test Mã nhân sự rỗng 
    try:
        e1 = Employee("", "Nguyễn Việt Anh", 10000000)
    except ValueError as err:
        print(f"Bắt thành công lỗi Mã rỗng: {err}")

    # 2. Test Họ tên rỗng
    try:
        e2 = Employee("E_TEST_2", "   ", 10000000)
    except ValueError as err:
        print(f"Bắt thành công lỗi Họ tên rỗng: {err}")

    # 3. Test Lương cơ bản âm
    try:
        e3 = Employee("E_TEST_3", "Trần Văn Bình ", -5000000)
    except ValueError as err:
        print(f"Bắt thành công lỗi Lương âm: {err}")

    # 4. Test Lương cơ bản = 0 (Giá trị biên hợp lệ)
    try:
        e4 = Employee("E_TEST_4", "Lê Văn Cường", 0)
        print(f"Khởi tạo lương = 0 hợp lệ: {e4.base_salary:,.2f} VNĐ")
    except Exception as err:
        print(f"Bị lỗi không mong muốn: {err}")

    # 5. Test Phụ cấp kỹ thuật âm
    try:
        se1 = SoftwareEngineer("SE_TEST_1", "Phạm Văn Dương", 15000000, "Python", -2000000)
    except ValueError as err:
        print(f"Bắt thành công lỗi Phụ cấp âm: {err}")

    # 6. Test Tăng lương với số tiền âm / bằng 0
    e_test = Employee("E_TEST_6", "Hoàng Văn E", 10000000)
    e_test.increase_salary(-2000000)  
    e_test.increase_salary(0)        
    e_test.increase_salary(5000000)  
    # 7. Test Xóa nhân sự không tồn tại trong nhóm
    team_test = ProjectTeam("PRJ_TEST", "Dự án Test Biên")
    team_test.add_member(e_test)
    print("\n-- Test xóa thành viên không tồn tại --")
    team_test.remove_member("ID_KHONG_TON_TAI")

    print("HOÀN THÀNH TẤT CẢ KIỂM THỬ TRƯỜNG HỢP BIÊN")
# KỊCH BẢN KIỂM THỬ CHÍNH 
def main():
    try:
        # Bước 1: Tạo hai Employee bằng hai constructor khác nhau
        print("Bước 1: Tạo 2 Employee")
        emp1 = Employee("E01", "Nguyễn Văn A")
        emp2 = Employee("E02", "Trần Thị B", 12000000)

        # Bước 2: Tạo hai SoftwareEngineer bằng hai constructor khác nhau
        print("\n Bước 2: Tạo 2 SoftwareEngineer")
        se1 = SoftwareEngineer("SE01", "Lê Văn C", "C++")
        se2 = SoftwareEngineer("SE02", "Phạm Minh D", 18000000, "Java", 4000000)

        # Bước 3: Tăng lương một nhân sự bằng số tiền cố định
        print("\nBước 3: Tăng lương cố định")
        emp1.increase_salary(10000000)

        # Bước 4: Tăng lương một nhân sự khác theo phần trăm
        print("\nBước 4: Tăng lương theo phần trăm ")
        se2.increase_salary(10, True)

        # Bước 5: Tạo nhóm dự án không có trưởng nhóm
        print("\nBước 5: Tạo nhóm dự án chưa có trưởng nhóm")
        team1 = ProjectTeam("PRJ_AI", "Hệ thống AI và Big Data")

        # Bước 6: Thêm một nhân sự vào nhóm bằng add_member(employee)
        print("\n Bước 6: Thêm nhân sự vào nhóm ")
        team1.add_member(emp1)
        team1.add_member(emp2)

        # Bước 7: Thêm một kỹ sư bằng add_member(employee, True) để đặt làm trưởng nhóm
        print("\nBước 7: Thêm kỹ sư làm trưởng nhóm")
        team1.add_member(se2, make_leader=True)

        # Bước 8: Thử thêm lại một thành viên đã tồn tại
        print("\nBước 8: Thử thêm lại thành viên đã có trong nhóm")
        team1.add_member(emp1)

        # Bước 9: Hiển thị danh sách bằng lời gọi đa hình
        print("\n Bước 9: Hiển thị thông tin nhóm dự án ")
        team1.display_team()

        # Bước 10: Tính tổng chi phí nhân sự hằng tháng
        print("Bước 10: Tổng chi phí nhân sự hằng tháng")
        print(f"Tổng chi phí Team 1: {team1.calculate_total_monthly_cost():,.2f} VNĐ\n")

        # Bước 11: Thử xóa trưởng nhóm hiện tại và kiểm tra thao tác bị từ chối
        print(" Bước 11: Thử xóa trưởng nhóm hiện tại ")
        team1.remove_member(se2.id)

        # Bước 12: Đổi trưởng nhóm rồi xóa người từng là trưởng nhóm
        print("\nBước 12: Đổi trưởng nhóm và xóa trưởng nhóm cũ")
        team1.change_leader(se1)
        team1.remove_member(se2.id)

        # Bước 13: Tạo nhóm thứ hai và thêm nhân sự đã có ở nhóm thứ nhất
        print("\nBước 13: Tạo nhóm 2 và thêm nhân sự đã có ở nhóm 1")
        
        def local_scope_demo():
            print("Vào phạm vi cục bộ ")
            team2 = ProjectTeam("PRJ_WEB", "Website Thương mại điện tử")
            team2.add_member(emp1, make_leader=True)
            team2.add_member(se1)
            team2.display_team()
            print("Chuẩn bị thoát phạm vi cục bộ ")
        local_scope_demo()

        # Bước 15: Chứng minh nhân sự của nhóm thứ hai vẫn tồn tại sau khi nhóm bị hủy
        print("\nBước 15: Kiểm tra emp1 và se1 sau khi team2 bị hủy ")
        print("Nhân sự emp1 vẫn tồn tại an toàn:")
        emp1.display_info()
        print("\nNhân sự se1 vẫn tồn tại an toàn trong Team 1:")
        team1.display_team()
    except Exception as e:
        print(f"\n {e}")
    run_boundary_tests()

if __name__ == "__main__":
    main()