from typing import List, cast, Dict
from openpilot.selfdrive.car.body.values import CAR as BODY
from openpilot.selfdrive.car.chrysler.values import CAR as CHRYSLER
from openpilot.selfdrive.car.ford.values import CAR as FORD
from openpilot.selfdrive.car.gm.values import CAR as GM
from openpilot.selfdrive.car.honda.values import CAR as HONDA
from openpilot.selfdrive.car.hyundai.values import CAR as HYUNDAI
from openpilot.selfdrive.car.mazda.values import CAR as MAZDA
from openpilot.selfdrive.car.nissan.values import CAR as NISSAN
from openpilot.selfdrive.car.subaru.values import CAR as SUBARU
from openpilot.selfdrive.car.tesla.values import CAR as TESLA
from openpilot.selfdrive.car.toyota.values import CAR as TOYOTA
from openpilot.selfdrive.car.volkswagen.values import CAR as VOLKSWAGEN

Platform = BODY | CHRYSLER | FORD | GM | HONDA | HYUNDAI | MAZDA | NISSAN | SUBARU | TESLA | TOYOTA | VOLKSWAGEN
BRANDS = [BODY, CHRYSLER, FORD, GM, HONDA, HYUNDAI, MAZDA, NISSAN, SUBARU, TESLA, TOYOTA, VOLKSWAGEN]

PLATFORMS: Dict[str, Platform] = {str(platform): platform for brand in BRANDS for platform in cast(List[Platform], brand)}
