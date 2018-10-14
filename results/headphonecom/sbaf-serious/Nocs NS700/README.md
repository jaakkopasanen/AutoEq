# Nocs NS700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 21 0.0; 23 0.6; 25 0.1; 28 -0.5; 31 -1.0; 34 -1.4; 37 -1.7; 41 -1.9; 45 -2.0; 49 -2.1; 54 -2.4; 60 -2.7; 66 -3.0; 72 -3.3; 79 -3.3; 87 -2.9; 96 -1.3; 106 -1.5; 116 -2.4; 128 -2.7; 141 -2.6; 155 -2.1; 170 -1.4; 187 -0.9; 206 0.2; 227 1.1; 249 2.2; 274 3.3; 302 2.5; 332 -1.9; 365 -1.6; 402 -1.0; 442 -0.9; 486 -0.8; 535 -0.6; 588 -0.4; 647 -0.1; 712 -0.2; 783 -0.2; 861 -0.1; 947 -0.1; 1042 0.0; 1146 -0.0; 1261 0.1; 1387 0.2; 1526 -0.5; 1678 0.6; 1846 0.8; 2031 0.8; 2234 0.7; 2457 0.5; 2703 -0.1; 2973 -1.4; 3270 -1.3; 3597 -1.2; 3957 1.4; 4353 3.9; 4788 2.7; 5267 0.2; 5793 2.2; 6373 1.6; 7010 -4.8; 7711 -2.4; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 89 Hz   |  0.47 | -2.8 dB |
| Peaking | 286 Hz  |  2.45 | 7.3 dB  |
| Peaking | 337 Hz  |  2.88 | -5.4 dB |
| Peaking | 4504 Hz |  6.56 | 4.7 dB  |
| Peaking | 7144 Hz |  9.68 | -5.5 dB |
| Peaking | 18 Hz   |  2.03 | 1.8 dB  |
| Peaking | 139 Hz  |  6.31 | -0.7 dB |
| Peaking | 2120 Hz |  2.65 | 1.1 dB  |
| Peaking | 3198 Hz |  4.05 | -2.1 dB |
| Peaking | 6061 Hz | 11.7  | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS700/Nocs%20NS700.png)