# Monoprice 8323

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 5.9; 49 5.1; 54 4.0; 60 3.1; 66 2.6; 72 2.3; 79 2.2; 87 2.1; 96 2.0; 106 2.0; 116 2.2; 128 2.0; 141 1.9; 155 1.6; 170 2.2; 187 1.8; 206 1.8; 227 1.8; 249 2.0; 274 2.4; 302 3.0; 332 3.3; 365 3.2; 402 2.8; 442 2.3; 486 1.6; 535 1.3; 588 1.2; 647 0.9; 712 0.5; 783 0.5; 861 0.2; 947 -0.0; 1042 0.2; 1146 0.3; 1261 -0.3; 1387 -0.3; 1526 -1.0; 1678 -1.0; 1846 0.1; 2031 1.5; 2234 3.1; 2457 5.4; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.4; 9330 -2.0; 10263 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice 8323 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.64 | 6.5 dB  |
| Peaking | 161 Hz  | 1.18 | 1.1 dB  |
| Peaking | 350 Hz  | 1.9  | 3.1 dB  |
| Peaking | 4385 Hz | 0.86 | 7.1 dB  |
| Peaking | 8847 Hz | 3.02 | -4.4 dB |
| Peaking | 1676 Hz | 2.14 | -3.3 dB |
| Peaking | 2204 Hz | 4.92 | -1.1 dB |
| Peaking | 2532 Hz | 1.86 | 4.2 dB  |
| Peaking | 4318 Hz | 0.86 | -1.7 dB |
| Peaking | 6106 Hz | 4.11 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%208323/Monoprice%208323.png)