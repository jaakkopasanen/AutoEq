# Sennheiser HD 238

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 21 0.0; 23 2.5; 25 2.0; 28 1.3; 31 0.8; 34 0.4; 37 -0.0; 41 -0.5; 45 -0.8; 49 -1.1; 54 -1.4; 60 -1.7; 66 -2.1; 72 -2.5; 79 -2.7; 87 -3.1; 96 -3.7; 106 -4.0; 116 -4.1; 128 -4.4; 141 -4.4; 155 -4.4; 170 -4.4; 187 -4.3; 206 -4.2; 227 -3.9; 249 -3.6; 274 -3.4; 302 -3.1; 332 -2.8; 365 -2.4; 402 -2.0; 442 -1.6; 486 -1.4; 535 -1.1; 588 -0.7; 647 -0.5; 712 -0.4; 783 0.0; 861 -0.1; 947 -0.0; 1042 0.5; 1146 0.7; 1261 -0.1; 1387 -0.7; 1526 -1.1; 1678 -1.2; 1846 -0.7; 2031 0.4; 2234 1.8; 2457 3.2; 2703 1.3; 2973 -0.9; 3270 -3.2; 3597 0.4; 3957 2.6; 4353 -3.2; 4788 -3.0; 5267 -0.4; 5793 -0.5; 6373 -1.2; 7010 0.5; 7711 0.3; 8482 -2.3; 9330 -3.5; 10263 -0.7; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 238 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.26 | 3.7 dB  |
| Peaking | 151 Hz  | 0.54 | -4.6 dB |
| Peaking | 2453 Hz | 6.25 | 3.6 dB  |
| Peaking | 3206 Hz | 9.51 | -3.8 dB |
| Peaking | 9157 Hz | 5.92 | -4.0 dB |
| Peaking | 1100 Hz | 2.55 | 1.1 dB  |
| Peaking | 1576 Hz | 3.33 | -1.5 dB |
| Peaking | 3930 Hz | 8.97 | 4.7 dB  |
| Peaking | 4536 Hz | 5.6  | -4.6 dB |
| Peaking | 7472 Hz | 9.79 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20238/Sennheiser%20HD%20238.png)