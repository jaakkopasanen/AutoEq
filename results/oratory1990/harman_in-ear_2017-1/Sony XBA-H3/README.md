# Sony XBA-H3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.1; 25 -0.0; 28 -0.2; 31 -0.4; 34 -0.5; 37 -0.7; 41 -0.8; 45 -1.0; 49 -1.1; 54 -1.3; 60 -1.6; 66 -1.9; 72 -2.2; 79 -2.5; 87 -2.8; 96 -3.1; 106 -3.4; 116 -3.6; 128 -3.8; 141 -3.9; 155 -3.8; 170 -3.8; 187 -3.6; 206 -3.3; 227 -3.0; 249 -2.6; 274 -2.2; 302 -1.8; 332 -1.4; 365 -1.0; 402 -0.7; 442 -0.4; 486 -0.1; 535 0.1; 588 0.3; 647 0.5; 712 0.7; 783 0.7; 861 0.4; 947 0.2; 1042 -0.2; 1146 -0.6; 1261 -0.8; 1387 -0.6; 1526 -0.2; 1678 0.2; 1846 1.1; 2031 2.7; 2234 5.2; 2457 6.0; 2703 6.0; 2973 6.0; 3270 4.0; 3597 2.6; 3957 2.3; 4353 0.2; 4788 -2.4; 5267 -1.4; 5793 2.6; 6373 5.1; 7010 2.5; 7711 0.3; 8482 -0.5; 9330 -5.3; 10263 -7.4; 11289 -4.7; 12418 -4.0; 13660 -9.4; 15026 -15.7; 16529 -19.7; 18182 -19.5; 20000 -11.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-H3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 140 Hz   | 0.71 | -4.0 dB  |
| Peaking | 2686 Hz  | 2.32 | 7.1 dB   |
| Peaking | 6522 Hz  | 5.15 | 6.9 dB   |
| Peaking | 16675 Hz | 1.05 | -17.6 dB |
| Peaking | 18909 Hz | 1.56 | -8.0 dB  |
| Peaking | 1441 Hz  | 1.6  | -2.3 dB  |
| Peaking | 2380 Hz  | 0.23 | 1.1 dB   |
| Peaking | 4880 Hz  | 5.77 | -4.2 dB  |
| Peaking | 9966 Hz  | 5.84 | -4.7 dB  |
| Peaking | 12163 Hz | 5.88 | 3.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Sony%20XBA-H3/Sony%20XBA-H3.png)