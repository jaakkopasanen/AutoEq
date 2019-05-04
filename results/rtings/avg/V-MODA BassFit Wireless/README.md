# V-MODA BassFit Wireless
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.7; 23 -7.9; 25 -8.1; 28 -8.4; 31 -8.7; 34 -9.0; 37 -9.2; 41 -9.4; 45 -9.5; 49 -9.6; 54 -9.5; 60 -9.3; 66 -9.2; 72 -8.9; 79 -8.7; 87 -8.3; 96 -8.0; 106 -8.0; 116 -7.9; 128 -7.5; 141 -7.0; 155 -6.5; 170 -6.0; 187 -5.3; 206 -4.6; 227 -3.9; 249 -3.4; 274 -3.0; 302 -2.9; 332 -2.8; 365 -2.7; 402 -2.6; 442 -2.4; 486 -2.2; 535 -1.9; 588 -1.8; 647 -1.6; 712 -1.3; 783 -0.8; 861 -0.5; 947 -0.6; 1042 -1.0; 1146 -1.3; 1261 -1.3; 1387 -1.3; 1526 -1.1; 1678 -1.0; 1846 -1.0; 2031 -1.2; 2234 -1.2; 2457 -1.0; 2703 -1.0; 2973 -1.5; 3270 -2.4; 3597 -3.2; 3957 -4.0; 4353 -5.5; 4788 -7.9; 5267 -9.0; 5793 -6.8; 6373 -3.9; 7010 -3.9; 7711 -3.7; 8482 -3.0; 9330 -3.1; 10263 -3.1; 11289 -3.1; 12418 -3.1; 13660 -3.1; 15026 -3.6; 16529 -5.4; 18182 -7.5; 20000 -4.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`V-MODA BassFit Wireless GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-MODA BassFit Wireless ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.56 | -3.9 dB |
| Peaking | 95 Hz    | 0.44 | -5.1 dB |
| Peaking | 956 Hz   | 0.13 | 2.3 dB  |
| Peaking | 5110 Hz  | 2.58 | -7.6 dB |
| Peaking | 18430 Hz | 1.2  | -4.9 dB |
| Peaking | 255 Hz   | 3.37 | 0.7 dB  |
| Peaking | 444 Hz   | 2.68 | -0.5 dB |
| Peaking | 13398 Hz | 3.52 | 0.2 dB  |
| Peaking | 14427 Hz | 3.9  | 0.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/V-MODA%20BassFit%20Wireless/V-MODA%20BassFit%20Wireless.png)