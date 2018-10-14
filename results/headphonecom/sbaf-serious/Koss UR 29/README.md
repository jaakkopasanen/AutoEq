# Koss UR 29

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 5.5; 87 4.8; 96 4.3; 106 3.8; 116 3.5; 128 3.3; 141 2.8; 155 2.7; 170 2.8; 187 2.7; 206 2.5; 227 2.2; 249 1.9; 274 1.8; 302 1.9; 332 2.1; 365 2.3; 402 2.2; 442 2.3; 486 2.1; 535 1.7; 588 1.1; 647 0.2; 712 0.2; 783 0.4; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.7; 1261 0.9; 1387 0.6; 1526 0.3; 1678 -0.5; 1846 -2.1; 2031 -2.3; 2234 -1.9; 2457 0.3; 2703 2.7; 2973 4.5; 3270 5.6; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -1.8; 9330 -2.2; 10263 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss UR 29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.2  | 4.9 dB  |
| Peaking | 70 Hz   | 0.41 | 2.4 dB  |
| Peaking | 407 Hz  | 1.72 | 1.8 dB  |
| Peaking | 2071 Hz | 3.18 | -4.8 dB |
| Peaking | 4123 Hz | 1.13 | 7.1 dB  |
| Peaking | 896 Hz  | 5.87 | -0.8 dB |
| Peaking | 3114 Hz | 5.24 | 1.1 dB  |
| Peaking | 4151 Hz | 3.82 | -1.2 dB |
| Peaking | 6116 Hz | 3.95 | 3.0 dB  |
| Peaking | 8782 Hz | 3.62 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Koss%20UR%2029/Koss%20UR%2029.png)