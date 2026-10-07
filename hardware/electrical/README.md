# Electrical

<!-- GUIDE: Schematics, PCB designs and the wiring diagram. If you only use off-the-shelf
     modules connected by jumper wires, you still need a wiring diagram and a power budget.
     Those are the first things anyone debugging your device will ask for. -->

**Tool and version:** TODO: e.g. KiCad 8, Fritzing, draw.io

## File index

| Item | Source file | Export (PDF/PNG) | Version | Notes |
|---|---|---|---|---|
| Wiring diagram | TODO | TODO | v1 | TODO |
| TODO: e.g. Sensor breakout PCB | TODO | TODO | v1 | TODO |

## Pin assignments

<!-- GUIDE: Every pin you use on every microcontroller and computer. Keep this in sync with
     the code. A mismatch here is one of the most common integration bugs. -->

| Board | Pin | Connected to | Signal / function | Notes |
|---|---|---|---|---|
| TODO: e.g. ESP32-S3 | TODO: e.g. GPIO 5 | TODO: e.g. SHT31 SDA | TODO: e.g. I2C data (sensor address 0x44) | TODO |

## Power budget

<!-- GUIDE: Can your battery and regulators supply everything, including at peak? For
     battery-powered devices that sleep, also work out the average current over a whole
     cycle (sleep, wake, sense, transmit): that sets the battery life. Estimate in Phase 2,
     then measure in Phase 3 and record the experiment. Mains-powered only? Note the supply
     rating and skip the battery line. -->

| Component | Supply rail | Typical current | Peak current | Source of figure |
|---|---|---|---|---|
| TODO | TODO: e.g. 5 V | TODO | TODO | TODO: datasheet / measured (EXP-…) |
| **Total per rail** | | TODO | TODO | |

**Battery:** TODO: chemistry, voltage, capacity · **Estimated run time:** TODO · **Measured run time:** TODO

## Safety

<!-- GUIDE: Tick what applies; mark the rest "not applicable". -->

- [ ] Fuse on the main battery line, rated for the expected peak current
- [ ] Systems with motors or other moving parts: an emergency stop that cuts actuator power physically, not only in software
- [ ] Battery charging and storage rules followed (LiPo bag, never left charging unattended); cells have protection against short circuit and over-discharge
- [ ] No exposed conductors at battery voltage
- [ ] Mains voltage (if any) only inside closed, certified modules or power supplies, never on a breadboard
