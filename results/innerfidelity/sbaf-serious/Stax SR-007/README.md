# Stax SR-007
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 6.0; 45 6.0; 49 5.2; 54 2.7; 60 2.8; 66 3.5; 72 3.7; 79 3.8; 87 3.6; 96 3.4; 106 3.2; 116 3.2; 128 2.9; 141 2.6; 155 2.4; 170 2.3; 187 2.2; 206 1.9; 227 1.9; 249 1.7; 274 1.7; 302 1.5; 332 1.4; 365 1.3; 402 1.2; 442 1.4; 486 2.1; 535 2.4; 588 1.6; 647 0.6; 712 0.3; 783 0.6; 861 0.5; 947 0.2; 1042 0.5; 1146 2.0; 1261 3.9; 1387 -0.1; 1526 -0.9; 1678 -0.3; 1846 1.9; 2031 3.8; 2234 4.9; 2457 5.9; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.2; 3957 4.6; 4353 3.3; 4788 2.0; 5267 3.4; 5793 5.2; 6373 5.3; 7010 2.5; 7711 0.3; 8482 -0.9; 9330 -1.4; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 0.0; 18182 0.0; 20000 -3.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Stax SR-007 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 28 Hz   |  0.68 | 6.0 dB  |
| Peaking | 125 Hz  |  0.5  | 2.3 dB  |
| Peaking | 519 Hz  |  4.34 | 1.9 dB  |
| Peaking | 2927 Hz |  1.49 | 6.6 dB  |
| Peaking | 6076 Hz |  4.45 | 4.9 dB  |
| Peaking | 1243 Hz |  5.57 | 5.7 dB  |
| Peaking | 1478 Hz |  2.14 | -3.9 dB |
| Peaking | 2121 Hz |  3.62 | 2.1 dB  |
| Peaking | 6694 Hz | 10.07 | 1.3 dB  |
| Peaking | 8887 Hz |  4.73 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007/Stax%20SR-007.png)