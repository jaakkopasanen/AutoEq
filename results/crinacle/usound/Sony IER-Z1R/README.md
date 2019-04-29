# Sony IER-Z1R
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.7; 23 -7.0; 25 -7.3; 28 -7.6; 31 -7.8; 34 -8.0; 37 -8.1; 41 -8.3; 45 -8.4; 49 -8.5; 54 -8.6; 60 -8.7; 66 -8.9; 72 -9.0; 79 -9.2; 87 -9.3; 96 -9.4; 106 -9.5; 116 -9.5; 128 -9.4; 141 -9.3; 155 -9.1; 170 -8.8; 187 -8.5; 206 -8.1; 227 -7.7; 249 -7.4; 274 -7.0; 302 -6.7; 332 -6.4; 365 -6.3; 402 -6.1; 442 -6.1; 486 -6.0; 535 -6.0; 588 -5.9; 647 -5.8; 712 -5.7; 783 -5.6; 861 -5.4; 947 -5.6; 1042 -5.9; 1146 -6.6; 1261 -7.3; 1387 -7.7; 1526 -7.6; 1678 -7.0; 1846 -6.1; 2031 -5.0; 2234 -3.9; 2457 -2.1; 2703 -0.5; 2973 -1.6; 3270 -4.9; 3597 -6.7; 3957 -6.4; 4353 -5.9; 4788 -4.1; 5267 -3.3; 5793 -5.4; 6373 -7.0; 7010 -4.8; 7711 -6.0; 8482 -7.2; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.5; 13660 -6.3; 15026 -7.3; 16529 -11.3; 18182 -12.6; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 60 Hz    | 0.62 | -2.3 dB |
| Peaking | 137 Hz   | 1.2  | -2.3 dB |
| Peaking | 2707 Hz  | 4.07 | 6.3 dB  |
| Peaking | 14320 Hz | 1.34 | 1.6 dB  |
| Peaking | 17626 Hz | 1.35 | -7.6 dB |
| Peaking | 1092 Hz  | 0.84 | 1.7 dB  |
| Peaking | 1415 Hz  | 1.75 | -3.2 dB |
| Peaking | 2147 Hz  | 3.45 | 0.9 dB  |
| Peaking | 3659 Hz  | 5.56 | -1.7 dB |
| Peaking | 5102 Hz  | 6.27 | 3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20IER-Z1R/Sony%20IER-Z1R.png)