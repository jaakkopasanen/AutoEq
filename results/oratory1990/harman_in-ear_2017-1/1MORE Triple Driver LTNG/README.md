# 1MORE Triple Driver LTNG

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -1.1; 23 -1.4; 25 -1.8; 28 -2.2; 31 -2.5; 34 -2.8; 37 -3.0; 41 -3.3; 45 -3.5; 49 -3.7; 54 -4.0; 60 -4.3; 66 -4.6; 72 -4.8; 79 -5.1; 87 -5.4; 96 -5.7; 106 -6.0; 116 -6.1; 128 -6.3; 141 -6.3; 155 -6.2; 170 -6.1; 187 -5.9; 206 -5.7; 227 -5.4; 249 -5.0; 274 -4.7; 302 -4.2; 332 -3.6; 365 -3.0; 402 -2.7; 442 -2.3; 486 -1.8; 535 -1.3; 588 -0.9; 647 -0.5; 712 -0.1; 783 0.2; 861 0.3; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -0.7; 1387 -0.7; 1526 -0.8; 1678 -0.9; 1846 -1.2; 2031 -1.4; 2234 -1.6; 2457 -1.7; 2703 -1.1; 2973 -0.2; 3270 0.1; 3597 -0.6; 3957 -2.6; 4353 -4.1; 4788 -1.5; 5267 4.5; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 0.0; 10263 -0.3; 11289 -2.6; 12418 -6.9; 13660 -15.7; 15026 -25.4; 16529 -29.7; 18182 -20.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Triple Driver LTNG ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 79 Hz    | 0.42 | -3.8 dB  |
| Peaking | 191 Hz   | 0.66 | -3.9 dB  |
| Peaking | 4255 Hz  | 4.36 | -6.7 dB  |
| Peaking | 7484 Hz  | 0.79 | 9.3 dB   |
| Peaking | 16190 Hz | 1.46 | -34.1 dB |
| Peaking | 2263 Hz  | 2.03 | -2.2 dB  |
| Peaking | 5838 Hz  | 4.43 | 4.1 dB   |
| Peaking | 7843 Hz  | 2.96 | -4.3 dB  |
| Peaking | 11650 Hz | 1.69 | 5.2 dB   |
| Peaking | 14411 Hz | 2.64 | -6.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/1MORE%20Triple%20Driver%20LTNG/1MORE%20Triple%20Driver%20LTNG.png)