# Stax SR-Alpha Pro Excellent

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.8; 54 4.1; 60 2.5; 66 1.0; 72 -1.2; 79 -3.1; 87 -3.3; 96 -3.2; 106 -2.9; 116 -2.1; 128 -1.5; 141 -1.0; 155 -0.7; 170 -0.4; 187 -0.1; 206 0.0; 227 0.3; 249 0.4; 274 0.6; 302 0.6; 332 0.7; 365 0.8; 402 0.8; 442 1.1; 486 1.0; 535 1.0; 588 1.1; 647 1.1; 712 0.8; 783 0.9; 861 0.6; 947 0.3; 1042 -0.1; 1146 -0.5; 1261 -1.1; 1387 -1.9; 1526 -2.6; 1678 -3.2; 1846 -3.0; 2031 -1.8; 2234 -1.3; 2457 -0.8; 2703 0.2; 2973 1.3; 3270 2.0; 3597 2.6; 3957 3.5; 4353 3.0; 4788 3.9; 5267 4.9; 5793 3.8; 6373 1.2; 7010 0.4; 7711 -1.1; 8482 -4.0; 9330 -4.8; 10263 -2.3; 11289 -0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Alpha Pro Excellent ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 61 Hz    | 0.3  | 18.6 dB  |
| Peaking | 86 Hz    | 0.57 | -20.6 dB |
| Peaking | 1742 Hz  | 2.06 | -3.9 dB  |
| Peaking | 4921 Hz  | 1.26 | 4.7 dB   |
| Peaking | 8939 Hz  | 3.07 | -6.2 dB  |
| Peaking | 680 Hz   | 2.37 | 0.6 dB   |
| Peaking | 4544 Hz  | 8.75 | -1.2 dB  |
| Peaking | 5508 Hz  | 4.64 | 1.4 dB   |
| Peaking | 6419 Hz  | 6.17 | -1.4 dB  |
| Peaking | 11334 Hz | 7.16 | 0.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Alpha%20Pro%20Excellent/Stax%20SR-Alpha%20Pro%20Excellent.png)