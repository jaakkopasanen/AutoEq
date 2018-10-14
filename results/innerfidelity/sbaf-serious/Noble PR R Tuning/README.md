# Noble PR R Tuning

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.9; 60 5.6; 66 5.2; 72 4.8; 79 4.4; 87 4.0; 96 3.5; 106 3.1; 116 2.8; 128 2.5; 141 2.2; 155 1.9; 170 1.7; 187 1.6; 206 1.4; 227 1.4; 249 1.3; 274 1.3; 302 1.3; 332 1.3; 365 1.4; 402 1.4; 442 1.6; 486 1.6; 535 1.6; 588 1.8; 647 1.8; 712 1.7; 783 1.6; 861 1.0; 947 0.5; 1042 -0.3; 1146 -0.9; 1261 -1.6; 1387 -2.6; 1526 -3.5; 1678 -4.3; 1846 -4.6; 2031 -4.4; 2234 -4.2; 2457 -3.1; 2703 -1.7; 2973 0.7; 3270 2.6; 3597 3.0; 3957 1.6; 4353 -1.4; 4788 -2.8; 5267 -1.7; 5793 1.3; 6373 4.9; 7010 2.5; 7711 0.3; 8482 -1.1; 9330 -3.2; 10263 -2.7; 11289 -0.5; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble PR R Tuning ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.12 | 6.3 dB  |
| Peaking | 1952 Hz | 1.77 | -5.2 dB |
| Peaking | 3408 Hz | 5.28 | 4.6 dB  |
| Peaking | 6496 Hz | 7.19 | 5.9 dB  |
| Peaking | 9612 Hz | 3.93 | -3.6 dB |
| Peaking | 148 Hz  | 1.42 | -0.7 dB |
| Peaking | 680 Hz  | 0.89 | 2.0 dB  |
| Peaking | 1353 Hz | 1.79 | -1.4 dB |
| Peaking | 4754 Hz | 1.51 | 2.1 dB  |
| Peaking | 4834 Hz | 3.88 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Noble%20PR%20R%20Tuning/Noble%20PR%20R%20Tuning.png)