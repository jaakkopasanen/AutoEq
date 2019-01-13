# Ortofon 0-One
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 6.0; 37 6.0; 41 5.7; 45 5.4; 49 5.1; 54 5.1; 60 5.8; 66 5.4; 72 4.0; 79 3.0; 87 2.4; 96 2.2; 106 2.3; 116 2.2; 128 2.0; 141 2.2; 155 2.7; 170 2.9; 187 3.5; 206 4.2; 227 5.1; 249 6.0; 274 6.0; 302 6.0; 332 4.4; 365 1.9; 402 0.1; 442 -0.6; 486 -1.0; 535 -0.8; 588 -0.3; 647 1.8; 712 2.7; 783 1.2; 861 0.5; 947 0.1; 1042 -0.1; 1146 1.7; 1261 1.5; 1387 0.6; 1526 -0.6; 1678 0.0; 1846 2.8; 2031 5.7; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 5.9; 3957 2.9; 4353 5.5; 4788 4.0; 5267 2.3; 5793 5.4; 6373 5.5; 7010 2.5; 7711 0.3; 8482 -0.1; 9330 -0.5; 10263 0.0; 11289 0.0; 12418 0.0; 13660 0.0; 15026 0.0; 16529 -0.3; 18182 -1.5; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Ortofon 0-One GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 0-One ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.43 | 6.1 dB  |
| Peaking | 62 Hz   | 4.94 | 2.1 dB  |
| Peaking | 257 Hz  | 2.09 | 6.2 dB  |
| Peaking | 2886 Hz | 1.28 | 6.7 dB  |
| Peaking | 6144 Hz | 5.13 | 5.1 dB  |
| Peaking | 319 Hz  | 6.15 | 2.5 dB  |
| Peaking | 482 Hz  | 1.81 | -2.3 dB |
| Peaking | 690 Hz  | 6.17 | 3.4 dB  |
| Peaking | 1613 Hz | 5.31 | -2.9 dB |
| Peaking | 2072 Hz | 6.26 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ortofon%200-One/Ortofon%200-One.png)