# Oppo PM3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 0.0; 23 1.1; 25 1.2; 28 1.4; 31 1.6; 34 1.9; 37 2.1; 41 2.7; 45 3.1; 49 3.0; 54 2.0; 60 1.1; 66 0.4; 72 -0.5; 79 -1.3; 87 -1.8; 96 -2.6; 106 -3.3; 116 -3.7; 128 -3.8; 141 -3.9; 155 -3.7; 170 -3.3; 187 -2.7; 206 -2.2; 227 -1.4; 249 -0.4; 274 0.6; 302 1.4; 332 2.0; 365 2.3; 402 2.0; 442 1.7; 486 1.3; 535 0.6; 588 0.4; 647 0.3; 712 0.3; 783 0.3; 861 0.2; 947 0.1; 1042 -0.2; 1146 -1.1; 1261 -1.7; 1387 -1.8; 1526 -2.0; 1678 -2.4; 1846 -2.8; 2031 -2.3; 2234 -2.0; 2457 -2.4; 2703 -2.5; 2973 -1.7; 3270 -1.7; 3597 -0.5; 3957 0.2; 4353 -0.4; 4788 0.1; 5267 1.2; 5793 -0.6; 6373 -5.0; 7010 -3.4; 7711 -3.5; 8482 -4.1; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 -4.0; 13660 -4.1; 15026 -0.1; 16529 0.0; 18182 0.0; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 44 Hz    | 1.59 | 3.4 dB  |
| Peaking | 128 Hz   | 1.51 | -4.6 dB |
| Peaking | 1978 Hz  | 1.51 | -2.8 dB |
| Peaking | 7229 Hz  | 2.89 | -4.2 dB |
| Peaking | 13194 Hz | 5.78 | -5.6 dB |
| Peaking | 201 Hz   | 2.49 | -1.5 dB |
| Peaking | 360 Hz   | 1.54 | 2.8 dB  |
| Peaking | 2748 Hz  | 5.42 | -1.0 dB |
| Peaking | 5255 Hz  | 8.32 | 2.6 dB  |
| Peaking | 10511 Hz | 6.14 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Oppo%20PM3/Oppo%20PM3.png)