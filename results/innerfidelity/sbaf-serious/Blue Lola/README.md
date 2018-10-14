# Blue Lola

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.2; 23 -0.4; 25 -0.6; 28 -0.8; 31 -0.9; 34 -1.0; 37 -1.1; 41 -1.3; 45 -1.4; 49 -1.4; 54 -1.5; 60 -1.7; 66 -1.8; 72 -1.9; 79 -2.1; 87 -2.4; 96 -2.8; 106 -2.6; 116 -2.4; 128 -2.6; 141 -3.0; 155 -3.4; 170 -2.3; 187 -2.7; 206 -2.4; 227 -1.7; 249 -0.8; 274 0.1; 302 0.7; 332 0.8; 365 0.8; 402 0.5; 442 1.0; 486 1.7; 535 2.9; 588 2.1; 647 1.6; 712 1.0; 783 1.1; 861 0.7; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.4; 1387 -0.5; 1526 -1.0; 1678 -1.1; 1846 -0.6; 2031 0.2; 2234 0.8; 2457 1.9; 2703 2.4; 2973 3.0; 3270 3.4; 3597 5.9; 3957 6.0; 4353 2.3; 4788 1.8; 5267 5.4; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue Lola ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 82 Hz   | 0.71 | -2.1 dB |
| Peaking | 162 Hz  | 1.77 | -2.2 dB |
| Peaking | 535 Hz  | 2.02 | 2.6 dB  |
| Peaking | 3630 Hz | 3.1  | 5.6 dB  |
| Peaking | 5904 Hz | 3.78 | 6.3 dB  |
| Peaking | 311 Hz  | 5.61 | 1.2 dB  |
| Peaking | 1649 Hz | 2.24 | -1.6 dB |
| Peaking | 2642 Hz | 2.57 | 1.5 dB  |
| Peaking | 3300 Hz | 7.13 | -1.1 dB |
| Peaking | 8250 Hz | 4.67 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20Lola/Blue%20Lola.png)