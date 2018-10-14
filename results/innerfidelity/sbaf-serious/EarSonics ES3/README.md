# EarSonics ES3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -2.9; 23 -3.0; 25 -3.2; 28 -3.3; 31 -3.4; 34 -3.5; 37 -3.5; 41 -3.5; 45 -3.5; 49 -3.5; 54 -3.5; 60 -3.4; 66 -3.4; 72 -3.3; 79 -3.3; 87 -3.1; 96 -2.9; 106 -2.4; 116 -1.9; 128 -1.3; 141 -0.7; 155 0.1; 170 0.8; 187 1.6; 206 2.2; 227 2.8; 249 2.9; 274 3.0; 302 2.9; 332 2.7; 365 2.4; 402 2.1; 442 2.0; 486 1.7; 535 1.6; 588 1.7; 647 1.7; 712 1.4; 783 1.4; 861 0.9; 947 0.4; 1042 -0.3; 1146 -1.0; 1261 -1.7; 1387 -2.8; 1526 -3.8; 1678 -4.4; 1846 -3.8; 2031 -1.5; 2234 1.5; 2457 3.6; 2703 5.4; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.9; 5793 6.0; 6373 3.6; 7010 -0.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `EarSonics ES3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.31 | -3.6 dB |
| Peaking | 116 Hz  | 0.78 | -3.5 dB |
| Peaking | 202 Hz  | 0.5  | 5.1 dB  |
| Peaking | 1695 Hz | 1.91 | -7.7 dB |
| Peaking | 3427 Hz | 0.88 | 7.6 dB  |
| Peaking | 1947 Hz | 6.42 | -0.9 dB |
| Peaking | 2750 Hz | 2.2  | 1.2 dB  |
| Peaking | 3443 Hz | 3.13 | -1.5 dB |
| Peaking | 5999 Hz | 2.8  | 6.6 dB  |
| Peaking | 6671 Hz | 1.92 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/EarSonics%20ES3/EarSonics%20ES3.png)