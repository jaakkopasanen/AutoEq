# Sennheiser PX 360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.5; 87 4.9; 96 4.3; 106 4.2; 116 5.0; 128 6.0; 141 4.8; 155 4.4; 170 5.8; 187 5.9; 206 5.0; 227 4.0; 249 4.0; 274 2.4; 302 0.3; 332 -0.4; 365 -0.5; 402 -1.4; 442 -1.6; 486 -1.0; 535 -0.2; 588 0.4; 647 0.5; 712 0.7; 783 0.8; 861 0.6; 947 0.3; 1042 -0.2; 1146 -1.3; 1261 -2.8; 1387 -5.2; 1526 -7.6; 1678 -9.3; 1846 -9.8; 2031 -8.7; 2234 -6.2; 2457 -3.1; 2703 -0.7; 2973 1.2; 3270 3.5; 3597 5.8; 3957 6.0; 4353 3.0; 4788 1.6; 5267 3.3; 5793 5.9; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.9; 10263 -2.9; 11289 -2.5; 12418 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.45 | 5.3 dB   |
| Peaking | 77 Hz    | 0.69 | 3.6 dB   |
| Peaking | 187 Hz   | 2.06 | 4.4 dB   |
| Peaking | 1870 Hz  | 1.94 | -12.2 dB |
| Peaking | 3844 Hz  | 1.12 | 6.4 dB   |
| Peaking | 417 Hz   | 2.95 | -2.4 dB  |
| Peaking | 835 Hz   | 2.1  | 1.8 dB   |
| Peaking | 4783 Hz  | 6.35 | -3.6 dB  |
| Peaking | 6035 Hz  | 4.33 | 4.5 dB   |
| Peaking | 10389 Hz | 3.16 | -3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PX%20360/Sennheiser%20PX%20360.png)