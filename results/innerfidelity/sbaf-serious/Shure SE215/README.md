# Shure SE215

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 21 -4.1; 23 -4.1; 25 -4.2; 28 -4.2; 31 -4.3; 34 -4.4; 37 -4.4; 41 -4.5; 45 -4.7; 49 -4.8; 54 -5.0; 60 -5.2; 66 -5.5; 72 -5.7; 79 -6.0; 87 -6.3; 96 -6.6; 106 -6.7; 116 -6.7; 128 -6.8; 141 -6.8; 155 -6.8; 170 -6.7; 187 -6.5; 206 -6.2; 227 -5.8; 249 -5.5; 274 -5.0; 302 -4.5; 332 -4.0; 365 -3.4; 402 -2.9; 442 -2.2; 486 -1.8; 535 -1.3; 588 -0.5; 647 -0.1; 712 0.2; 783 0.6; 861 0.5; 947 0.3; 1042 -0.1; 1146 -0.3; 1261 -0.8; 1387 -1.9; 1526 -2.9; 1678 -3.8; 1846 -4.4; 2031 -4.8; 2234 -4.8; 2457 -3.5; 2703 -1.3; 2973 1.8; 3270 3.8; 3597 4.2; 3957 1.9; 4353 -3.3; 4788 -7.9; 5267 -2.7; 5793 2.9; 6373 5.2; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 48 Hz   | 0.27 | -4.4 dB  |
| Peaking | 179 Hz  | 0.69 | -4.5 dB  |
| Peaking | 2202 Hz | 1.53 | -10.4 dB |
| Peaking | 3535 Hz | 0.78 | 8.8 dB   |
| Peaking | 4721 Hz | 4.9  | -14.4 dB |
| Peaking | 807 Hz  | 2.21 | 1.5 dB   |
| Peaking | 1556 Hz | 5.29 | -1.3 dB  |
| Peaking | 5221 Hz | 9.21 | -2.3 dB  |
| Peaking | 6398 Hz | 3.38 | 5.6 dB   |
| Peaking | 7549 Hz | 1.51 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE215/Shure%20SE215.png)