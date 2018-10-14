# Master Dynamic ME05

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.5dB
GraphicEQ: 21 -5.7; 23 -6.1; 25 -6.4; 28 -6.8; 31 -7.2; 34 -7.5; 37 -7.7; 41 -8.0; 45 -8.1; 49 -8.3; 54 -8.4; 60 -8.5; 66 -8.7; 72 -8.7; 79 -8.9; 87 -9.0; 96 -9.0; 106 -8.9; 116 -8.7; 128 -8.5; 141 -8.3; 155 -8.0; 170 -7.7; 187 -7.3; 206 -6.9; 227 -6.2; 249 -5.8; 274 -5.3; 302 -4.7; 332 -4.1; 365 -3.5; 402 -3.0; 442 -2.2; 486 -1.8; 535 -1.3; 588 -0.5; 647 -0.2; 712 0.1; 783 0.5; 861 0.4; 947 0.2; 1042 -0.3; 1146 -0.6; 1261 -0.7; 1387 -1.4; 1526 -2.1; 1678 -2.7; 1846 -3.0; 2031 -3.1; 2234 -3.5; 2457 -3.4; 2703 -3.6; 2973 -2.7; 3270 -0.9; 3597 0.0; 3957 -1.0; 4353 -3.9; 4788 -5.8; 5267 -4.8; 5793 -1.8; 6373 0.4; 7010 1.4; 7711 0.3; 8482 -1.2; 9330 -1.0; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.5dB` and instead set Global volume in the UI for both channels to **-14**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic ME05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.38 | -7.2 dB |
| Peaking | 131 Hz  | 0.78 | -4.7 dB |
| Peaking | 262 Hz  | 1.37 | -2.5 dB |
| Peaking | 2217 Hz | 1.78 | -3.7 dB |
| Peaking | 4903 Hz | 5.02 | -6.2 dB |
| Peaking | 804 Hz  | 1.68 | 1.7 dB  |
| Peaking | 1633 Hz | 0.21 | -0.6 dB |
| Peaking | 3571 Hz | 7.15 | 2.2 dB  |
| Peaking | 6944 Hz | 5.04 | 2.4 dB  |
| Peaking | 8825 Hz | 7.27 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20ME05/Master%20Dynamic%20ME05.png)