# Sennheiser Momentum M2 OEBT Wired Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 4.5; 25 4.0; 28 3.2; 31 2.4; 34 1.7; 37 1.2; 41 0.5; 45 -0.4; 49 -1.2; 54 -2.3; 60 -3.4; 66 -4.2; 72 -4.5; 79 -4.9; 87 -5.8; 96 -6.0; 106 -5.3; 116 -4.5; 128 -3.5; 141 -2.4; 155 -1.3; 170 -0.5; 187 0.1; 206 0.5; 227 1.1; 249 1.7; 274 2.4; 302 3.1; 332 3.8; 365 3.9; 402 3.6; 442 3.4; 486 3.1; 535 2.9; 588 2.8; 647 2.3; 712 1.7; 783 1.3; 861 0.7; 947 0.2; 1042 -0.2; 1146 -0.3; 1261 -0.7; 1387 -1.5; 1526 -2.6; 1678 -3.5; 1846 -4.2; 2031 -4.6; 2234 -5.0; 2457 -4.1; 2703 -3.0; 2973 -1.1; 3270 1.2; 3597 3.0; 3957 5.9; 4353 6.0; 4788 3.6; 5267 1.6; 5793 4.1; 6373 2.9; 7010 0.4; 7711 -0.5; 8482 -2.7; 9330 -4.0; 10263 -0.2; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 OEBT Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.84 | 5.5 dB  |
| Peaking | 90 Hz   | 0.95 | -6.9 dB |
| Peaking | 377 Hz  | 0.67 | 4.3 dB  |
| Peaking | 2216 Hz | 1.14 | -6.0 dB |
| Peaking | 4097 Hz | 2.09 | 7.9 dB  |
| Peaking | 5112 Hz | 9.89 | -2.3 dB |
| Peaking | 5968 Hz | 5.92 | 3.4 dB  |
| Peaking | 9000 Hz | 4.96 | -4.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Active/Sennheiser%20Momentum%20M2%20OEBT%20Wired%20Active.png)