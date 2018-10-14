# Stax SR-Sigma 07381

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 6.0; 60 6.0; 66 6.0; 72 4.9; 79 3.5; 87 2.3; 96 1.5; 106 1.2; 116 1.4; 128 1.5; 141 2.1; 155 2.9; 170 1.9; 187 -1.8; 206 -0.6; 227 -0.7; 249 -1.3; 274 -0.9; 302 -0.6; 332 0.0; 365 0.6; 402 0.9; 442 1.6; 486 2.0; 535 2.5; 588 3.0; 647 2.2; 712 1.0; 783 0.7; 861 0.0; 947 0.4; 1042 0.7; 1146 0.9; 1261 2.3; 1387 3.5; 1526 5.2; 1678 5.9; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 5.6; 5793 2.7; 6373 2.9; 7010 2.4; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-Sigma 07381 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.42 | 6.2 dB  |
| Peaking | 62 Hz   | 3.18 | 2.3 dB  |
| Peaking | 562 Hz  | 1.29 | 8.1 dB  |
| Peaking | 687 Hz  | 0.57 | -7.7 dB |
| Peaking | 2216 Hz | 0.5  | 8.3 dB  |
| Peaking | 164 Hz  | 5.33 | 4.6 dB  |
| Peaking | 181 Hz  | 4.78 | -3.5 dB |
| Peaking | 1178 Hz | 7.08 | -0.7 dB |
| Peaking | 4875 Hz | 3.75 | 2.4 dB  |
| Peaking | 8860 Hz | 1.35 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-Sigma%2007381/Stax%20SR-Sigma%2007381.png)