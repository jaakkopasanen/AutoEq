# Westone W2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.7; 28 2.6; 31 2.5; 34 2.4; 37 2.3; 41 2.1; 45 1.9; 49 1.8; 54 1.6; 60 1.3; 66 0.9; 72 0.5; 79 0.2; 87 -0.3; 96 -0.7; 106 -1.0; 116 -1.2; 128 -1.6; 141 -1.8; 155 -2.1; 170 -2.3; 187 -2.4; 206 -2.4; 227 -2.4; 249 -2.3; 274 -2.3; 302 -2.2; 332 -2.0; 365 -1.8; 402 -1.6; 442 -1.3; 486 -1.0; 535 -0.7; 588 -0.1; 647 0.2; 712 0.3; 783 0.7; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.3; 1261 -0.6; 1387 -1.2; 1526 -1.7; 1678 -2.1; 1846 -2.1; 2031 -1.8; 2234 -1.2; 2457 0.6; 2703 2.8; 2973 5.8; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.8; 5267 5.7; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.73 | 2.8 dB  |
| Peaking | 54 Hz   | 1.51 | 1.0 dB  |
| Peaking | 208 Hz  | 0.73 | -2.7 dB |
| Peaking | 1990 Hz | 1.72 | -5.2 dB |
| Peaking | 3760 Hz | 0.9  | 7.6 dB  |
| Peaking | 775 Hz  | 2.14 | 1.3 dB  |
| Peaking | 1968 Hz | 0.14 | -0.4 dB |
| Peaking | 2991 Hz | 8.74 | 1.9 dB  |
| Peaking | 6272 Hz | 2.81 | 6.0 dB  |
| Peaking | 7012 Hz | 1.42 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W2/Westone%20W2.png)