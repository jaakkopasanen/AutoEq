# Havi B3 Pro1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.7; 54 5.3; 60 4.7; 66 4.3; 72 3.9; 79 3.4; 87 3.0; 96 2.5; 106 2.1; 116 1.9; 128 1.5; 141 1.2; 155 0.9; 170 0.7; 187 0.6; 206 0.3; 227 0.4; 249 0.1; 274 0.1; 302 -0.0; 332 -0.1; 365 -0.2; 402 -0.3; 442 -0.3; 486 -0.5; 535 -0.6; 588 -0.4; 647 -0.3; 712 -0.5; 783 -0.2; 861 -0.1; 947 -0.0; 1042 0.2; 1146 0.7; 1261 0.4; 1387 0.8; 1526 1.1; 1678 1.0; 1846 1.5; 2031 1.8; 2234 2.4; 2457 3.5; 2703 4.5; 2973 5.7; 3270 6.0; 3597 5.1; 3957 3.5; 4353 4.2; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Havi B3 Pro1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.51 | 6.5 dB  |
| Peaking | 3033 Hz  | 1.99 | 4.9 dB  |
| Peaking | 5854 Hz  | 1.56 | 6.6 dB  |
| Peaking | 7642 Hz  | 3.44 | -2.5 dB |
| Peaking | 9191 Hz  | 1.2  | -1.1 dB |
| Peaking | 479 Hz   | 1.06 | -0.7 dB |
| Peaking | 21268 Hz | 1.99 | -0.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Havi%20B3%20Pro1/Havi%20B3%20Pro1.png)