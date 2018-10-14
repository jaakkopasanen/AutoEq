# Shure SRH1840

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 6.0; 54 5.8; 60 5.2; 66 4.8; 72 4.8; 79 4.5; 87 3.6; 96 2.8; 106 2.2; 116 1.8; 128 1.3; 141 0.9; 155 0.5; 170 0.3; 187 0.0; 206 -0.2; 227 -0.2; 249 -0.2; 274 -0.2; 302 -0.3; 332 -0.2; 365 -0.1; 402 0.1; 442 0.4; 486 0.5; 535 0.7; 588 1.0; 647 0.9; 712 0.9; 783 1.4; 861 0.6; 947 0.1; 1042 -0.1; 1146 -0.4; 1261 -0.5; 1387 -1.0; 1526 -1.9; 1678 -2.8; 1846 -3.6; 2031 -4.2; 2234 -4.7; 2457 -4.2; 2703 -4.3; 2973 -4.1; 3270 -4.0; 3597 -4.0; 3957 -3.4; 4353 -2.9; 4788 -1.5; 5267 0.5; 5793 0.3; 6373 0.3; 7010 0.8; 7711 -1.1; 8482 -5.0; 9330 -5.0; 10263 -0.1; 11289 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SRH1840 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.56 | 6.7 dB  |
| Peaking | 949 Hz   | 0.99 | 2.3 dB  |
| Peaking | 3061 Hz  | 0.52 | -6.1 dB |
| Peaking | 6535 Hz  | 0.83 | 4.8 dB  |
| Peaking | 8831 Hz  | 4.14 | -8.0 dB |
| Peaking | 36 Hz    | 3.01 | -0.8 dB |
| Peaking | 78 Hz    | 2.38 | 1.3 dB  |
| Peaking | 217 Hz   | 0.77 | -0.9 dB |
| Peaking | 556 Hz   | 2.23 | 0.6 dB  |
| Peaking | 10279 Hz | 7.84 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SRH1840/Shure%20SRH1840.png)