import csv
import os
from abc import ABC, abstractmethod
from model import Patient, HantaCase

# SOLID : Interface Segregation Principle (ISP) & Dependency Inversion Principle (DIP)
# Memisahkan kontrak (interface) dari implementasi. Klien (MainMenu) hanya akan bergantung
# pada antarmuka abstrak ini, bukan pada logika baca CSV yang spesifik.
class Repository(ABC):
    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def get_all_cases(self) -> list:
        pass

    @abstractmethod
    def get_source_name(self) -> str:
        pass


class HantaRepository(Repository):
    def __init__(self, file_path: str):
        self.__file_path = file_path
        # DATA STRUCTURE INTEGRATION : List objek untuk menampung data rekam medis
        self.__cases = []

    def load_data(self):
        self.__cases = []
        with open(self.__file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # INSTANSIASI OBJEK : Mengonversi data baris teks menjadi objek beneran
                patient = Patient(
                    age=int(row['patient_age']),
                    gender=row['gender'],
                    symptoms=row['symptoms']
                )
                hanta_case = HantaCase(
                    case_id=row['case_id'],
                    country=row['country'],
                    strain=row['virus_strain'],
                    transmission_type=row['transmission_type'],
                    exposure_source=row['exposure_source'],
                    patient=patient,
                    hospitalized=row['hospitalization'],
                    fatality=row['fatality'],
                    recovery_days=int(row['recovery_days']) if row['recovery_days'].isdigit() else 0,
                    temp=float(row['temperature_celsius']) if row['temperature_celsius'] else 0.0,
                    humidity=float(row['humidity_percent']) if row['humidity_percent'] else 0.0,
                    quarantine_days=int(row['quarantine_days']) if row['quarantine_days'].isdigit() else 0
                )
                self.__cases.append(hanta_case)

    def get_all_cases(self) -> list:
        return self.__cases

    def get_source_name(self) -> str:
        return self.__file_path

    # STATIC METHOD : Method utilitas independen milik kelas (bisa dipanggil tanpa instansiasi objek)
    @staticmethod
    def check_file_exists(file_path: str) -> bool:
        return os.path.exists(file_path)