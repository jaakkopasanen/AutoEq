# Grado SR325

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 5.0; 49 4.1; 54 3.2; 60 2.3; 66 1.6; 72 1.0; 79 0.6; 87 0.1; 96 -0.3; 106 -0.3; 116 -0.3; 128 -0.3; 141 -0.3; 155 -0.3; 170 -0.1; 187 0.1; 206 -0.0; 227 0.1; 249 0.2; 274 0.3; 302 0.5; 332 0.9; 365 1.1; 402 0.4; 442 0.5; 486 0.5; 535 0.3; 588 0.7; 647 0.6; 712 0.5; 783 0.6; 861 0.4; 947 0.0; 1042 -0.1; 1146 -0.3; 1261 -1.1; 1387 -2.3; 1526 -3.6; 1678 -4.3; 1846 -5.4; 2031 -9.4; 2234 -7.5; 2457 -5.5; 2703 -4.1; 2973 -2.1; 3270 -1.1; 3597 2.2; 3957 -3.7; 4353 -7.5; 4788 -8.8; 5267 -5.7; 5793 -3.7; 6373 -3.0; 7010 -5.8; 7711 -5.9; 8482 -8.9; 9330 -11.0; 10263 -8.1; 11289 -3.6; 12418 -0.4; 13660 0.0; 15026 0.0; 16529 -0.4; 18182 -1.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 1.01 | 7.0 dB   |
| Peaking | 2058 Hz  | 3.21 | -8.2 dB  |
| Peaking | 9869 Hz  | 1    | -22.0 dB |
| Peaking | 11431 Hz | 0.9  | 14.2 dB  |
| Peaking | 24000 Hz | 2.25 | -8.3 dB  |
| Peaking | 105 Hz   | 2.21 | -1.1 dB  |
| Peaking | 2509 Hz  | 6.96 | -0.5 dB  |
| Peaking | 3689 Hz  | 6.24 | 8.5 dB   |
| Peaking | 4533 Hz  | 2.82 | -6.7 dB  |
| Peaking | 6139 Hz  | 4.37 | 3.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325/Grado%20SR325.png)