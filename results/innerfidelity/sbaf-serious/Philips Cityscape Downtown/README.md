# Philips Cityscape Downtown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.0; 25 5.0; 28 4.9; 31 4.9; 34 4.9; 37 5.0; 41 5.0; 45 5.0; 49 5.1; 54 5.1; 60 5.2; 66 5.2; 72 5.2; 79 5.2; 87 5.1; 96 4.9; 106 4.9; 116 5.0; 128 5.1; 141 4.9; 155 4.5; 170 4.8; 187 4.1; 206 3.9; 227 3.9; 249 3.7; 274 3.7; 302 3.6; 332 3.6; 365 3.6; 402 3.3; 442 2.9; 486 2.3; 535 1.8; 588 1.7; 647 1.3; 712 0.8; 783 0.6; 861 0.2; 947 -0.0; 1042 0.0; 1146 0.3; 1261 0.7; 1387 0.8; 1526 1.3; 1678 2.2; 1846 3.3; 2031 5.1; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 5.7; 4353 4.4; 4788 5.5; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Philips Cityscape Downtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.24 | 4.9 dB  |
| Peaking | 159 Hz  | 0.75 | 2.3 dB  |
| Peaking | 370 Hz  | 1.73 | 2.3 dB  |
| Peaking | 2842 Hz | 1.23 | 6.5 dB  |
| Peaking | 5599 Hz | 2.69 | 5.2 dB  |
| Peaking | 1137 Hz | 1.75 | -1.0 dB |
| Peaking | 2143 Hz | 5.02 | 1.9 dB  |
| Peaking | 2878 Hz | 3.21 | -1.0 dB |
| Peaking | 3850 Hz | 4.91 | 1.3 dB  |
| Peaking | 8392 Hz | 3.68 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Philips%20Cityscape%20Downtown/Philips%20Cityscape%20Downtown.png)