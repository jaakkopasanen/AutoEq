# Shure SE420

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 5.0; 25 4.7; 28 4.4; 31 4.1; 34 3.8; 37 3.5; 41 3.2; 45 2.9; 49 2.6; 54 2.2; 60 1.8; 66 1.3; 72 1.0; 79 0.5; 87 0.2; 96 -0.1; 106 -0.6; 116 -0.9; 128 -1.2; 141 -1.5; 155 -1.7; 170 -1.9; 187 -2.0; 206 -2.1; 227 -2.1; 249 -2.2; 274 -2.0; 302 -1.8; 332 -1.7; 365 -1.4; 402 -1.2; 442 -1.1; 486 -0.8; 535 -0.6; 588 -0.1; 647 0.1; 712 0.3; 783 0.4; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.5; 1261 -0.8; 1387 -1.3; 1526 -1.9; 1678 -2.2; 1846 -2.3; 2031 -2.5; 2234 -2.6; 2457 -2.0; 2703 -0.7; 2973 1.1; 3270 3.1; 3597 4.7; 3957 4.9; 4353 4.7; 4788 5.7; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.77 | 5.0 dB  |
| Peaking | 45 Hz   | 1.16 | 1.4 dB  |
| Peaking | 209 Hz  | 0.82 | -2.4 dB |
| Peaking | 2105 Hz | 1.73 | -4.0 dB |
| Peaking | 4702 Hz | 1.28 | 6.6 dB  |
| Peaking | 809 Hz  | 2.77 | 1.0 dB  |
| Peaking | 3518 Hz | 3.94 | 2.6 dB  |
| Peaking | 5551 Hz | 0.86 | -2.9 dB |
| Peaking | 6206 Hz | 2.33 | 5.4 dB  |
| Peaking | 7684 Hz | 2.86 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE420/Shure%20SE420.png)