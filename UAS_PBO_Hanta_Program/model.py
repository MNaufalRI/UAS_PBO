class Patient:
    def __init__(self, age: int, gender: str, symptoms: str):
        # ENKAPSULASI : Atribut private menggunakan double underscore (__)
        self.__age = age
        self.__gender = gender
        self.__symptoms = symptoms

    # ENKAPSULASI : Getter menggunakan properti agar aman diakses dari luar kelas
    @property
    def age(self) -> int:
        return self.__age

    @property
    def gender(self) -> str:
        return self.__gender

    @property
    def symptoms(self) -> str:
        return self.__symptoms

    # POLIMORFISME : Meng-override dunder method __str__ untuk representasi string objek Patient
    def __str__(self):
        return f"Pasien({self.__age} tahun, {self.__gender})"


class HantaCase:
    def __init__(self, case_id: str, country: str, strain: str, transmission_type: str, exposure_source: str, patient: Patient, hospitalized: str, fatality: str, recovery_days: int, temp: float, humidity: float, quarantine_days: int):
        # ENKAPSULASI : Mengamankan seluruh variabel kasus medis
        self.__case_id = case_id
        self.__country = country
        self.__strain = strain
        self.__transmission_type = transmission_type
        self.__exposure_source = exposure_source
        # ASOSIASI / KOMPOSISI : Kelas HantaCase menyimpan instance dari objek Patient
        self.__patient = patient
        self.__hospitalized = hospitalized
        self.__fatality = fatality
        self.__recovery_days = recovery_days
        self.__temp = temp
        self.__humidity = humidity
        self.__quarantine_days = quarantine_days

    @property
    def case_id(self) -> str:
        return self.__case_id

    @property
    def country(self) -> str:
        return self.__country

    @property
    def strain(self) -> str:
        return self.__strain

    @property
    def transmission_type(self) -> str:
        return self.__transmission_type

    @property
    def exposure_source(self) -> str:
        return self.__exposure_source

    @property
    def patient(self) -> Patient:
        return self.__patient

    @property
    def recovery_days(self) -> int:
        return self.__recovery_days

    @property
    def temp(self) -> float:
        return self.__temp

    @property
    def humidity(self) -> float:
        return self.__humidity

    @property
    def quarantine_days(self) -> int:
        return self.__quarantine_days

    def is_hospitalized(self) -> bool:
        return self.__hospitalized.strip().lower() == "yes"

    def is_fatal(self) -> bool:
        return self.__fatality.strip().lower() == "yes"

    # POLIMORFISME : Meng-override dunder method __str__ untuk cetak ringkas objek HantaCase
    def __str__(self):
        return f"Kasus {self.__case_id} di {self.__country} ({self.__strain})"