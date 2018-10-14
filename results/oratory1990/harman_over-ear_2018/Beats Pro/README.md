# Beats Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 21 -0.9; 23 -1.9; 25 -2.7; 28 -3.8; 31 -4.6; 34 -5.3; 37 -5.8; 41 -6.3; 45 -6.6; 49 -6.8; 54 -6.9; 60 -6.9; 66 -6.8; 72 -6.7; 79 -6.9; 87 -7.2; 96 -7.6; 106 -8.0; 116 -7.9; 128 -8.1; 141 -8.4; 155 -8.6; 170 -8.5; 187 -8.4; 206 -8.1; 227 -7.5; 249 -6.9; 274 -6.0; 302 -4.7; 332 -4.0; 365 -3.0; 402 -2.2; 442 -1.9; 486 -1.9; 535 -2.0; 588 -2.0; 647 -1.9; 712 -1.4; 783 -1.4; 861 -1.1; 947 -0.0; 1042 -0.3; 1146 0.1; 1261 0.6; 1387 0.8; 1526 0.4; 1678 -0.5; 1846 -1.7; 2031 -3.4; 2234 -5.5; 2457 -7.5; 2703 -9.4; 2973 -9.8; 3270 -7.8; 3597 -4.1; 3957 -0.3; 4353 -1.4; 4788 -3.7; 5267 -1.3; 5793 -0.2; 6373 -4.2; 7010 -5.2; 7711 -5.5; 8482 -2.6; 9330 -0.0; 10263 0.0; 11289 0.0; 12418 -0.9; 13660 -2.4; 15026 -2.7; 16529 -1.7; 18182 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9dB` and instead set Global volume in the UI for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of --0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 54 Hz    | 0.57 | -5.7 dB  |
| Peaking | 180 Hz   | 0.79 | -7.2 dB  |
| Peaking | 2820 Hz  | 2.7  | -10.7 dB |
| Peaking | 7295 Hz  | 4.04 | -6.0 dB  |
| Peaking | 14935 Hz | 2.68 | -3.0 dB  |
| Peaking | 649 Hz   | 4.04 | -0.8 dB  |
| Peaking | 1407 Hz  | 2.19 | 2.4 dB   |
| Peaking | 2711 Hz  | 0.59 | -0.9 dB  |
| Peaking | 3990 Hz  | 9.25 | 3.6 dB   |
| Peaking | 9904 Hz  | 3.67 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Beats%20Pro/Beats%20Pro.png)