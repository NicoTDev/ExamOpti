class TeamCreds:
    teamName: str
    password: str


class SolutionApiModel:
    credentials: TeamCreds
    dayNumber: int
    steps: list[str]


class TruckDaily:
    Id: int
    AffiliatedWarehouseId: int
    Capacity: int


class LegosQty:
    LegoId: int
    Quantity: int


class CustomerDaily:
    Id: int
    Orders: list[LegosQty]


class LegoType:
    Id: int
    Weight: int


class Warehouse:
    Id: int
    Stock: list[LegosQty]


class Coords:
    X: int
    Y: int


class Daily:
    DayNumber: int
    Trucks: list[TruckDaily]
    Customers: list[CustomerDaily]
    Warehouses: list[Warehouse]
    Legos: list[LegoType]


class IdCoords:
    Id: int
    Coordinates: Coords


class MapData:
    Customers: list[IdCoords]
    Warehouses: list[IdCoords]
