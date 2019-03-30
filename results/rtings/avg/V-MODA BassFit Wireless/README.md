# V-MODA BassFit Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.5; 25 -3.7; 28 -4.0; 31 -4.3; 34 -4.5; 37 -4.7; 41 -4.9; 45 -5.0; 49 -5.1; 54 -5.1; 60 -5.3; 66 -5.4; 72 -5.3; 79 -5.3; 87 -5.2; 96 -5.3; 106 -5.7; 116 -6.0; 128 -6.1; 141 -6.1; 155 -5.9; 170 -5.7; 187 -5.4; 206 -4.9; 227 -4.3; 249 -3.8; 274 -3.5; 302 -3.3; 332 -3.2; 365 -3.1; 402 -3.0; 442 -2.8; 486 -2.5; 535 -2.2; 588 -2.1; 647 -1.9; 712 -1.5; 783 -1.1; 861 -0.8; 947 -0.9; 1042 -1.2; 1146 -1.5; 1261 -1.6; 1387 -1.5; 1526 -1.3; 1678 -1.1; 1846 -1.1; 2031 -1.2; 2234 -0.8; 2457 -0.5; 2703 -0.9; 2973 -1.9; 3270 -3.0; 3597 -3.8; 3957 -4.7; 4353 -6.3; 4788 -7.9; 5267 -9.0; 5793 -7.3; 6373 -5.2; 7010 -4.2; 7711 -3.3; 8482 -3.2; 9330 -3.2; 10263 -3.2; 11289 -3.2; 12418 -3.2; 13660 -3.3; 15026 -4.3; 16529 -5.9; 18182 -8.0; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA BassFit Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA BassFit Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 127 Hz   | 0.41 | -3.0 dB |
| Peaking | 921 Hz   | 0.29 | 2.2 dB  |
| Peaking | 2484 Hz  | 3.27 | 1.7 dB  |
| Peaking | 5045 Hz  | 2.54 | -6.5 dB |
| Peaking | 18493 Hz | 1.22 | -5.3 dB |
| Peaking | 50 Hz    | 1.14 | -0.7 dB |
| Peaking | 120 Hz   | 0.74 | 1.6 dB  |
| Peaking | 139 Hz   | 1.41 | -1.9 dB |
| Peaking | 1269 Hz  | 6.19 | -0.4 dB |
| Peaking | 10748 Hz | 1.22 | 0.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 4000 Hz  | 1.41 | -3.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20BassFit%20Wireless/V-MODA%20BassFit%20Wireless.png)