# HiFiMAN HE-5LE
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.4; 23 -3.8; 25 -4.1; 28 -4.3; 31 -4.3; 34 -4.2; 37 -4.0; 41 -3.9; 45 -3.9; 49 -4.0; 54 -4.1; 60 -4.1; 66 -4.0; 72 -4.3; 79 -4.5; 87 -4.6; 96 -5.0; 106 -5.2; 116 -5.4; 128 -6.0; 141 -6.7; 155 -7.5; 170 -8.1; 187 -8.3; 206 -8.3; 227 -8.5; 249 -8.7; 274 -8.7; 302 -8.6; 332 -8.5; 365 -8.5; 402 -8.6; 442 -8.5; 486 -8.7; 535 -9.7; 588 -8.6; 647 -5.2; 712 -3.9; 783 -3.6; 861 -4.6; 947 -5.1; 1042 -4.6; 1146 -3.1; 1261 -2.6; 1387 -1.9; 1526 -1.9; 1678 -1.3; 1846 -0.5; 2031 -1.4; 2234 -2.9; 2457 -1.6; 2703 -1.6; 2973 -3.4; 3270 -3.4; 3597 -2.0; 3957 -4.3; 4353 -7.8; 4788 -8.6; 5267 -5.0; 5793 -6.4; 6373 -9.2; 7010 -8.2; 7711 -8.8; 8482 -11.3; 9330 -12.1; 10263 -7.2; 11289 -5.1; 12418 -5.1; 13660 -5.1; 15026 -5.4; 16529 -6.3; 18182 -6.9; 20000 -7.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`HiFiMAN HE-5LE GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 343 Hz   |  0.69 | -4.4 dB |
| Peaking | 1772 Hz  |  0.78 | 4.2 dB  |
| Peaking | 3765 Hz  |  4.84 | 3.6 dB  |
| Peaking | 4426 Hz  |  3.25 | -4.9 dB |
| Peaking | 8705 Hz  |  2.6  | -7.3 dB |
| Peaking | 46 Hz    |  0.79 | 1.4 dB  |
| Peaking | 555 Hz   |  6.43 | -3.0 dB |
| Peaking | 706 Hz   |  5.05 | 2.6 dB  |
| Peaking | 6461 Hz  | 10.85 | -2.9 dB |
| Peaking | 19038 Hz |  1.23 | -2.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.5 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)