# E-Mu Walnut

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 -0.2; 23 -0.5; 25 -0.8; 28 -1.1; 31 -1.3; 34 -1.5; 37 -1.7; 41 -1.8; 45 -1.9; 49 -2.1; 54 -2.2; 60 -2.3; 66 -2.4; 72 -2.5; 79 -2.7; 87 -2.8; 96 -2.9; 106 -2.9; 116 -2.9; 128 -3.0; 141 -3.0; 155 -2.9; 170 -2.6; 187 -2.4; 206 -2.2; 227 -1.8; 249 -1.5; 274 -1.1; 302 -0.6; 332 -0.3; 365 0.1; 402 0.5; 442 0.8; 486 0.6; 535 0.5; 588 0.6; 647 0.3; 712 -0.1; 783 -0.0; 861 -0.2; 947 -0.1; 1042 0.1; 1146 0.8; 1261 1.0; 1387 0.8; 1526 0.6; 1678 0.6; 1846 1.3; 2031 2.5; 2234 3.6; 2457 4.8; 2703 3.5; 2973 3.0; 3270 2.8; 3597 3.9; 3957 5.3; 4353 1.5; 4788 3.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0; 9330 -0.6; 10263 -0.7; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `E-Mu Walnut ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 70 Hz   | 0.66 | -2.4 dB |
| Peaking | 157 Hz  | 1.39 | -2.0 dB |
| Peaking | 2444 Hz | 2.55 | 4.3 dB  |
| Peaking | 3797 Hz | 5.91 | 4.1 dB  |
| Peaking | 5762 Hz | 3.32 | 6.6 dB  |
| Peaking | 241 Hz  | 3.55 | -0.5 dB |
| Peaking | 449 Hz  | 2.37 | 1.1 dB  |
| Peaking | 1225 Hz | 7.58 | 0.8 dB  |
| Peaking | 6557 Hz | 9.36 | 2.0 dB  |
| Peaking | 8656 Hz | 1.6  | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/E-Mu%20Walnut/E-Mu%20Walnut.png)