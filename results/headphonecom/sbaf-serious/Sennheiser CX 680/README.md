# Sennheiser CX 680

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 0.0; 23 1.8; 25 1.5; 28 1.0; 31 0.6; 34 0.3; 37 -0.0; 41 -0.4; 45 -0.7; 49 -1.0; 54 -1.5; 60 -1.9; 66 -2.4; 72 -2.8; 79 -3.2; 87 -3.7; 96 -4.1; 106 -4.5; 116 -4.9; 128 -5.3; 141 -5.8; 155 -6.0; 170 -6.4; 187 -6.6; 206 -6.6; 227 -6.7; 249 -6.7; 274 -6.5; 302 -6.1; 332 -5.6; 365 -5.0; 402 -4.5; 442 -3.9; 486 -3.3; 535 -2.5; 588 -1.9; 647 -1.0; 712 0.2; 783 0.4; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.0; 1526 -2.9; 1678 -3.5; 1846 -4.0; 2031 -4.3; 2234 -4.5; 2457 -4.2; 2703 -3.0; 2973 -0.9; 3270 1.6; 3597 3.0; 3957 1.8; 4353 -1.4; 4788 -5.0; 5267 -5.9; 5793 -0.8; 6373 3.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -0.7; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.2dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 198 Hz  | 0.61 | -7.1 dB |
| Peaking | 2204 Hz | 1.77 | -5.1 dB |
| Peaking | 3631 Hz | 3.18 | 5.4 dB  |
| Peaking | 5068 Hz | 3.48 | -7.7 dB |
| Peaking | 6434 Hz | 4.84 | 5.9 dB  |
| Peaking | 22 Hz   | 1.71 | 2.5 dB  |
| Peaking | 419 Hz  | 1.59 | -1.1 dB |
| Peaking | 802 Hz  | 1.87 | 2.2 dB  |
| Peaking | 1565 Hz | 4.42 | -1.2 dB |
| Peaking | 9783 Hz | 9.57 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20680/Sennheiser%20CX%20680.png)