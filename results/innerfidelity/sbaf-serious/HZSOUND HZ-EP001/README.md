# HZSOUND HZ-EP001

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.6; 23 -2.6; 25 -2.6; 28 -2.6; 31 -2.6; 34 -2.6; 37 -2.5; 41 -2.5; 45 -2.5; 49 -2.6; 54 -2.5; 60 -2.6; 66 -2.8; 72 -2.9; 79 -3.1; 87 -3.3; 96 -3.5; 106 -3.7; 116 -3.7; 128 -3.9; 141 -4.0; 155 -4.1; 170 -4.1; 187 -4.1; 206 -4.1; 227 -4.0; 249 -3.9; 274 -3.8; 302 -3.7; 332 -3.6; 365 -3.8; 402 -3.4; 442 -0.9; 486 -1.7; 535 -1.6; 588 -1.0; 647 -0.8; 712 -0.4; 783 -0.1; 861 -0.0; 947 -0.0; 1042 0.0; 1146 0.1; 1261 0.2; 1387 0.1; 1526 -0.0; 1678 0.1; 1846 0.7; 2031 1.3; 2234 1.8; 2457 2.9; 2703 3.0; 2973 3.2; 3270 3.4; 3597 1.6; 3957 0.7; 4353 0.9; 4788 3.1; 5267 5.9; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ-EP001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.13 | -2.4 dB |
| Peaking | 195 Hz  | 0.71 | -3.1 dB |
| Peaking | 360 Hz  | 3.83 | -1.9 dB |
| Peaking | 2774 Hz | 2.31 | 3.3 dB  |
| Peaking | 5760 Hz | 3.25 | 6.6 dB  |
| Peaking | 863 Hz  | 3.15 | 0.4 dB  |
| Peaking | 1599 Hz | 6.79 | -0.4 dB |
| Peaking | 4160 Hz | 5.87 | -3.2 dB |
| Peaking | 4276 Hz | 1.97 | 1.5 dB  |
| Peaking | 8220 Hz | 3.69 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ-EP001/HZSOUND%20HZ-EP001.png)