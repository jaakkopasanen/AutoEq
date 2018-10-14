# Torque t402v OverEar Red

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.3dB
GraphicEQ: 21 0.0; 23 5.4; 25 4.4; 28 3.0; 31 1.8; 34 0.8; 37 -0.1; 41 -1.1; 45 -1.9; 49 -2.6; 54 -3.3; 60 -4.1; 66 -4.6; 72 -5.0; 79 -5.3; 87 -5.9; 96 -6.7; 106 -7.4; 116 -7.8; 128 -8.4; 141 -8.7; 155 -9.1; 170 -8.9; 187 -9.5; 206 -9.9; 227 -10.1; 249 -10.4; 274 -10.6; 302 -10.6; 332 -10.2; 365 -9.7; 402 -8.7; 442 -6.6; 486 -4.4; 535 -2.1; 588 0.7; 647 2.7; 712 4.1; 783 4.4; 861 3.0; 947 1.2; 1042 -0.9; 1146 -1.5; 1261 -2.5; 1387 -3.3; 1526 -4.6; 1678 -3.3; 1846 -0.7; 2031 -0.0; 2234 -1.3; 2457 -1.9; 2703 -2.3; 2973 -1.4; 3270 1.0; 3597 1.7; 3957 1.9; 4353 1.5; 4788 1.9; 5267 3.4; 5793 3.6; 6373 2.1; 7010 1.3; 7711 -2.1; 8482 -4.7; 9330 -2.4; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.3dB` and instead set Global volume in the UI for both channels to **-73**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Red ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.21 | 7.8 dB  |
| Peaking | 133 Hz  | 0.44 | -6.7 dB |
| Peaking | 349 Hz  | 0.82 | -8.2 dB |
| Peaking | 705 Hz  | 1.53 | 9.1 dB  |
| Peaking | 1425 Hz | 2.23 | -4.6 dB |
| Peaking | 1990 Hz | 6.03 | 2.3 dB  |
| Peaking | 2862 Hz | 1.87 | -3.4 dB |
| Peaking | 3422 Hz | 3.21 | 3.5 dB  |
| Peaking | 5714 Hz | 1.93 | 4.0 dB  |
| Peaking | 8473 Hz | 4.59 | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Red/Torque%20t402v%20OverEar%20Red.png)