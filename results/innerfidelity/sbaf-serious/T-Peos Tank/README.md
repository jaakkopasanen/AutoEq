# T-Peos Tank

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -10.0; 23 -9.9; 25 -9.8; 28 -9.7; 31 -9.7; 34 -9.6; 37 -9.5; 41 -9.3; 45 -9.2; 49 -9.1; 54 -9.0; 60 -8.9; 66 -8.8; 72 -8.8; 79 -8.7; 87 -8.6; 96 -8.6; 106 -8.3; 116 -8.0; 128 -7.8; 141 -7.5; 155 -7.2; 170 -6.7; 187 -6.2; 206 -5.8; 227 -5.2; 249 -4.7; 274 -4.1; 302 -3.5; 332 -3.0; 365 -2.3; 402 -1.8; 442 -1.2; 486 -0.8; 535 -0.3; 588 0.3; 647 0.7; 712 0.8; 783 1.0; 861 0.7; 947 0.3; 1042 -0.3; 1146 -0.7; 1261 -1.5; 1387 -2.7; 1526 -4.2; 1678 -5.4; 1846 -6.1; 2031 -6.3; 2234 -5.8; 2457 -3.4; 2703 -0.7; 2973 2.4; 3270 4.5; 3597 5.1; 3957 3.4; 4353 -0.7; 4788 -5.1; 5267 -9.2; 5793 -4.5; 6373 -0.2; 7010 0.6; 7711 -1.7; 8482 -4.8; 9330 -4.8; 10263 -1.8; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Tank ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 26 Hz   | 0.23 | -9.6 dB  |
| Peaking | 153 Hz  | 0.81 | -3.8 dB  |
| Peaking | 2005 Hz | 2.04 | -7.6 dB  |
| Peaking | 3495 Hz | 2.6  | 7.7 dB   |
| Peaking | 5195 Hz | 4.29 | -10.4 dB |
| Peaking | 300 Hz  | 2.01 | -0.8 dB  |
| Peaking | 745 Hz  | 1.38 | 1.9 dB   |
| Peaking | 1529 Hz | 4.96 | -1.5 dB  |
| Peaking | 6740 Hz | 4.81 | 3.0 dB   |
| Peaking | 8830 Hz | 3.91 | -5.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Tank/T-Peos%20Tank.png)