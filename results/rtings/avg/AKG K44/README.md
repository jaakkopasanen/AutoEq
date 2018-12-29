# AKG K44
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 21 0.0; 23 6.0; 25 6.0; 28 6.0; 31 6.0; 34 5.7; 37 5.3; 41 4.8; 45 4.4; 49 4.2; 54 3.9; 60 3.7; 66 3.4; 72 3.2; 79 3.1; 87 2.9; 96 2.9; 106 2.7; 116 2.5; 128 2.3; 141 2.1; 155 1.9; 170 1.7; 187 1.6; 206 1.6; 227 1.6; 249 1.4; 274 1.2; 302 1.0; 332 0.8; 365 0.8; 402 0.6; 442 0.2; 486 0.4; 535 1.2; 588 1.6; 647 0.4; 712 0.8; 783 2.3; 861 2.1; 947 0.5; 1042 -0.2; 1146 -0.1; 1261 0.9; 1387 2.4; 1526 4.0; 1678 5.6; 1846 6.0; 2031 6.0; 2234 6.0; 2457 6.0; 2703 6.0; 2973 6.0; 3270 6.0; 3597 6.0; 3957 6.0; 4353 6.0; 4788 6.0; 5267 6.0; 5793 6.0; 6373 5.5; 7010 2.5; 7711 0.3; 8482 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AKG K44 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K44 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.48 | 6.0 dB  |
| Peaking | 126 Hz  | 0.59 | 1.5 dB  |
| Peaking | 579 Hz  | 3.21 | 0.6 dB  |
| Peaking | 2314 Hz | 1.13 | 6.0 dB  |
| Peaking | 4990 Hz | 1.6  | 5.4 dB  |
| Peaking | 833 Hz  | 5.26 | 2.7 dB  |
| Peaking | 1072 Hz | 1.87 | -2.2 dB |
| Peaking | 1664 Hz | 4.49 | 2.1 dB  |
| Peaking | 6414 Hz | 4.58 | 3.4 dB  |
| Peaking | 7573 Hz | 1.79 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/AKG%20K44/AKG%20K44.png)