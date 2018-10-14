# VSonic VSD3S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 21 0.0; 23 0.4; 25 0.1; 28 -0.3; 31 -0.6; 34 -0.8; 37 -1.1; 41 -1.3; 45 -1.6; 49 -1.8; 54 -2.1; 60 -2.4; 66 -2.8; 72 -3.1; 79 -3.4; 87 -3.8; 96 -4.1; 106 -4.4; 116 -4.5; 128 -4.7; 141 -4.9; 155 -4.9; 170 -4.9; 187 -4.9; 206 -4.8; 227 -4.6; 249 -4.4; 274 -4.1; 302 -3.9; 332 -3.6; 365 -3.2; 402 -2.9; 442 -2.4; 486 -2.2; 535 -1.8; 588 -1.1; 647 -0.8; 712 -0.6; 783 -0.1; 861 -0.0; 947 -0.0; 1042 0.0; 1146 0.1; 1261 0.2; 1387 0.0; 1526 -0.3; 1678 -0.3; 1846 0.2; 2031 0.8; 2234 1.4; 2457 2.3; 2703 2.8; 2973 3.7; 3270 4.6; 3597 4.9; 3957 3.9; 4353 1.3; 4788 -0.3; 5267 -1.6; 5793 -2.5; 6373 0.0; 7010 1.7; 7711 0.3; 8482 -0.7; 9330 -4.0; 10263 -4.5; 11289 -1.8; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.1dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 129 Hz  | 0.57 | -4.3 dB |
| Peaking | 295 Hz  | 0.95 | -2.0 dB |
| Peaking | 3422 Hz | 1.82 | 5.2 dB  |
| Peaking | 5383 Hz | 4.5  | -3.6 dB |
| Peaking | 9950 Hz | 4.69 | -5.5 dB |
| Peaking | 20 Hz   | 1.82 | 1.2 dB  |
| Peaking | 867 Hz  | 2.74 | 0.5 dB  |
| Peaking | 1650 Hz | 5.54 | -0.8 dB |
| Peaking | 5932 Hz | 8.63 | -1.3 dB |
| Peaking | 6938 Hz | 5.81 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3S/VSonic%20VSD3S.png)