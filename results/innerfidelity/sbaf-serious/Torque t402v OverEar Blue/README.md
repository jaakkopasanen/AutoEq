# Torque t402v OverEar Blue

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 21 -3.9; 23 -4.6; 25 -5.2; 28 -5.9; 31 -6.5; 34 -7.1; 37 -7.5; 41 -8.1; 45 -8.5; 49 -8.8; 54 -9.2; 60 -9.5; 66 -9.8; 72 -10.2; 79 -10.4; 87 -10.5; 96 -10.9; 106 -11.6; 116 -12.3; 128 -13.1; 141 -13.3; 155 -13.7; 170 -13.1; 187 -14.2; 206 -14.7; 227 -15.0; 249 -15.2; 274 -15.0; 302 -14.2; 332 -12.8; 365 -10.7; 402 -8.5; 442 -6.0; 486 -4.0; 535 -1.9; 588 0.6; 647 2.8; 712 4.1; 783 4.5; 861 3.4; 947 1.4; 1042 -1.2; 1146 -2.7; 1261 -3.6; 1387 -4.2; 1526 -4.5; 1678 -2.2; 1846 -0.2; 2031 0.0; 2234 -0.8; 2457 -1.0; 2703 -0.6; 2973 0.5; 3270 2.8; 3597 3.0; 3957 2.5; 4353 1.9; 4788 2.3; 5267 3.1; 5793 1.6; 6373 -1.4; 7010 -3.8; 7711 -5.1; 8482 -5.3; 9330 -1.5; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.6dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t402v OverEar Blue ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 236 Hz  | 0.12 | -12.3 dB |
| Peaking | 278 Hz  | 0.57 | -16.1 dB |
| Peaking | 760 Hz  | 0.41 | 29.7 dB  |
| Peaking | 1279 Hz | 0.71 | -13.8 dB |
| Peaking | 7840 Hz | 2.59 | -8.3 dB  |
| Peaking | 329 Hz  | 6.61 | -0.3 dB  |
| Peaking | 1916 Hz | 4.44 | 3.0 dB   |
| Peaking | 2984 Hz | 1.29 | -3.4 dB  |
| Peaking | 3409 Hz | 3.38 | 4.1 dB   |
| Peaking | 5297 Hz | 6.59 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t402v%20OverEar%20Blue/Torque%20t402v%20OverEar%20Blue.png)