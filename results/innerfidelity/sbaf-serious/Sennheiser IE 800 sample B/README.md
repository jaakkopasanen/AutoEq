# Sennheiser IE 800 sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 5.9; 31 5.6; 34 5.1; 37 4.5; 41 3.9; 45 3.3; 49 2.8; 54 2.2; 60 1.6; 66 1.1; 72 0.6; 79 0.0; 87 -0.5; 96 -1.1; 106 -1.5; 116 -1.7; 128 -2.2; 141 -2.5; 155 -2.8; 170 -2.9; 187 -2.9; 206 -3.0; 227 -2.8; 249 -2.8; 274 -2.6; 302 -2.4; 332 -2.2; 365 -1.9; 402 -1.6; 442 -1.2; 486 -1.0; 535 -0.7; 588 -0.1; 647 0.2; 712 0.3; 783 0.6; 861 0.4; 947 0.2; 1042 -0.1; 1146 -0.4; 1261 -0.5; 1387 -0.9; 1526 -1.0; 1678 -0.8; 1846 0.2; 2031 1.4; 2234 2.9; 2457 5.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 5.1; 5267 3.9; 5793 1.9; 6373 3.7; 7010 2.5; 7711 0.3; 8482 -0.0; 9330 -2.0; 10263 -3.5; 11289 -5.1; 12418 -5.0; 13660 -3.1; 15026 -2.2; 16529 -0.2; 18182 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 23 Hz    |  0.59 | 5.7 dB  |
| Peaking | 34 Hz    |  0.75 | 0.8 dB  |
| Peaking | 181 Hz   |  0.58 | -3.3 dB |
| Peaking | 3758 Hz  |  1.09 | 6.9 dB  |
| Peaking | 11787 Hz |  1.84 | -6.1 dB |
| Peaking | 763 Hz   |  1.42 | 1.7 dB  |
| Peaking | 1543 Hz  |  0.38 | -1.1 dB |
| Peaking | 1605 Hz  |  2.45 | -1.5 dB |
| Peaking | 2578 Hz  |  3.58 | 3.2 dB  |
| Peaking | 6669 Hz  | 11.12 | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20B/Sennheiser%20IE%20800%20sample%20B.png)