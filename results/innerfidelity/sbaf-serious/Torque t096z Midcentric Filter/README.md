# Torque t096z Midcentric Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.3; 28 4.9; 31 4.5; 34 4.2; 37 4.0; 41 3.7; 45 3.4; 49 3.1; 54 2.8; 60 2.3; 66 2.0; 72 1.5; 79 1.1; 87 0.6; 96 0.1; 106 -0.2; 116 -0.4; 128 -0.8; 141 -1.3; 155 -1.5; 170 -1.7; 187 -1.8; 206 -2.0; 227 -1.8; 249 -1.9; 274 -1.8; 302 -1.7; 332 -1.5; 365 -1.3; 402 -1.0; 442 -0.6; 486 -0.5; 535 -0.2; 588 0.3; 647 0.5; 712 0.6; 783 0.8; 861 0.6; 947 0.2; 1042 -0.2; 1146 -0.5; 1261 -0.8; 1387 -1.4; 1526 -1.9; 1678 -2.3; 1846 -1.9; 2031 -1.5; 2234 -1.0; 2457 0.4; 2703 0.9; 2973 1.9; 3270 2.4; 3597 0.8; 3957 -1.8; 4353 -4.3; 4788 -3.0; 5267 0.9; 5793 4.1; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.3; 10263 -1.9; 11289 -1.4; 12418 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Midcentric Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.37 | 5.8 dB   |
| Peaking | 46 Hz    | 2    | 2.5 dB   |
| Peaking | 3327 Hz  | 1.81 | 10.9 dB  |
| Peaking | 4334 Hz  | 0.88 | -13.4 dB |
| Peaking | 6014 Hz  | 2.01 | 12.7 dB  |
| Peaking | 233 Hz   | 0.94 | -2.2 dB  |
| Peaking | 781 Hz   | 1.58 | 1.5 dB   |
| Peaking | 1640 Hz  | 3.13 | -1.1 dB  |
| Peaking | 2516 Hz  | 6.6  | 1.1 dB   |
| Peaking | 13829 Hz | 3.64 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Midcentric%20Filter/Torque%20t096z%20Midcentric%20Filter.png)