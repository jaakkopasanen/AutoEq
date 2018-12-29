# Sennheiser RS 180
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 21 0.0; 23 2.0; 25 1.3; 28 0.5; 31 -0.2; 34 -0.8; 37 -1.3; 41 -1.8; 45 -2.3; 49 -2.7; 54 -2.9; 60 -3.1; 66 -4.0; 72 -4.3; 79 -4.3; 87 -4.8; 96 -5.1; 106 -5.4; 116 -5.3; 128 -5.4; 141 -5.6; 155 -5.7; 170 -5.7; 187 -5.8; 206 -5.5; 227 -4.9; 249 -4.6; 274 -4.5; 302 -4.0; 332 -3.6; 365 -3.3; 402 -3.0; 442 -2.7; 486 -2.3; 535 -2.0; 588 -1.8; 647 -1.4; 712 -1.4; 783 -0.5; 861 0.7; 947 0.2; 1042 0.1; 1146 0.4; 1261 0.7; 1387 1.0; 1526 -0.7; 1678 -3.0; 1846 -4.8; 2031 -5.9; 2234 -6.1; 2457 -4.3; 2703 -1.3; 2973 2.3; 3270 -2.3; 3597 1.9; 3957 1.1; 4353 -0.2; 4788 -5.2; 5267 -4.1; 5793 -2.1; 6373 -3.0; 7010 2.2; 7711 -1.7; 8482 -7.1; 9330 -8.3; 10263 -2.8; 11289 0.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sennheiser RS 180 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 84 Hz    |  0.9  | -3.0 dB |
| Peaking | 199 Hz   |  0.66 | -4.9 dB |
| Peaking | 2107 Hz  |  3.68 | -6.8 dB |
| Peaking | 9055 Hz  |  4.7  | -9.6 dB |
| Peaking | 24000 Hz |  2.11 | -5.8 dB |
| Peaking | 20 Hz    |  2.48 | 3.2 dB  |
| Peaking | 1265 Hz  |  3.74 | 1.8 dB  |
| Peaking | 4158 Hz  |  2.77 | 5.4 dB  |
| Peaking | 4830 Hz  |  2.88 | -7.7 dB |
| Peaking | 7040 Hz  | 10.3  | 4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20180/Sennheiser%20RS%20180.png)