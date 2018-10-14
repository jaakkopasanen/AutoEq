# TDK MT300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 -8.9; 23 -8.9; 25 -8.9; 28 -8.9; 31 -8.8; 34 -8.8; 37 -8.8; 41 -8.8; 45 -8.8; 49 -8.8; 54 -8.8; 60 -8.9; 66 -8.9; 72 -9.0; 79 -9.1; 87 -9.2; 96 -9.4; 106 -9.3; 116 -9.1; 128 -9.0; 141 -8.9; 155 -8.6; 170 -8.3; 187 -7.9; 206 -7.4; 227 -6.9; 249 -6.3; 274 -5.6; 302 -5.0; 332 -4.3; 365 -3.5; 402 -2.8; 442 -1.9; 486 -1.4; 535 -0.8; 588 -0.0; 647 0.3; 712 0.4; 783 0.7; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.4; 1261 -0.4; 1387 -0.6; 1526 -0.5; 1678 0.3; 1846 1.5; 2031 2.7; 2234 3.7; 2457 4.6; 2703 4.9; 2973 5.0; 3270 4.2; 3597 2.7; 3957 0.3; 4353 -3.7; 4788 -7.3; 5267 -3.6; 5793 2.0; 6373 5.3; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK MT300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 61 Hz   | 0.22 | -9.8 dB  |
| Peaking | 2910 Hz | 1.48 | 6.0 dB   |
| Peaking | 4825 Hz | 3.56 | -10.1 dB |
| Peaking | 6331 Hz | 3.89 | 7.3 dB   |
| Peaking | 7617 Hz | 2.15 | -1.0 dB  |
| Peaking | 17 Hz   | 1.26 | -2.2 dB  |
| Peaking | 52 Hz   | 0.93 | 1.4 dB   |
| Peaking | 197 Hz  | 0.78 | -1.3 dB  |
| Peaking | 642 Hz  | 1.08 | 2.1 dB   |
| Peaking | 1399 Hz | 2.63 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20MT300/TDK%20MT300.png)