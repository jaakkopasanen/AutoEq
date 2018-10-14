# Nocs NS200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 21 -10.0; 23 -9.8; 25 -9.6; 28 -9.3; 31 -9.0; 34 -8.7; 37 -8.5; 41 -8.2; 45 -8.0; 49 -7.8; 54 -7.6; 60 -7.4; 66 -7.4; 72 -7.3; 79 -7.3; 87 -7.2; 96 -7.1; 106 -7.0; 116 -6.9; 128 -6.8; 141 -6.7; 155 -6.6; 170 -6.5; 187 -6.3; 206 -6.0; 227 -5.6; 249 -5.3; 274 -4.9; 302 -4.4; 332 -3.9; 365 -3.3; 402 -2.8; 442 -2.3; 486 -1.8; 535 -1.3; 588 -0.8; 647 -0.2; 712 0.2; 783 0.4; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.7; 1261 -1.3; 1387 -1.9; 1526 -2.6; 1678 -3.2; 1846 -3.6; 2031 -3.9; 2234 -4.2; 2457 -4.0; 2703 -3.2; 2973 -1.2; 3270 1.8; 3597 3.8; 3957 3.4; 4353 1.2; 4788 -0.5; 5267 -1.6; 5793 -3.1; 6373 -1.5; 7010 1.2; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.1dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.14 | -9.3 dB |
| Peaking | 199 Hz  | 0.81 | -4.0 dB |
| Peaking | 2262 Hz | 1.56 | -4.9 dB |
| Peaking | 3649 Hz | 3.4  | 5.8 dB  |
| Peaking | 5712 Hz | 5.87 | -3.5 dB |
| Peaking | 383 Hz  | 1.93 | -0.6 dB |
| Peaking | 801 Hz  | 1.73 | 1.5 dB  |
| Peaking | 1529 Hz | 3.58 | -1.0 dB |
| Peaking | 7067 Hz | 9.67 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS200/Nocs%20NS200.png)