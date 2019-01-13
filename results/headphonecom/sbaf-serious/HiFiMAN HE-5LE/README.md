# HiFiMAN HE-5LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 21 0.0; 23 1.2; 25 0.9; 28 0.7; 31 0.8; 34 0.9; 37 1.0; 41 1.1; 45 1.1; 49 1.0; 54 1.0; 60 1.0; 66 1.0; 72 0.7; 79 0.5; 87 0.5; 96 0.1; 106 -0.1; 116 -0.4; 128 -0.9; 141 -1.7; 155 -2.5; 170 -3.0; 187 -3.3; 206 -3.3; 227 -3.5; 249 -3.7; 274 -3.6; 302 -3.6; 332 -3.5; 365 -3.4; 402 -3.5; 442 -3.4; 486 -3.6; 535 -4.6; 588 -3.6; 647 -0.2; 712 1.1; 783 1.4; 861 0.5; 947 -0.1; 1042 0.4; 1146 2.0; 1261 2.5; 1387 3.1; 1526 3.1; 1678 3.7; 1846 4.6; 2031 3.7; 2234 2.1; 2457 3.4; 2703 3.5; 2973 1.6; 3270 1.7; 3597 3.1; 3957 0.7; 4353 -2.7; 4788 -3.5; 5267 0.0; 5793 -1.3; 6373 -4.1; 7010 -3.2; 7711 -3.7; 8482 -6.3; 9330 -7.0; 10263 -2.1; 11289 0.0; 12418 0.0; 13660 0.0; 15026 -0.4; 16529 -1.3; 18182 -1.9; 20000 -2.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.
Set volume attenuation in the Connection tab for both channels to **-47**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 343 Hz   |  0.69 | -4.4 dB |
| Peaking | 1774 Hz  |  0.78 | 4.2 dB  |
| Peaking | 3757 Hz  |  4.94 | 3.7 dB  |
| Peaking | 4420 Hz  |  3.19 | -4.9 dB |
| Peaking | 8693 Hz  |  2.73 | -7.3 dB |
| Peaking | 46 Hz    |  0.79 | 1.4 dB  |
| Peaking | 552 Hz   |  6.43 | -3.0 dB |
| Peaking | 704 Hz   |  5.05 | 2.6 dB  |
| Peaking | 6422 Hz  | 10.61 | -2.8 dB |
| Peaking | 18931 Hz |  1.89 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)