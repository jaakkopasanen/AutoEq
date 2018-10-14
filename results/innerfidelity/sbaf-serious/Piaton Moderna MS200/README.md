# Piaton Moderna MS200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 0.4; 25 -0.2; 28 -1.0; 31 -1.7; 34 -2.3; 37 -2.8; 41 -3.5; 45 -4.1; 49 -4.6; 54 -5.2; 60 -5.8; 66 -6.4; 72 -6.9; 79 -7.5; 87 -8.0; 96 -8.7; 106 -9.0; 116 -9.2; 128 -9.5; 141 -9.9; 155 -10.0; 170 -10.0; 187 -10.1; 206 -10.0; 227 -9.8; 249 -9.7; 274 -9.4; 302 -9.0; 332 -8.6; 365 -8.2; 402 -7.4; 442 -6.4; 486 -6.5; 535 -6.0; 588 -4.9; 647 -3.9; 712 -2.9; 783 -1.8; 861 -1.0; 947 -0.3; 1042 0.1; 1146 0.4; 1261 0.4; 1387 -0.5; 1526 -1.8; 1678 -2.5; 1846 -3.3; 2031 -3.5; 2234 -3.5; 2457 -1.9; 2703 0.4; 2973 3.2; 3270 5.3; 3597 6.0; 3957 5.5; 4353 3.0; 4788 1.8; 5267 2.3; 5793 1.8; 6373 -0.9; 7010 -2.5; 7711 -3.4; 8482 -3.7; 9330 -3.3; 10263 -2.4; 11289 -0.2; 12418 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Piaton Moderna MS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 137 Hz  | 0.44 | -8.9 dB  |
| Peaking | 415 Hz  | 0.64 | -5.0 dB  |
| Peaking | 2156 Hz | 1.08 | -16.5 dB |
| Peaking | 2969 Hz | 0.41 | 15.5 dB  |
| Peaking | 7650 Hz | 0.95 | -9.7 dB  |
| Peaking | 20 Hz   | 1.98 | 2.1 dB   |
| Peaking | 2685 Hz | 5.61 | -1.2 dB  |
| Peaking | 3726 Hz | 2.55 | 2.1 dB   |
| Peaking | 4562 Hz | 3.39 | -3.0 dB  |
| Peaking | 5605 Hz | 5.67 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Piaton%20Moderna%20MS200/Piaton%20Moderna%20MS200.png)