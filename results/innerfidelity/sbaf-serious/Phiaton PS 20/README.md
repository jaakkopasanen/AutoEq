# Phiaton PS 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.4; 25 3.8; 28 3.1; 31 2.5; 34 1.9; 37 1.5; 41 0.9; 45 0.4; 49 -0.1; 54 -0.6; 60 -1.2; 66 -1.8; 72 -2.3; 79 -2.9; 87 -3.5; 96 -4.1; 106 -4.5; 116 -4.8; 128 -5.3; 141 -5.7; 155 -6.0; 170 -6.2; 187 -6.4; 206 -6.6; 227 -6.8; 249 -7.0; 274 -7.0; 302 -7.1; 332 -7.1; 365 -7.2; 402 -7.4; 442 -7.0; 486 -7.1; 535 -6.7; 588 -5.9; 647 -5.0; 712 -3.9; 783 -2.5; 861 -1.3; 947 -0.4; 1042 0.2; 1146 0.5; 1261 0.2; 1387 -0.7; 1526 -2.1; 1678 -3.5; 1846 -4.9; 2031 -5.7; 2234 -5.4; 2457 -2.4; 2703 0.6; 2973 4.1; 3270 6.0; 3597 6.0; 3957 5.4; 4353 1.6; 4788 -2.0; 5267 -4.1; 5793 -1.3; 6373 2.3; 7010 2.4; 7711 0.3; 8482 -1.0; 9330 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 20 Hz   | 0.95 | 5.2 dB   |
| Peaking | 274 Hz  | 0.4  | -7.7 dB  |
| Peaking | 2163 Hz | 2.02 | -14.3 dB |
| Peaking | 2929 Hz | 0.73 | 10.6 dB  |
| Peaking | 5156 Hz | 3.75 | -9.0 dB  |
| Peaking | 587 Hz  | 1.15 | -5.7 dB  |
| Peaking | 743 Hz  | 0.62 | 4.8 dB   |
| Peaking | 1656 Hz | 2.85 | -2.8 dB  |
| Peaking | 6766 Hz | 5.29 | 3.8 dB   |
| Peaking | 7898 Hz | 1.57 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%2020/Phiaton%20PS%2020.png)