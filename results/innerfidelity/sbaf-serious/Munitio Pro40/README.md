# Munitio Pro40

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.4; 25 -0.4; 28 -1.5; 31 -2.4; 34 -3.1; 37 -3.7; 41 -4.2; 45 -4.6; 49 -4.8; 54 -5.0; 60 -5.0; 66 -5.1; 72 -5.2; 79 -5.3; 87 -5.8; 96 -6.2; 106 -6.5; 116 -6.6; 128 -6.8; 141 -7.1; 155 -7.2; 170 -7.0; 187 -7.2; 206 -7.3; 227 -7.2; 249 -7.2; 274 -6.9; 302 -6.2; 332 -5.0; 365 -4.2; 402 -3.4; 442 -2.6; 486 -1.2; 535 0.8; 588 3.5; 647 5.6; 712 5.7; 783 4.4; 861 2.1; 947 0.6; 1042 0.0; 1146 0.5; 1261 1.5; 1387 1.6; 1526 2.1; 1678 2.8; 1846 3.9; 2031 4.7; 2234 5.5; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.9; 3957 5.9; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Munitio Pro40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.63 | 4.1 dB  |
| Peaking | 38 Hz   | 0.95 | -3.2 dB |
| Peaking | 195 Hz  | 0.34 | -7.4 dB |
| Peaking | 659 Hz  | 2.24 | 9.2 dB  |
| Peaking | 3380 Hz | 0.7  | 6.9 dB  |
| Peaking | 1038 Hz | 6.04 | -1.4 dB |
| Peaking | 2245 Hz | 3.07 | 1.1 dB  |
| Peaking | 3452 Hz | 2.55 | -1.1 dB |
| Peaking | 6238 Hz | 2.17 | 5.3 dB  |
| Peaking | 7469 Hz | 1.47 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Munitio%20Pro40/Munitio%20Pro40.png)