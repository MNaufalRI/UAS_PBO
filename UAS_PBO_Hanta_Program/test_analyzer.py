import unittest
from model import Patient, HantaCase
from analyzer import ClinicalAnalyzer, DemographicAnalyzer, TransmissionAnalyzer, EnvironmentalAnalyzer, QuarantineAnalyzer

# PEWARISAN (Inheritance) : Mewarisi sifat TestCase dari modul unittest bawaan Python
class TestHantaAnalyzer(unittest.TestCase):

    # SETUP METHOD : Menyiapkan tiruan objek data rekam medis (mock data) sebelum pengujian dimulai
    def setUp(self):
        # Instansiasi objek komponen Patient (Enkapsulasi)
        p1 = Patient(age=20, gender="Male", symptoms="Fever")
        p2 = Patient(age=60, gender="Female", symptoms="Cough")
        
        # Instansiasi objek kasus rekam medis HantaCase (Asosiasi Komposisi)
        self.c1 = HantaCase("HV001", "Indonesia", "Seoul", "Rodent-to-Human", "Home", p1, "Yes", "No", 10, 25.0, 50.0, 14)
        self.c2 = HantaCase("HV002", "Indonesia", "Andes", "Human-to-Human", "Forest", p2, "Yes", "Yes", 0, 35.0, 70.0, 7)
        
        self.mock_cases = [self.c1, self.c2]

    # UNIT TEST 1 : Menguji fungsionalitas hitungan ClinicalAnalyzer
    def test_clinical_analyzer(self):
        analyzer = ClinicalAnalyzer(self.mock_cases)
        result = analyzer.analyze()

        self.assertEqual(result["hospitalization_rate"], 100.0)
        self.assertEqual(result["fatality_rate"], 50.0)
        self.assertEqual(result["hosp_count"], 2)
        self.assertEqual(result["fatal_count"], 1)

    # UNIT TEST 2 : Menguji fungsionalitas hitungan DemographicAnalyzer
    def test_demographic_analyzer(self):
        analyzer = DemographicAnalyzer(self.mock_cases)
        result = analyzer.analyze()

        self.assertEqual(result["average_age"], 40.0)
        self.assertEqual(result["male_count"], 1)
        self.assertEqual(result["female_count"], 1)

    # UNIT TEST 3 : Menguji fungsionalitas hitungan EnvironmentalAnalyzer
    def test_environmental_analyzer(self):
        analyzer = EnvironmentalAnalyzer(self.mock_cases)
        result = analyzer.analyze()

        self.assertEqual(result["avg_temperature"], 30.0)
        self.assertEqual(result["avg_humidity"], 60.0)
        self.assertEqual(result["min_temp"], 25.0)
        self.assertEqual(result["max_temp"], 35.0)

    # UNIT TEST 4 : Menguji fungsionalitas hitungan QuarantineAnalyzer
    def test_quarantine_analyzer(self):
        analyzer = QuarantineAnalyzer(self.mock_cases)
        result = analyzer.analyze()

        self.assertEqual(result["avg_quarantine_days"], 10.5)
        self.assertEqual(result["min_q"], 7)
        self.assertEqual(result["max_q"], 14)


if __name__ == "__main__":
    unittest.main()