# AirBuds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.8; 25 -2.3; 28 -2.5; 31 -2.6; 34 -3.1; 37 -3.6; 41 -4.1; 45 -4.4; 49 -4.9; 54 -5.3; 60 -5.9; 66 -6.4; 72 -6.9; 79 -7.4; 87 -7.9; 96 -8.4; 106 -8.8; 116 -9.0; 128 -9.4; 141 -9.6; 155 -9.8; 170 -9.9; 187 -9.9; 206 -9.8; 227 -9.6; 249 -9.5; 274 -9.2; 302 -8.8; 332 -8.4; 365 -7.9; 402 -7.4; 442 -6.6; 486 -6.1; 535 -5.4; 588 -4.4; 647 -3.6; 712 -2.9; 783 -1.8; 861 -1.0; 947 -0.4; 1042 0.2; 1146 2.9; 1261 3.4; 1387 5.4; 1526 6.0; 1678 5.8; 1846 3.1; 2031 1.9; 2234 3.1; 2457 5.5; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.7; 4353 1.9; 4788 -1.7; 5267 -4.5; 5793 -4.2; 6373 -0.6; 7010 2.2; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AirBuds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 87 Hz   | 0.46 | -4.7 dB |
| Peaking | 255 Hz  | 0.46 | -7.7 dB |
| Peaking | 1431 Hz | 2.2  | 6.1 dB  |
| Peaking | 3428 Hz | 1.19 | 7.1 dB  |
| Peaking | 5289 Hz | 3.58 | -8.5 dB |
| Peaking | 858 Hz  | 4.99 | 0.6 dB  |
| Peaking | 1700 Hz | 6.47 | 2.4 dB  |
| Peaking | 2029 Hz | 2.66 | -2.6 dB |
| Peaking | 2527 Hz | 4    | 2.3 dB  |
| Peaking | 3132 Hz | 4.52 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AirBuds/AirBuds.png)