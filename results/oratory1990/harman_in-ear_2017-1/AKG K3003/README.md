# AKG K3003

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -3.7; 23 -3.8; 25 -3.9; 28 -3.9; 31 -3.9; 34 -3.8; 37 -3.8; 41 -3.9; 45 -4.1; 49 -4.3; 54 -4.4; 60 -4.6; 66 -4.8; 72 -5.0; 79 -5.4; 87 -5.7; 96 -6.0; 106 -6.3; 116 -6.5; 128 -6.7; 141 -6.8; 155 -6.9; 170 -6.9; 187 -6.9; 206 -6.7; 227 -6.5; 249 -6.3; 274 -6.0; 302 -5.5; 332 -5.0; 365 -4.5; 402 -4.0; 442 -3.6; 486 -3.0; 535 -2.5; 588 -2.0; 647 -1.4; 712 -0.9; 783 -0.4; 861 -0.1; 947 0.0; 1042 -0.0; 1146 -0.0; 1261 0.2; 1387 0.5; 1526 1.0; 1678 1.6; 1846 2.1; 2031 2.8; 2234 3.8; 2457 5.1; 2703 6.0; 2973 5.7; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 1.9; 5267 0.2; 5793 -0.8; 6373 0.2; 7010 -0.4; 7711 -1.9; 8482 -1.2; 9330 -0.2; 10263 0.0; 11289 0.0; 12418 -0.2; 13660 -10.0; 15026 -19.8; 16529 -17.7; 18182 -8.9; 20000 -2.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 0.17 | -3.5 dB  |
| Peaking | 134 Hz   | 0.75 | -3.4 dB  |
| Peaking | 277 Hz   | 0.76 | -3.9 dB  |
| Peaking | 3176 Hz  | 1.22 | 6.9 dB   |
| Peaking | 15837 Hz | 2.3  | -22.7 dB |
| Peaking | 4400 Hz  | 5.41 | 4.1 dB   |
| Peaking | 5081 Hz  | 2.52 | -3.0 dB  |
| Peaking | 7829 Hz  | 5.99 | -1.8 dB  |
| Peaking | 12429 Hz | 2.12 | 6.8 dB   |
| Peaking | 14364 Hz | 3.78 | -8.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/AKG%20K3003/AKG%20K3003.png)