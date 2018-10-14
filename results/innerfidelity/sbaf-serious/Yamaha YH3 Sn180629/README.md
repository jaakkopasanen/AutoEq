# Yamaha YH3 Sn180629

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.5; 28 2.2; 31 1.9; 34 1.7; 37 1.5; 41 1.4; 45 1.2; 49 1.1; 54 0.9; 60 0.6; 66 0.3; 72 0.1; 79 -0.1; 87 -0.3; 96 -0.7; 106 -1.2; 116 -1.3; 128 -1.6; 141 -1.9; 155 -2.2; 170 -2.2; 187 -2.5; 206 -2.6; 227 -2.6; 249 -2.7; 274 -2.6; 302 -2.4; 332 -2.2; 365 -2.1; 402 -2.3; 442 -2.2; 486 -2.3; 535 -2.2; 588 -2.0; 647 -2.1; 712 -2.0; 783 -1.2; 861 -1.0; 947 -0.6; 1042 0.5; 1146 1.9; 1261 3.3; 1387 4.3; 1526 4.3; 1678 4.1; 1846 3.5; 2031 1.7; 2234 0.7; 2457 0.7; 2703 2.0; 2973 4.9; 3270 6.0; 3597 4.3; 3957 3.4; 4353 3.5; 4788 4.8; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.4; 16529 -1.2; 18182 -0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH3 Sn180629 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.19 | 3.0 dB  |
| Peaking | 885 Hz   | 0.08 | -3.0 dB |
| Peaking | 1483 Hz  | 1.51 | 7.3 dB  |
| Peaking | 3236 Hz  | 3.62 | 6.7 dB  |
| Peaking | 5557 Hz  | 1.8  | 8.4 dB  |
| Peaking | 2367 Hz  | 6.56 | -0.8 dB |
| Peaking | 6560 Hz  | 0.19 | 0.2 dB  |
| Peaking | 7952 Hz  | 5.18 | -1.3 dB |
| Peaking | 14218 Hz | 1.53 | 0.6 dB  |
| Peaking | 16149 Hz | 3.99 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH3%20Sn180629/Yamaha%20YH3%20Sn180629.png)