# Sennheiser Momentum Wireless Wired Active

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.4; 28 2.3; 31 2.6; 34 3.0; 37 3.3; 41 3.5; 45 3.8; 49 4.0; 54 4.3; 60 4.4; 66 4.6; 72 4.6; 79 4.6; 87 4.7; 96 4.6; 106 4.7; 116 4.9; 128 5.0; 141 5.0; 155 5.2; 170 5.4; 187 5.7; 206 5.9; 227 6.0; 249 6.0; 274 6.0; 302 6.0; 332 6.0; 365 6.0; 402 6.0; 442 6.0; 486 5.8; 535 4.9; 588 4.3; 647 3.4; 712 2.5; 783 2.0; 861 1.1; 947 0.4; 1042 -0.2; 1146 -0.6; 1261 -1.6; 1387 -2.7; 1526 -4.2; 1678 -4.9; 1846 -5.7; 2031 -5.7; 2234 -4.3; 2457 -1.5; 2703 0.8; 2973 3.7; 3270 5.8; 3597 6.0; 3957 6.0; 4353 6.0; 4788 1.8; 5267 3.6; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum Wireless Wired Active ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 100 Hz  |  0.23 | 4.4 dB  |
| Peaking | 413 Hz  |  0.73 | 3.8 dB  |
| Peaking | 1946 Hz |  1.26 | -8.3 dB |
| Peaking | 3464 Hz |  1.62 | 8.7 dB  |
| Peaking | 6072 Hz |  4.98 | 5.3 dB  |
| Peaking | 104 Hz  |  3.98 | -0.1 dB |
| Peaking | 4542 Hz |  6.53 | 2.5 dB  |
| Peaking | 4900 Hz | 14.47 | -5.0 dB |
| Peaking | 7974 Hz |  7.98 | -0.9 dB |
| Peaking | 9495 Hz |  3.49 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20Wireless%20Wired%20Active/Sennheiser%20Momentum%20Wireless%20Wired%20Active.png)