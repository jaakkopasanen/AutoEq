# Sennheiser PMX 680

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 21 -3.7; 23 -4.1; 25 -4.4; 28 -4.8; 31 -5.2; 34 -5.5; 37 -5.7; 41 -5.9; 45 -6.1; 49 -6.3; 54 -6.5; 60 -6.7; 66 -6.8; 72 -7.0; 79 -7.0; 87 -7.0; 96 -7.0; 106 -6.9; 116 -7.0; 128 -6.9; 141 -7.1; 155 -7.1; 170 -7.3; 187 -7.2; 206 -7.1; 227 -7.1; 249 -6.9; 274 -6.7; 302 -6.3; 332 -5.7; 365 -5.1; 402 -4.5; 442 -4.0; 486 -3.3; 535 -2.6; 588 -1.9; 647 -1.0; 712 0.2; 783 0.4; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.2; 1387 -2.0; 1526 -2.9; 1678 -3.5; 1846 -4.0; 2031 -4.3; 2234 -4.5; 2457 -4.2; 2703 -3.0; 2973 -0.9; 3270 1.6; 3597 3.0; 3957 1.8; 4353 -1.4; 4788 -5.0; 5267 -5.9; 5793 -0.8; 6373 3.3; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -1.0; 10263 -0.7; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.2dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PMX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 68 Hz   | 0.33 | -6.7 dB  |
| Peaking | 261 Hz  | 0.98 | -4.2 dB  |
| Peaking | 2317 Hz | 1.46 | -8.0 dB  |
| Peaking | 3848 Hz | 0.87 | 6.7 dB   |
| Peaking | 4967 Hz | 4.09 | -11.2 dB |
| Peaking | 494 Hz  | 1.9  | -1.1 dB  |
| Peaking | 789 Hz  | 1.77 | 2.0 dB   |
| Peaking | 1559 Hz | 4.32 | -1.2 dB  |
| Peaking | 6616 Hz | 6.29 | 4.6 dB   |
| Peaking | 8402 Hz | 1.16 | -1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PMX%20680/Sennheiser%20PMX%20680.png)