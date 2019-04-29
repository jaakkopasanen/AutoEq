# Sony MH755
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.4; 23 -9.2; 25 -9.0; 28 -8.7; 31 -8.5; 34 -8.2; 37 -7.9; 41 -7.6; 45 -7.2; 49 -6.9; 54 -6.6; 60 -6.3; 66 -6.0; 72 -5.8; 79 -5.7; 87 -5.5; 96 -5.4; 106 -5.3; 116 -5.1; 128 -5.0; 141 -4.9; 155 -4.7; 170 -4.4; 187 -4.2; 206 -3.9; 227 -3.6; 249 -3.4; 274 -3.1; 302 -2.9; 332 -2.6; 365 -2.4; 402 -2.2; 442 -2.0; 486 -1.8; 535 -1.6; 588 -1.4; 647 -1.2; 712 -0.9; 783 -0.7; 861 -0.5; 947 -0.5; 1042 -0.9; 1146 -1.8; 1261 -2.6; 1387 -3.1; 1526 -3.1; 1678 -2.9; 1846 -2.6; 2031 -2.6; 2234 -2.8; 2457 -3.3; 2703 -4.4; 2973 -5.2; 3270 -5.4; 3597 -4.9; 3957 -4.0; 4353 -3.1; 4788 -2.3; 5267 -1.8; 5793 -1.8; 6373 -2.6; 7010 -4.0; 7711 -3.3; 8482 -2.7; 9330 -2.7; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -3.2; 15026 -4.7; 16529 -4.4; 18182 -3.4; 20000 -2.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.31 | -6.7 dB |
| Peaking | 136 Hz   | 1.08 | -1.3 dB |
| Peaking | 767 Hz   | 1.3  | 2.3 dB  |
| Peaking | 3167 Hz  | 3.11 | -3.0 dB |
| Peaking | 15972 Hz | 1.92 | -2.2 dB |
| Peaking | 1000 Hz  | 5.58 | 0.7 dB  |
| Peaking | 1402 Hz  | 4.04 | -1.0 dB |
| Peaking | 5547 Hz  | 3.61 | 1.4 dB  |
| Peaking | 7123 Hz  | 7.09 | -1.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.9 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -1.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MH755/Sony%20MH755.png)