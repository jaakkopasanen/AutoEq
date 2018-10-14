# Audeo PFE 121 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.3; 25 0.2; 28 0.1; 31 -0.1; 34 -0.2; 37 -0.3; 41 -0.5; 45 -0.6; 49 -0.8; 54 -1.1; 60 -1.4; 66 -1.7; 72 -2.0; 79 -2.4; 87 -2.8; 96 -3.1; 106 -3.4; 116 -3.6; 128 -3.8; 141 -4.1; 155 -4.1; 170 -4.2; 187 -4.2; 206 -4.1; 227 -4.0; 249 -3.9; 274 -3.6; 302 -3.4; 332 -3.1; 365 -2.8; 402 -2.5; 442 -2.0; 486 -1.8; 535 -1.4; 588 -0.6; 647 -0.3; 712 -0.1; 783 0.3; 861 0.3; 947 0.0; 1042 -0.0; 1146 -0.1; 1261 -0.1; 1387 -0.3; 1526 -0.6; 1678 -0.5; 1846 0.3; 2031 1.0; 2234 2.2; 2457 3.5; 2703 3.0; 2973 3.4; 3270 4.3; 3597 5.2; 3957 5.5; 4353 5.0; 4788 5.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 -0.9; 8482 -4.2; 9330 -3.6; 10263 -2.0; 11289 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 131 Hz  | 0.75 | -3.3 dB |
| Peaking | 278 Hz  | 0.93 | -2.5 dB |
| Peaking | 3533 Hz | 1.43 | 3.8 dB  |
| Peaking | 6028 Hz | 1.48 | 6.4 dB  |
| Peaking | 8580 Hz | 2.54 | -7.3 dB |
| Peaking | 23 Hz   | 1.15 | 0.6 dB  |
| Peaking | 789 Hz  | 3.39 | 0.8 dB  |
| Peaking | 1622 Hz | 2.63 | -1.2 dB |
| Peaking | 2400 Hz | 7.13 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Black%20Filter/Audeo%20PFE%20121%20Black%20Filter.png)