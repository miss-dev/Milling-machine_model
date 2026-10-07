# Source Code

<!-- GUIDE: Projects use different stacks, so this template does not impose a code layout.
     Choose one in Phase 2, describe it in "Our layout" below, and delete the examples you
     don't use. -->

## Rules for every stack

1. **Organise by subsystem** where you can, using the same names as [docs/03-subsystems/](../docs/03-subsystems/README.md).
2. **Every top-level code folder has a `README.md`** covering what it does, its dependencies (with versions), how to build or flash it, how to run it, and its configuration.
3. **Pin your versions.** Use `requirements.txt` or `pyproject.toml` for Python, `platformio.ini` for PlatformIO, the ESP-IDF or Zephyr version for those SDKs, `package.xml` plus the ROS distro name for ROS, and `package-lock.json` for Node.js. Record board and library versions for Arduino IDE projects, and CUDA and driver versions for GPU training.
4. **No magic numbers.** Pin numbers, gains, thresholds, calibration values and model hyperparameters go in one clearly named config file or header, with units in a comment.
5. **No secrets in code.** See [CONTRIBUTING.md](../CONTRIBUTING.md#secrets).
6. **Notebooks are for exploring.** Once something in a Jupyter notebook works, move it into a module and keep the notebook as a record, linked from an experiment.
7. **Tests live next to the code** and follow your stack's conventions (`test/` in PlatformIO, `test/` in a ROS package, `tests/` for Python).
8. **Make results reproducible.** Training and analysis scripts take a config file and a random seed, and log the code version (commit hash) and dataset version with every result.

## Our layout

TODO: Describe your actual layout and why you chose it.

## Example layouts

### Microcontroller with PlatformIO (Arduino, ESP32, STM32, RP2040; recommended over Arduino IDE for team projects)

```
src/
└── firmware/
    ├── platformio.ini        # board, framework, library versions
    ├── include/config.h      # pins, constants, gains (with units)
    ├── src/main.cpp
    ├── lib/                  # your own libraries, one per subsystem
    │   ├── sensors/
    │   ├── comms/
    │   └── actuators/
    ├── test/
    └── README.md
```

### Vendor SDK (ESP-IDF, Zephyr, STM32Cube, Pico SDK)

```
src/
└── firmware/
    ├── CMakeLists.txt
    ├── main/                 # app_main / main.c, config.h
    ├── components/           # one per subsystem (ESP-IDF); modules/ or lib/ elsewhere
    │   ├── sensors/
    │   └── comms/
    ├── sdkconfig.defaults    # or prj.conf (Zephyr), .ioc (STM32Cube)
    └── README.md             # SDK version, target board, build and flash commands
```

### Arduino IDE sketch

```
src/
└── device_sketch/
    ├── device_sketch.ino     # folder and .ino names must match
    ├── config.h
    ├── sensors.h / sensors.cpp
    ├── secrets.example.h     # copy to secrets.h (ignored by git)
    └── README.md             # board, core version, libraries and versions
```

### ROS 2

```
src/
└── ros2_ws/
    └── src/
        ├── myproject_bringup/      # launch files, parameters
        ├── myproject_description/  # URDF, meshes
        ├── myproject_perception/
        ├── myproject_navigation/
        └── myproject_interfaces/   # custom messages and services
```

Build from `src/ros2_ws` with `colcon build`. The `build/`, `install/` and `log/` folders are ignored by git.

### Raspberry Pi / Linux device (Python)

```
src/
└── device/
    ├── pyproject.toml        # or requirements.txt
    ├── device/
    │   ├── __init__.py
    │   ├── main.py
    │   ├── config.py
    │   ├── sensors.py
    │   └── vision.py
    ├── tests/
    ├── systemd/app.service   # if it starts on boot
    └── README.md
```

### IoT back end and dashboard

```
src/
└── server/
    ├── docker-compose.yml    # broker, database, dashboard, your services
    ├── ingest/               # receives device messages (MQTT, HTTP, LoRaWAN webhook) and stores them
    ├── api/                  # if the app or dashboard needs one
    ├── dashboard/            # e.g. Grafana provisioning, Node-RED flows or a web app
    ├── .env.example          # copy to .env (ignored by git)
    └── README.md             # how to deploy, where it runs, who has access
```

### Machine learning (training, evaluation, deployment)

```
src/
└── ml/
    ├── pyproject.toml        # or requirements.txt; pin framework and CUDA versions
    ├── configs/              # one file per training run setup
    ├── ml/                   # reusable code: datasets, models, transforms, metrics
    ├── scripts/              # prepare_data.py, train.py, evaluate.py, export.py
    ├── notebooks/            # exploration, linked from experiments
    ├── tests/
    └── README.md             # where datasets and weights live (see the large-file policy)
```

Document each dataset with a [dataset card](../data/README.md#datasets) and each model with a [model card](../docs/02-design/ml-models/README.md). Keep raw data and large weights out of git; the `.gitignore` already excludes common weight formats.

### Mixed systems (e.g. microcontroller + Raspberry Pi + server)

Combine the layouts above, one folder per computing device or service: `src/firmware/`, `src/device/`, `src/server/`, `src/ml/`. Document the links between them (serial protocol, message formats, model file format) in [architecture.md](../docs/02-design/architecture.md#4-interfaces).
