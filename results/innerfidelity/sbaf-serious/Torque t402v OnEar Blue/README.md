# Torque t402v OnEar Blue

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.9; 23 -3.6; 25 -4.2; 28 -4.9; 31 -5.6; 34 -6.1; 37 -6.5; 41 -7.0; 45 -7.3; 49 -7.7; 54 -8.1; 60 -8.5; 66 -8.9; 72 -9.2; 79 -9.5; 87 -9.8; 96 -10.2; 106 -10.8; 116 -11.1; 128 -11.5; 141 -11.7; 155 -11.9; 170 -11.7; 187 -11.9; 206 -11.7; 227 -11.4; 249 -11.0; 274 -10.4; 302 -9.7; 332 -9.1; 365 -8.5; 402 -7.6; 442 -6.7; 486 -6.0; 535 -4.8; 588 -2.9; 647 -1.0; 712 0.9; 783 2.4; 861 2.5; 947 1.3; 1042 -1.0; 1146 -3.2; 1261 -5.0; 1387 -4.0; 1526 -4.6; 1678 -2.9; 1846 -1.8; 2031 -2.1; 2234 -3.1; 2457 -3.5; 2703 -3.5; 2973 -2.8; 3270 -1.7; 3597 -1.3; 3957 -1.3; 4353 -2.4; 4788 -1.3; 5267 3.0; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OnEar Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.38 | -8.9 dB |
| Peaking | 242 Hz  | 0.88 | -7.0 dB |
| Peaking | 2504 Hz | 0.85 | -3.2 dB |
| Peaking | 6040 Hz | 3.81 | 7.6 dB  |
| Peaking | 8112 Hz | 2.94 | -0.5 dB |
| Peaking | 479 Hz  | 1.69 | -3.2 dB |
| Peaking | 827 Hz  | 1.88 | 5.5 dB  |
| Peaking | 1121 Hz | 0.31 | 1.0 dB  |
| Peaking | 1270 Hz | 2.36 | -5.4 dB |
| Peaking | 4530 Hz | 7.73 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OnEar%20Blue/Torque%20t402v%20OnEar%20Blue.png)