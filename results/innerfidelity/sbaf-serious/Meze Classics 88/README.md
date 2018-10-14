# Meze Classics 88

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.4; 25 4.2; 28 4.0; 31 3.8; 34 3.7; 37 3.5; 41 3.4; 45 3.3; 49 3.2; 54 3.1; 60 3.0; 66 2.9; 72 2.8; 79 2.5; 87 1.9; 96 1.3; 106 1.3; 116 1.0; 128 0.5; 141 0.3; 155 0.1; 170 0.3; 187 0.0; 206 0.0; 227 0.2; 249 0.7; 274 1.1; 302 1.2; 332 1.2; 365 1.6; 402 2.1; 442 3.3; 486 4.7; 535 6.0; 588 6.0; 647 5.0; 712 3.3; 783 2.2; 861 1.0; 947 0.0; 1042 0.5; 1146 -1.1; 1261 -1.8; 1387 -1.9; 1526 -1.2; 1678 0.3; 1846 2.6; 2031 4.6; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze Classics 88 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.65 | 4.3 dB  |
| Peaking | 66 Hz   | 1.58 | 1.9 dB  |
| Peaking | 563 Hz  | 2.13 | 6.1 dB  |
| Peaking | 1373 Hz | 1.87 | -5.6 dB |
| Peaking | 3114 Hz | 0.63 | 7.2 dB  |
| Peaking | 1670 Hz | 6.77 | -0.8 dB |
| Peaking | 2171 Hz | 3.79 | 1.5 dB  |
| Peaking | 3181 Hz | 2.23 | -1.1 dB |
| Peaking | 6224 Hz | 2.05 | 5.7 dB  |
| Peaking | 7436 Hz | 1.42 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%20Classics%2088/Meze%20Classics%2088.png)