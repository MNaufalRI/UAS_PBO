from abc import ABC, abstractmethod

# ABSTRAKSI : Blueprint kelas induk abstrak yang menggunakan modul ABC
# SOLID : Open/Closed Principle (OCP) & Liskov Substitution Principle (LSP)
class BaseAnalyzer(ABC):
    def __init__(self, cases: list):
        self._cases = cases

    # ABSTRAKSI : Method abstrak tanpa implementasi yang wajib dibuat ulang oleh kelas anak
    @abstractmethod
    def analyze(self) -> dict:
        pass


# PEWARISAN (Inheritance) : ClinicalAnalyzer mewarisi sifat dari BaseAnalyzer
# SOLID : Single Responsibility Principle (SRP)
# Kelas ini hanya memiliki satu alasan untuk berubah, yaitu jika rumus analisis klinis berubah.
class ClinicalAnalyzer(BaseAnalyzer):
    # POLIMORFISME (Method Overriding) : Menyediakan logika analisis klinis spesifik
    def analyze(self) -> dict:
        total = len(self._cases)
        if total == 0:
            return {"hospitalization_rate": 0.0, "fatality_rate": 0.0, "hosp_count": 0, "fatal_count": 0, "recovered_count": 0}
        
        hospitalized_count = sum(1 for c in self._cases if c.is_hospitalized())
        fatal_count = sum(1 for c in self._cases if c.is_fatal())
        recovered_count = total - fatal_count  # Yang tidak fatal berarti berhasil sembuh
        
        return {
            "hospitalization_rate": (hospitalized_count / total) * 100,
            "fatality_rate": (fatal_count / total) * 100,
            "hosp_count": hospitalized_count,
            "fatal_count": fatal_count,
            "recovered_count": recovered_count
        }

# PEWARISAN (Inheritance) : DemographicAnalyzer mewarisi sifat dari BaseAnalyzer
class DemographicAnalyzer(BaseAnalyzer):
    # POLIMORFISME (Method Overriding) : Menyediakan logika analisis demografi umur/gender
    def analyze(self) -> dict:
        total = len(self._cases)
        if total == 0:
            return {"average_age": 0.0, "male_count": 0, "female_count": 0, "age_groups": {}}
        
        total_age = sum(c.patient.age for c in self._cases)
        male_count = sum(1 for c in self._cases if c.patient.gender.strip().lower() == "male")
        female_count = sum(1 for c in self._cases if c.patient.gender.strip().lower() == "female")
        
        # Detail pengelompokan usia
        anak = sum(1 for c in self._cases if c.patient.age < 18)
        dewasa = sum(1 for c in self._cases if 18 <= c.patient.age <= 59)
        lansia = sum(1 for c in self._cases if c.patient.age >= 60)
        
        return {
            "average_age": total_age / total,
            "male_count": male_count,
            "female_count": female_count,
            "age_groups": {"Anak-anak (0-17 tahun)": anak, "Dewasa (18-59 tahun)": dewasa, "Lansia (60+ tahun)": lansia}
        }


# PEWARISAN (Inheritance) : Kelas untuk menganalisis penyebaran pola epidemiologi virus
class TransmissionAnalyzer(BaseAnalyzer):
    # POLIMORFISME (Method Overriding) : Menyediakan logika analisis pola transmisi penyebaran virus
    def analyze(self) -> dict:
        total = len(self._cases)
        if total == 0:
            return {"most_common_transmission": "N/A", "most_common_exposure": "N/A"}
        
        transmission_counts = {}
        exposure_counts = {}
        
        for c in self._cases:
            t_type = c.transmission_type
            e_source = c.exposure_source
            transmission_counts[t_type] = transmission_counts.get(t_type, 0) + 1
            exposure_counts[e_source] = exposure_counts.get(e_source, 0) + 1
            
        most_common_transmission = max(transmission_counts, key=transmission_counts.get)
        most_common_exposure = max(exposure_counts, key=exposure_counts.get)
        
        return {
            "most_common_transmission": most_common_transmission,
            "most_common_exposure": most_common_exposure,
            "transmission_counts": transmission_counts,
            "exposure_counts": exposure_counts
        }


# PEWARISAN : Menganalisis korelasi data iklim/cuaca lingkungan terhadap sebaran wabah
class EnvironmentalAnalyzer(BaseAnalyzer):
    # POLIMORFISME (Method Overriding) : Meng-override rumus untuk menghitung faktor rata-rata cuaca
    def analyze(self) -> dict:
        total = len(self._cases)
        if total == 0:
            return {"avg_temperature": 0.0, "avg_humidity": 0.0}
        
        temps = [c.temp for c in self._cases]
        humidities = [c.humidity for c in self._cases]
        
        return {
            "avg_temperature": sum(temps) / total,
            "avg_humidity": sum(humidities) / total,
            "min_temp": min(temps),
            "max_temp": max(temps),
            "min_humidity": min(humidities),
            "max_humidity": max(humidities)
        }


# PEWARISAN : Menganalisis efektivitas durasi karantina pasien
class QuarantineAnalyzer(BaseAnalyzer):
    # POLIMORFISME (Method Overriding) : Meng-override rumus untuk menghitung manajemen durasi isolasi
    def analyze(self) -> dict:
        total = len(self._cases)
        if total == 0:
            return {"avg_quarantine_days": 0.0, "avg_recovery_days": 0.0}
        
        q_days = [c.quarantine_days for c in self._cases]
        r_days = [c.recovery_days for c in self._cases]
        
        return {
            "avg_quarantine_days": sum(q_days) / total,
            "avg_recovery_days": sum(r_days) / total,
            "min_q": min(q_days),
            "max_q": max(q_days),
            "min_r": min(r_days),
            "max_r": max(r_days)
        }


# PEWARISAN : Menganalisis karakteristik spesifik dari tiap Strain Virus (Varian)
class StrainAnalyzer(BaseAnalyzer):
    # POLIMORFISME (Method Overriding) : Mengelompokkan data berdasarkan jenis varian strain virus
    def analyze(self) -> dict:
        strain_data = {}
        
        for c in self._cases:
            s_name = c.strain
            if s_name not in strain_data:
                strain_data[s_name] = {"count": 0, "fatal_count": 0, "total_recovery_days": 0}
                
            strain_data[s_name]["count"] += 1
            if c.is_fatal():
                strain_data[s_name]["fatal_count"] += 1
            strain_data[s_name]["total_recovery_days"] += c.recovery_days
            
        results = {}
        for s_name, data in strain_data.items():
            count = data["count"]
            results[s_name] = {
                "total_cases": count,
                "fatality_rate": (data["fatal_count"] / count) * 100,
                "avg_recovery_days": data["total_recovery_days"] / count
            }
        return results