# Sony IER-M7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.2; 25 -6.5; 28 -6.8; 31 -7.1; 34 -7.2; 37 -7.4; 41 -7.5; 45 -7.6; 49 -7.8; 54 -7.9; 60 -8.1; 66 -8.3; 72 -8.5; 79 -8.7; 87 -8.9; 96 -9.2; 106 -9.4; 116 -9.5; 128 -9.6; 141 -9.7; 155 -9.7; 170 -9.6; 187 -9.5; 206 -9.4; 227 -9.2; 249 -9.0; 274 -8.8; 302 -8.6; 332 -8.4; 365 -8.1; 402 -7.9; 442 -7.7; 486 -7.4; 535 -7.1; 588 -6.8; 647 -6.4; 712 -6.0; 783 -5.6; 861 -5.2; 947 -5.1; 1042 -5.3; 1146 -6.0; 1261 -6.6; 1387 -6.9; 1526 -6.7; 1678 -6.2; 1846 -5.7; 2031 -5.3; 2234 -5.0; 2457 -4.5; 2703 -3.5; 2973 -2.4; 3270 -3.6; 3597 -5.1; 3957 -3.3; 4353 -2.4; 4788 -3.2; 5267 -2.6; 5793 -1.1; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -8.3; 13660 -7.8; 15026 -7.1; 16529 -9.5; 18182 -7.7; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-M7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-M7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 115 Hz   | 0.49 | -3.2 dB |
| Peaking | 264 Hz   | 0.91 | -1.4 dB |
| Peaking | 2932 Hz  | 3.26 | 3.0 dB  |
| Peaking | 5904 Hz  | 2.27 | 5.3 dB  |
| Peaking | 16331 Hz | 0.77 | -2.9 dB |
| Peaking | 919 Hz   | 2.99 | 1.3 dB  |
| Peaking | 1399 Hz  | 3.55 | -1.2 dB |
| Peaking | 3570 Hz  | 9.75 | -1.3 dB |
| Peaking | 4185 Hz  | 7.94 | 2.1 dB  |
| Peaking | 7756 Hz  | 7.36 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB |
| Peaking | 4000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20IER-M7/Sony%20IER-M7.png)