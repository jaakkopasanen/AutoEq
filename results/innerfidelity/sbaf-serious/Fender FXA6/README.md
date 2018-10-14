# Fender FXA6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -5.2; 23 -5.2; 25 -5.1; 28 -5.1; 31 -5.0; 34 -5.0; 37 -4.9; 41 -4.9; 45 -4.9; 49 -4.9; 54 -4.9; 60 -5.0; 66 -5.2; 72 -5.3; 79 -5.5; 87 -5.8; 96 -6.0; 106 -6.1; 116 -6.1; 128 -6.2; 141 -6.2; 155 -6.2; 170 -6.0; 187 -5.8; 206 -5.6; 227 -5.2; 249 -5.0; 274 -4.5; 302 -4.1; 332 -3.6; 365 -3.1; 402 -2.6; 442 -1.9; 486 -1.6; 535 -1.1; 588 -0.4; 647 -0.0; 712 0.2; 783 0.6; 861 0.5; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.9; 1387 -1.9; 1526 -3.1; 1678 -4.5; 1846 -5.9; 2031 -6.8; 2234 -5.5; 2457 -2.1; 2703 0.7; 2973 3.3; 3270 4.3; 3597 2.8; 3957 1.2; 4353 2.0; 4788 4.3; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fender FXA6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.14 | -4.9 dB |
| Peaking | 181 Hz  | 0.74 | -4.1 dB |
| Peaking | 2010 Hz | 2.58 | -7.8 dB |
| Peaking | 3126 Hz | 3.54 | 5.2 dB  |
| Peaking | 5640 Hz | 2.78 | 6.8 dB  |
| Peaking | 361 Hz  | 2.16 | -0.8 dB |
| Peaking | 790 Hz  | 1.43 | 1.4 dB  |
| Peaking | 1564 Hz | 5.07 | -1.0 dB |
| Peaking | 6576 Hz | 7.42 | 2.3 dB  |
| Peaking | 7613 Hz | 2.17 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fender%20FXA6/Fender%20FXA6.png)