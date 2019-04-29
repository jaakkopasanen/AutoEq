# Sony IER-Z1R sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.3; 25 -6.6; 28 -6.9; 31 -7.2; 34 -7.4; 37 -7.5; 41 -7.7; 45 -7.8; 49 -7.9; 54 -8.1; 60 -8.2; 66 -8.4; 72 -8.5; 79 -8.7; 87 -8.8; 96 -8.9; 106 -9.1; 116 -9.1; 128 -9.0; 141 -8.9; 155 -8.7; 170 -8.5; 187 -8.2; 206 -7.8; 227 -7.4; 249 -7.1; 274 -6.7; 302 -6.4; 332 -6.1; 365 -5.9; 402 -5.8; 442 -5.7; 486 -5.7; 535 -5.6; 588 -5.6; 647 -5.5; 712 -5.4; 783 -5.1; 861 -5.0; 947 -5.4; 1042 -5.7; 1146 -6.4; 1261 -7.1; 1387 -7.6; 1526 -7.4; 1678 -6.8; 1846 -5.8; 2031 -4.7; 2234 -3.4; 2457 -1.8; 2703 -0.5; 2973 -1.7; 3270 -4.9; 3597 -7.1; 3957 -7.1; 4353 -6.5; 4788 -4.7; 5267 -4.0; 5793 -6.7; 6373 -8.3; 7010 -6.3; 7711 -7.2; 8482 -7.6; 9330 -6.2; 10263 -6.2; 11289 -6.2; 12418 -6.2; 13660 -6.2; 15026 -6.6; 16529 -11.8; 18182 -13.4; 20000 -6.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 70 Hz    | 0.79 | -2.1 dB |
| Peaking | 140 Hz   | 1.48 | -2.1 dB |
| Peaking | 2671 Hz  | 4.08 | 6.3 dB  |
| Peaking | 17699 Hz | 1.83 | -8.8 dB |
| Peaking | 19889 Hz | 2.41 | 1.0 dB  |
| Peaking | 1335 Hz  | 0.65 | 2.9 dB  |
| Peaking | 1418 Hz  | 1.67 | -4.5 dB |
| Peaking | 3817 Hz  | 3.53 | -2.6 dB |
| Peaking | 5300 Hz  | 3.83 | 4.3 dB  |
| Peaking | 5996 Hz  | 3.35 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | 1.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | -4.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20IER-Z1R%20sample%202/Sony%20IER-Z1R%20sample%202.png)