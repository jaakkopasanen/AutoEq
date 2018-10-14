# Koss Pro4AA 1975

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 5.5; 66 4.2; 72 3.0; 79 1.8; 87 0.7; 96 -0.1; 106 -0.9; 116 -1.7; 128 -2.6; 141 -3.2; 155 -3.9; 170 -4.0; 187 -4.5; 206 -5.4; 227 -6.3; 249 -7.2; 274 -8.0; 302 -8.9; 332 -9.1; 365 -8.5; 402 -7.3; 442 -5.2; 486 -2.9; 535 -1.7; 588 -0.3; 647 1.8; 712 2.7; 783 3.2; 861 2.1; 947 0.9; 1042 -0.2; 1146 -0.8; 1261 -2.0; 1387 -3.4; 1526 -5.0; 1678 -6.2; 1846 -6.7; 2031 -6.6; 2234 -6.3; 2457 -4.9; 2703 -4.2; 2973 -2.6; 3270 -0.4; 3597 2.4; 3957 5.6; 4353 5.5; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss Pro4AA 1975 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.54 | 7.5 dB   |
| Peaking | 362 Hz  | 0.56 | -17.2 dB |
| Peaking | 703 Hz  | 0.54 | 15.9 dB  |
| Peaking | 1972 Hz | 0.63 | -12.3 dB |
| Peaking | 4604 Hz | 1.26 | 10.7 dB  |
| Peaking | 123 Hz  | 3.61 | -0.6 dB  |
| Peaking | 2213 Hz | 0.26 | 0.3 dB   |
| Peaking | 4770 Hz | 7.29 | -1.4 dB  |
| Peaking | 6396 Hz | 3.46 | 3.6 dB   |
| Peaking | 7564 Hz | 1.99 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20Pro4AA%201975/Koss%20Pro4AA%201975.png)