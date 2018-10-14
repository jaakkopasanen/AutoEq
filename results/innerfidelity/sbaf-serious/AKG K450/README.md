# AKG K450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 5.9; 34 5.5; 37 5.0; 41 4.5; 45 4.1; 49 3.7; 54 3.3; 60 3.0; 66 2.7; 72 2.4; 79 2.1; 87 1.8; 96 1.4; 106 1.1; 116 0.8; 128 0.5; 141 0.0; 155 -0.2; 170 -0.3; 187 -0.5; 206 -0.6; 227 -0.7; 249 -0.9; 274 -0.7; 302 -0.8; 332 -0.9; 365 -0.8; 402 -0.4; 442 -0.5; 486 -0.8; 535 -1.0; 588 -0.5; 647 -0.3; 712 -0.1; 783 -0.0; 861 -0.0; 947 0.4; 1042 0.8; 1146 1.0; 1261 2.0; 1387 2.9; 1526 3.9; 1678 4.9; 1846 5.6; 2031 6.0; 2234 6.0; 2457 6.0; 2703 5.5; 2973 3.5; 3270 1.2; 3597 0.1; 3957 1.4; 4353 2.8; 4788 5.7; 5267 6.0; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.36 | 6.2 dB  |
| Peaking | 1391 Hz | 0.09 | -1.5 dB |
| Peaking | 2227 Hz | 0.93 | 7.9 dB  |
| Peaking | 3542 Hz | 3.27 | -4.2 dB |
| Peaking | 5506 Hz | 2.07 | 6.6 dB  |
| Peaking | 1110 Hz | 7.13 | -0.5 dB |
| Peaking | 5709 Hz | 6.78 | -2.3 dB |
| Peaking | 6462 Hz | 2.69 | 2.8 dB  |
| Peaking | 7490 Hz | 3.54 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K450/AKG%20K450.png)