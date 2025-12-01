from gymnasium.envs.registration import register


def register_environments():

    register(
        id="airsim-drone-sample-v0",
        entry_point="airgym.envs:AirSimDroneEnv",
    )

    register(
        id="airsim-car-sample-v0",
        entry_point="airgym.envs:AirSimCarEnv",
    )
