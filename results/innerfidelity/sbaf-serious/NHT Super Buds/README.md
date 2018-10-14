# NHT Super Buds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -10.2; 23 -10.3; 25 -10.4; 28 -10.3; 31 -10.2; 34 -10.1; 37 -10.1; 41 -9.9; 45 -9.8; 49 -9.6; 54 -9.5; 60 -9.4; 66 -9.3; 72 -9.2; 79 -9.0; 87 -9.0; 96 -8.9; 106 -8.6; 116 -8.2; 128 -8.0; 141 -7.7; 155 -7.3; 170 -6.8; 187 -6.4; 206 -5.9; 227 -5.3; 249 -4.7; 274 -4.1; 302 -3.5; 332 -2.9; 365 -2.3; 402 -1.8; 442 -1.1; 486 -0.7; 535 -0.2; 588 0.5; 647 0.5; 712 0.7; 783 0.9; 861 0.7; 947 0.3; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -2.2; 1526 -3.2; 1678 -4.0; 1846 -4.3; 2031 -4.2; 2234 -3.8; 2457 -2.7; 2703 -1.6; 2973 0.4; 3270 2.7; 3597 5.5; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NHT Super Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.1  | -10.0 dB |
| Peaking | 717 Hz  | 0.66 | 3.0 dB   |
| Peaking | 2017 Hz | 1.04 | -6.7 dB  |
| Peaking | 4357 Hz | 1.23 | 8.4 dB   |
| Peaking | 3628 Hz | 6.2  | 1.9 dB   |
| Peaking | 4436 Hz | 2.59 | -1.2 dB  |
| Peaking | 6327 Hz | 2.65 | 4.2 dB   |
| Peaking | 7528 Hz | 3.19 | -2.3 dB  |
| Peaking | 7537 Hz | 0.8  | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NHT%20Super%20Buds/NHT%20Super%20Buds.png)