# JBL J55i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -4.2; 23 -4.2; 25 -4.2; 28 -4.2; 31 -4.2; 34 -4.2; 37 -4.2; 41 -4.2; 45 -4.2; 49 -4.2; 54 -4.3; 60 -4.5; 66 -4.6; 72 -4.9; 79 -5.1; 87 -5.4; 96 -5.7; 106 -5.8; 116 -6.1; 128 -6.5; 141 -6.9; 155 -7.0; 170 -6.7; 187 -6.8; 206 -7.0; 227 -6.9; 249 -6.6; 274 -5.9; 302 -5.3; 332 -5.0; 365 -4.2; 402 -3.4; 442 -2.2; 486 -1.1; 535 0.3; 588 1.7; 647 2.0; 712 1.2; 783 0.6; 861 -0.2; 947 -0.4; 1042 0.4; 1146 1.4; 1261 1.9; 1387 0.6; 1526 -1.7; 1678 -0.2; 1846 5.8; 2031 3.0; 2234 0.5; 2457 3.8; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J55i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.23 | -3.8 dB |
| Peaking | 197 Hz  | 0.49 | -6.8 dB |
| Peaking | 608 Hz  | 2.14 | 4.3 dB  |
| Peaking | 3319 Hz | 1.2  | 6.2 dB  |
| Peaking | 5635 Hz | 2.86 | 4.5 dB  |
| Peaking | 1252 Hz | 5.71 | 2.1 dB  |
| Peaking | 1601 Hz | 4.24 | -6.3 dB |
| Peaking | 1877 Hz | 3.67 | 7.8 dB  |
| Peaking | 2170 Hz | 6.91 | -5.7 dB |
| Peaking | 8411 Hz | 3.68 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J55i/JBL%20J55i.png)