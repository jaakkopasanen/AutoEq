# Grado RS1e Flat Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.7; 66 4.1; 72 2.4; 79 0.9; 87 -0.5; 96 -1.4; 106 -1.7; 116 -1.7; 128 -1.7; 141 -1.5; 155 -1.3; 170 -1.1; 187 -0.7; 206 -0.5; 227 0.1; 249 0.1; 274 0.3; 302 0.1; 332 0.4; 365 0.6; 402 0.7; 442 1.0; 486 1.0; 535 1.0; 588 1.3; 647 1.3; 712 1.1; 783 1.1; 861 0.7; 947 0.3; 1042 0.1; 1146 -0.2; 1261 -0.4; 1387 -0.7; 1526 0.9; 1678 0.2; 1846 -6.2; 2031 -5.5; 2234 -2.1; 2457 1.8; 2703 4.8; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.4  | 9.0 dB  |
| Peaking | 103 Hz  | 0.86 | -8.1 dB |
| Peaking | 567 Hz  | 1.81 | 1.1 dB  |
| Peaking | 1963 Hz | 4.26 | -9.7 dB |
| Peaking | 3827 Hz | 0.91 | 7.2 dB  |
| Peaking | 1342 Hz | 3.36 | -1.6 dB |
| Peaking | 1633 Hz | 6.2  | 3.9 dB  |
| Peaking | 1787 Hz | 9.73 | -2.5 dB |
| Peaking | 6251 Hz | 2.72 | 5.8 dB  |
| Peaking | 7111 Hz | 1.38 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Flat%20Pads/Grado%20RS1e%20Flat%20Pads.png)