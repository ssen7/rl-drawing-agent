from gym.envs.registration import registry, register, make, spec


register(
    id="drawobjects-v0",
    entry_point="gym_drawobjects.envs:DrawObjectsEnv")
