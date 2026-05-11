class Product:
    def __init__(self, serialNumber: int, title: str, regularPrice: float):
        self.serialNumber = serialNumber
        self.title = title
        self.regularPrice = regularPrice

    def setRegularPrice(self, price: float):
        self.regularPrice = price

    def getRegularPrice(self) -> float:
        return self.regularPrice

    def setSerialNumber(self, sn: int):
        self.serialNumber = sn

    def getSerialNumber(self) -> int:
        return self.serialNumber

    def setTitle(self, title: str):
        self.title = title

    def getTitle(self) -> str:
        return self.title

    def __str__(self) -> str:
        return (f"Serial Number: {self.serialNumber}, "
                f"Title: {self.title}, "
                f"Regular Price: {self.regularPrice}")


class Electronics(Product):
    def __init__(self, serialNumber: int, title: str, regularPrice: float,
                 mafct: str, discount: float):
        super().__init__(serialNumber, title, regularPrice)
        self.manufacturer = mafct
        self.discount = discount

    def setManufacturer(self, mafct: str):
        self.manufacturer = mafct

    def getManufacturer(self) -> str:
        return self.manufacturer

    def setDiscount(self, discount: float):
        self.discount = discount

    def getDiscount(self) -> float:
        return self.discount

    def computeDiscount(self, regularPrice: float, discount: float) -> float:
        return regularPrice * (1 - discount)

    def __str__(self) -> str:
        return (f"{super().__str__()}, "
                f"Manufacturer: {self.manufacturer}, "
                f"Discount: {self.discount}")


class TVs(Electronics):
    def __init__(self, serialNumber: int, title: str, regularPrice: float,
                 mafct: str, size: int, SmartTv: bool, discount: float):
        super().__init__(serialNumber, title, regularPrice, mafct, discount)
        self.size = size
        self.smartTV = SmartTv

    def setSize(self, size: int):
        self.size = size

    def getSize(self) -> int:
        return self.size

    def setSmartTv(self, smart: bool):
        self.smartTV = smart

    def getSmartTv(self) -> bool:
        return self.smartTV

    def computeDiscount(self, regularPrice: float, discount: float) -> float:
        return regularPrice * (1 - discount)


class Books(Product):
    def __init__(self, serialNumber: int, title: str, regularPrice: float,
                 publisher: str, yearPublished: int, discount: float):
        super().__init__(serialNumber, title, regularPrice)
        self.author = publisher
        self.yearPublished = yearPublished
        self.discount = discount

    def setAuthor(self, Author: str):
        self.author = Author

    def getAuthor(self) -> str:
        return self.author

    def setYear(self, Year: int):
        self.yearPublished = Year

    def getYear(self) -> int:
        return self.yearPublished

    def setDiscount(self, discount: float):
        self.discount = discount

    def getDiscount(self) -> float:
        return self.discount

    def computeDiscount(self, regularPrice: float, discount: float) -> float:
        return regularPrice * (1 - discount)

    def __str__(self) -> str:
        return (f"{super().__str__()}, "
                f"Author: {self.author}, "
                f"Year Published: {self.yearPublished}, "
                f"Discount: {self.discount}")