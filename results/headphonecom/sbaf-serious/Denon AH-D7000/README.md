# Denon AH-D7000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 21 0.0; 23 3.5; 25 2.5; 28 1.3; 31 0.5; 34 0.0; 37 -0.3; 41 -0.6; 45 -0.9; 49 -0.9; 54 -0.5; 60 -0.4; 66 -0.6; 72 -0.6; 79 -0.7; 87 -0.6; 96 -0.4; 106 -0.4; 116 -0.4; 128 -0.2; 141 -0.2; 155 -0.0; 170 0.5; 187 0.4; 206 0.8; 227 1.0; 249 1.3; 274 1.7; 302 2.1; 332 2.5; 365 3.0; 402 3.2; 442 2.7; 486 2.0; 535 1.4; 588 0.6; 647 0.1; 712 -0.2; 783 -0.7; 861 -0.2; 947 0.8; 1042 0.0; 1146 0.4; 1261 1.1; 1387 1.6; 1526 1.7; 1678 1.9; 1846 2.2; 2031 2.1; 2234 2.6; 2457 3.0; 2703 3.2; 2973 2.7; 3270 1.2; 3597 0.1; 3957 0.5; 4353 0.3; 4788 -0.8; 5267 1.5; 5793 1.9; 6373 -0.8; 7010 -1.3; 7711 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 3.24 | 5.4 dB  |
| Peaking | 373 Hz  | 1.95 | 3.3 dB  |
| Peaking | 2447 Hz | 1.29 | 3.3 dB  |
| Peaking | 5491 Hz | 1.68 | -3.0 dB |
| Peaking | 5527 Hz | 5.05 | 4.9 dB  |
| Peaking | 21 Hz   | 0.98 | 1.9 dB  |
| Peaking | 41 Hz   | 0.71 | -1.4 dB |
| Peaking | 779 Hz  | 5.32 | -1.4 dB |
| Peaking | 1565 Hz | 2.38 | 0.6 dB  |
| Peaking | 2098 Hz | 6.18 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7000/Denon%20AH-D7000.png)