# Shure SE535

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.1; 25 3.0; 28 2.9; 31 2.8; 34 2.7; 37 2.6; 41 2.4; 45 2.3; 49 2.1; 54 1.9; 60 1.6; 66 1.3; 72 0.8; 79 0.5; 87 0.2; 96 -0.1; 106 -0.4; 116 -0.6; 128 -0.9; 141 -1.2; 155 -1.5; 170 -1.6; 187 -1.8; 206 -1.9; 227 -1.9; 249 -1.9; 274 -1.9; 302 -1.8; 332 -1.7; 365 -1.3; 402 -1.2; 442 -1.1; 486 -1.0; 535 -0.6; 588 -0.4; 647 -0.2; 712 0.0; 783 0.2; 861 0.2; 947 0.0; 1042 -0.2; 1146 -0.3; 1261 -0.4; 1387 -0.7; 1526 -1.1; 1678 -1.1; 1846 -1.0; 2031 -0.7; 2234 0.1; 2457 1.8; 2703 3.4; 2973 4.9; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.2; 9330 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.67 | 3.0 dB  |
| Peaking | 52 Hz   | 1.37 | 1.1 dB  |
| Peaking | 222 Hz  | 0.74 | -2.1 dB |
| Peaking | 1862 Hz | 1.86 | -3.0 dB |
| Peaking | 4049 Hz | 1    | 7.1 dB  |
| Peaking | 792 Hz  | 4.24 | 0.5 dB  |
| Peaking | 3147 Hz | 3.61 | 2.0 dB  |
| Peaking | 3752 Hz | 1.49 | -1.5 dB |
| Peaking | 6286 Hz | 2.47 | 5.1 dB  |
| Peaking | 7479 Hz | 1.6  | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE535/Shure%20SE535.png)