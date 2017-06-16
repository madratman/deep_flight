import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='QuadNavGym-v0',
    entry_point='envs.navigate_envs:GazeboCylinderForestNav'
)
