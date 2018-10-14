# Polk Audio UltraFit 1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.5; 54 4.4; 60 3.6; 66 2.6; 72 1.6; 79 1.1; 87 0.2; 96 -0.8; 106 -1.1; 116 -1.8; 128 -2.2; 141 -3.2; 155 -3.2; 170 -3.7; 187 -3.9; 206 -4.3; 227 -4.6; 249 -4.6; 274 -4.5; 302 -5.3; 332 -4.8; 365 -5.2; 402 -5.5; 442 -4.7; 486 -4.6; 535 -5.3; 588 -4.8; 647 -5.3; 712 -4.7; 783 -3.8; 861 -2.1; 947 1.1; 1042 0.8; 1146 3.0; 1261 3.0; 1387 2.7; 1526 3.0; 1678 4.5; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Audio UltraFit 1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.54 | 7.1 dB  |
| Peaking | 268 Hz  | 0.39 | -5.5 dB |
| Peaking | 674 Hz  | 2.25 | -3.6 dB |
| Peaking | 2205 Hz | 0.62 | 6.6 dB  |
| Peaking | 5260 Hz | 2.15 | 4.1 dB  |
| Peaking | 1165 Hz | 5.96 | 1.5 dB  |
| Peaking | 1479 Hz | 6.13 | -1.4 dB |
| Peaking | 3894 Hz | 2.61 | 1.3 dB  |
| Peaking | 6393 Hz | 3.89 | 4.7 dB  |
| Peaking | 6855 Hz | 1.35 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Audio%20UltraFit%201000/Polk%20Audio%20UltraFit%201000.png)