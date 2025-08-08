from .env import Env
from .recorder import Recorder

# Register only Gymnasium environments using the Gymnasium API.
try:
    import gymnasium as gym

    gym.register(
        id="CrafterReward-v2",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": True},
    )
    gym.register(
        id="CrafterNoReward-v2",
        entry_point="crafter:Env",
        max_episode_steps=10000,
        kwargs={"reward": False},
    )
except Exception:
    pass
