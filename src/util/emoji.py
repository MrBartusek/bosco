from typing import Union, TYPE_CHECKING
from util.constants import CUSTOM_EMOJIS
import emoji

if TYPE_CHECKING:
    from model.deepdives import Anomaly, MissionType, Warning

def get_emoji(model: Union["MissionType", "Warning", "Anomaly"]) -> Union[str, None]:
    return CUSTOM_EMOJIS.get(model.value, emoji.emojize(':black_medium_square:'))
