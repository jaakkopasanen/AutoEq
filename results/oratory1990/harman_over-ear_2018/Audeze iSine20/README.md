# Audeze iSine20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 6.0; 79 6.0; 87 6.0; 96 6.0; 106 5.9; 116 5.6; 128 5.3; 141 5.0; 155 4.7; 170 4.5; 187 4.4; 206 4.2; 227 4.1; 249 4.0; 274 4.1; 302 4.1; 332 4.1; 365 4.1; 402 4.0; 442 3.8; 486 3.6; 535 3.3; 588 3.0; 647 2.5; 712 1.9; 783 1.5; 861 1.3; 947 0.5; 1042 -0.3; 1146 -0.6; 1261 -0.9; 1387 -1.4; 1526 -0.1; 1678 2.3; 1846 4.9; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze iSine20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.18 | 6.2 dB  |
| Peaking | 434 Hz  | 1.08 | 2.2 dB  |
| Peaking | 1375 Hz | 1.65 | -6.4 dB |
| Peaking | 2186 Hz | 0.83 | 7.6 dB  |
| Peaking | 5188 Hz | 1.92 | 4.7 dB  |
| Peaking | 1014 Hz | 5.87 | -0.5 dB |
| Peaking | 2615 Hz | 2.76 | -1.7 dB |
| Peaking | 3381 Hz | 0.98 | 1.8 dB  |
| Peaking | 6356 Hz | 3.95 | 4.8 dB  |
| Peaking | 6595 Hz | 1.26 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Audeze%20iSine20/Audeze%20iSine20.png)