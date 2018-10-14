# Sennheiser PX 100 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.6; 25 5.1; 28 4.3; 31 3.5; 34 2.9; 37 2.3; 41 1.7; 45 1.2; 49 0.7; 54 0.1; 60 -0.4; 66 -0.9; 72 -1.4; 79 -1.8; 87 -2.3; 96 -2.4; 106 -2.5; 116 -2.9; 128 -3.1; 141 -3.5; 155 -3.5; 170 -3.6; 187 -3.5; 206 -3.4; 227 -3.2; 249 -3.0; 274 -2.6; 302 -2.1; 332 -1.9; 365 -1.5; 402 -1.0; 442 -0.9; 486 -0.8; 535 -0.4; 588 -0.2; 647 0.1; 712 0.3; 783 0.2; 861 0.3; 947 0.1; 1042 -0.1; 1146 -0.3; 1261 -0.5; 1387 -1.2; 1526 -2.0; 1678 -2.8; 1846 -3.0; 2031 -2.3; 2234 -0.3; 2457 2.6; 2703 4.1; 2973 4.1; 3270 2.1; 3597 3.9; 3957 2.7; 4353 -2.9; 4788 -0.8; 5267 4.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -1.2; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 100 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.01 | 6.0 dB  |
| Peaking | 154 Hz  | 0.66 | -3.8 dB |
| Peaking | 1867 Hz | 2.55 | -4.2 dB |
| Peaking | 2787 Hz | 2.63 | 5.2 dB  |
| Peaking | 5983 Hz | 4.65 | 6.8 dB  |
| Peaking | 758 Hz  | 2.15 | 0.8 dB  |
| Peaking | 3810 Hz | 7.22 | 4.4 dB  |
| Peaking | 4468 Hz | 4.8  | -5.6 dB |
| Peaking | 5275 Hz | 7.37 | 3.2 dB  |
| Peaking | 9204 Hz | 6.48 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20100%20II/Sennheiser%20PX%20100%20II.png)