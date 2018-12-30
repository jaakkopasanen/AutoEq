# HiFiMAN HE6
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 21 0.0; 23 2.8; 25 2.1; 28 1.5; 31 1.3; 34 1.2; 37 1.3; 41 1.5; 45 1.6; 49 1.7; 54 1.6; 60 1.4; 66 1.5; 72 1.3; 79 0.9; 87 0.8; 96 0.7; 106 0.7; 116 0.5; 128 0.3; 141 0.0; 155 -0.1; 170 -0.0; 187 -0.1; 206 -0.1; 227 -0.1; 249 -0.1; 274 -0.0; 302 0.3; 332 0.3; 365 0.5; 402 0.4; 442 0.3; 486 0.3; 535 0.3; 588 0.2; 647 0.5; 712 0.7; 783 0.5; 861 -0.2; 947 0.1; 1042 -0.1; 1146 1.0; 1261 0.8; 1387 1.0; 1526 0.6; 1678 1.5; 1846 3.2; 2031 3.2; 2234 1.7; 2457 2.6; 2703 2.0; 2973 -0.3; 3270 -0.2; 3597 -0.6; 3957 -0.6; 4353 -3.3; 4788 -1.4; 5267 3.9; 5793 -0.6; 6373 -4.6; 7010 -4.7; 7711 -3.6; 8482 -4.3; 9330 -4.3; 10263 -0.5; 11289 0.0; 12418 -1.3; 13660 -5.4; 15026 -5.9; 16529 -2.8; 18182 0.0; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE6 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-57**.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.1dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 2036 Hz  |  1.94 | 3.1 dB  |
| Peaking | 4357 Hz  | 10    | -3.3 dB |
| Peaking | 7683 Hz  |  2.32 | -4.8 dB |
| Peaking | 14849 Hz |  2.36 | -6.7 dB |
| Peaking | 17 Hz    |  1.94 | 4.4 dB  |
| Peaking | 56 Hz    |  1.13 | 1.5 dB  |
| Peaking | 5484 Hz  |  9.74 | 9.2 dB  |
| Peaking | 6078 Hz  |  4.72 | -4.0 dB |
| Peaking | 17986 Hz |  4.44 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE6/HiFiMAN%20HE6.png)