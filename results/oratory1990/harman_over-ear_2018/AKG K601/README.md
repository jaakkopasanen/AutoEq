# AKG K601

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 5.5; 72 4.4; 79 3.5; 87 2.8; 96 2.2; 106 1.6; 116 1.1; 128 0.6; 141 0.3; 155 0.0; 170 -0.1; 187 -0.3; 206 -0.4; 227 -0.5; 249 -0.5; 274 -0.3; 302 -0.0; 332 0.2; 365 0.3; 402 0.4; 442 0.6; 486 0.7; 535 1.0; 588 1.2; 647 1.5; 712 1.7; 783 1.3; 861 0.7; 947 0.2; 1042 -0.2; 1146 -0.8; 1261 -1.2; 1387 -1.8; 1526 -2.6; 1678 -3.5; 1846 -4.2; 2031 -5.1; 2234 -5.7; 2457 -5.8; 2703 -5.4; 2973 -4.0; 3270 -1.6; 3597 -1.3; 3957 -1.9; 4353 -0.4; 4788 0.7; 5267 1.6; 5793 0.2; 6373 -0.2; 7010 0.3; 7711 -1.7; 8482 -1.4; 9330 0.0; 10263 0.0; 11289 0.0; 12418 -0.2; 13660 -0.8; 15026 0.0; 16529 -0.7; 18182 -4.4; 20000 -8.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.66 | 6.9 dB  |
| Peaking | 705 Hz   | 2.13 | 2.1 dB  |
| Peaking | 2280 Hz  | 1.42 | -6.1 dB |
| Peaking | 5131 Hz  | 4.79 | 2.5 dB  |
| Peaking | 19678 Hz | 1.78 | -8.0 dB |
| Peaking | 40 Hz    | 2.72 | -1.0 dB |
| Peaking | 61 Hz    | 2.7  | 1.7 dB  |
| Peaking | 181 Hz   | 1.28 | -1.1 dB |
| Peaking | 8040 Hz  | 6.56 | -2.9 dB |
| Peaking | 8547 Hz  | 1.65 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K601/AKG%20K601.png)