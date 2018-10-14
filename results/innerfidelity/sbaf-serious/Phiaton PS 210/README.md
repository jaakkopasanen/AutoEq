# Phiaton PS 210

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.8; 25 5.5; 28 4.9; 31 4.3; 34 3.9; 37 3.5; 41 3.0; 45 2.5; 49 2.1; 54 1.6; 60 1.1; 66 0.6; 72 0.1; 79 -0.4; 87 -0.9; 96 -1.5; 106 -1.7; 116 -2.0; 128 -2.5; 141 -2.9; 155 -3.1; 170 -3.3; 187 -3.3; 206 -3.5; 227 -3.6; 249 -3.6; 274 -3.6; 302 -3.6; 332 -3.5; 365 -3.3; 402 -3.5; 442 -4.0; 486 -3.4; 535 -3.2; 588 -3.1; 647 -3.0; 712 -2.6; 783 -1.8; 861 -1.0; 947 -0.4; 1042 0.2; 1146 0.7; 1261 0.7; 1387 0.2; 1526 -0.9; 1678 -2.1; 1846 -3.4; 2031 -4.6; 2234 -5.4; 2457 -3.4; 2703 -0.2; 2973 3.4; 3270 5.6; 3597 5.9; 3957 3.7; 4353 -0.3; 4788 0.2; 5267 0.7; 5793 4.3; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 18 Hz   | 0.47 | 6.2 dB   |
| Peaking | 399 Hz  | 0.26 | -4.8 dB  |
| Peaking | 1946 Hz | 0.48 | 6.6 dB   |
| Peaking | 2165 Hz | 1.68 | -10.8 dB |
| Peaking | 3308 Hz | 4.12 | 5.7 dB   |
| Peaking | 665 Hz  | 5.69 | -0.8 dB  |
| Peaking | 3854 Hz | 5.34 | 2.8 dB   |
| Peaking | 4445 Hz | 3.96 | -4.0 dB  |
| Peaking | 6292 Hz | 4.33 | 6.2 dB   |
| Peaking | 7369 Hz | 1.38 | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20210/Phiaton%20PS%20210.png)