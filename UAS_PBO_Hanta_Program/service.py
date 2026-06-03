import os
from repository import Repository
from analyzer import (
    ClinicalAnalyzer, DemographicAnalyzer, TransmissionAnalyzer,
    EnvironmentalAnalyzer, QuarantineAnalyzer, StrainAnalyzer
)

# SOLID : Single Responsibility Principle (SRP)
# Service Layer ini bertanggung jawab khusus sebagai perantara logika bisnis (Business Logic).
# Memisahkan tanggung jawab UI (MainMenu) dari instansiasi detail analitik dan manipulasi data.
class HantaService:
    # SOLID : Dependency Inversion Principle (DIP)
    # Service bergantung pada abstraksi Repository, bukan pada HantaRepository yang konkret.
    def __init__(self, repository: Repository):
        self.__repo = repository
        self.__data_loaded = False

    def get_source_name(self) -> str:
        return self.__repo.get_source_name()

    def check_file_exists(self, file_path: str) -> bool:
        return os.path.exists(file_path)

    def load_data(self):
        self.__repo.load_data()
        self.__data_loaded = True

    def is_data_loaded(self) -> bool:
        return self.__data_loaded

    def get_cases(self) -> list:
        return self.__repo.get_all_cases()

    # ENKAPSULASI LOGIKA BISNIS: 
    def analyze_clinical(self) -> dict:
        analyzer = ClinicalAnalyzer(self.__repo.get_all_cases())
        return analyzer.analyze()

    def analyze_demographic(self) -> dict:
        analyzer = DemographicAnalyzer(self.__repo.get_all_cases())
        return analyzer.analyze()

    def analyze_transmission(self) -> dict:
        analyzer = TransmissionAnalyzer(self.__repo.get_all_cases())
        return analyzer.analyze()

    def analyze_environmental(self) -> dict:
        analyzer = EnvironmentalAnalyzer(self.__repo.get_all_cases())
        return analyzer.analyze()

    def analyze_quarantine(self) -> dict:
        analyzer = QuarantineAnalyzer(self.__repo.get_all_cases())
        return analyzer.analyze()

    def analyze_strain(self) -> dict:
        analyzer = StrainAnalyzer(self.__repo.get_all_cases())
        return analyzer.analyze()