# AKG K3003 Reference Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 3.7; 25 3.2; 28 2.6; 31 2.1; 34 1.7; 37 1.3; 41 0.8; 45 0.4; 49 0.1; 54 -0.4; 60 -0.9; 66 -1.3; 72 -1.8; 79 -2.2; 87 -2.7; 96 -3.2; 106 -3.5; 116 -3.6; 128 -4.0; 141 -4.3; 155 -4.4; 170 -4.4; 187 -4.4; 206 -4.3; 227 -4.1; 249 -4.0; 274 -3.7; 302 -3.4; 332 -3.1; 365 -2.7; 402 -2.3; 442 -1.7; 486 -1.5; 535 -1.1; 588 -0.4; 647 -0.1; 712 0.0; 783 0.4; 861 0.3; 947 0.1; 1042 -0.2; 1146 -0.4; 1261 -0.7; 1387 -1.1; 1526 -1.5; 1678 -2.2; 1846 -2.2; 2031 -2.0; 2234 -1.7; 2457 -0.6; 2703 0.9; 2973 2.8; 3270 4.7; 3597 6.0; 3957 5.9; 4353 0.7; 4788 -3.6; 5267 -2.7; 5793 0.4; 6373 3.8; 7010 2.5; 7711 0.3; 8482 -1.7; 9330 -5.6; 10263 -6.3; 11289 -0.9; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.88 | 4.4 dB   |
| Peaking | 166 Hz   | 0.61 | -4.7 dB  |
| Peaking | 3695 Hz  | 2.12 | 14.9 dB  |
| Peaking | 5204 Hz  | 0.74 | -12.1 dB |
| Peaking | 6523 Hz  | 2.87 | 12.8 dB  |
| Peaking | 823 Hz   | 2.06 | 1.4 dB   |
| Peaking | 1830 Hz  | 3.37 | -1.4 dB  |
| Peaking | 8144 Hz  | 7.05 | 2.4 dB   |
| Peaking | 10036 Hz | 3.16 | -7.3 dB  |
| Peaking | 11506 Hz | 1.57 | 4.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)