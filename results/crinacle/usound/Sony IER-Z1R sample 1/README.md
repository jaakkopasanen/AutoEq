# Sony IER-Z1R sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.8; 25 -8.0; 28 -8.3; 31 -8.5; 34 -8.6; 37 -8.7; 41 -8.9; 45 -9.0; 49 -9.1; 54 -9.2; 60 -9.3; 66 -9.4; 72 -9.5; 79 -9.6; 87 -9.7; 96 -9.8; 106 -9.9; 116 -9.9; 128 -9.8; 141 -9.7; 155 -9.4; 170 -9.1; 187 -8.8; 206 -8.5; 227 -8.1; 249 -7.7; 274 -7.3; 302 -7.0; 332 -6.8; 365 -6.6; 402 -6.5; 442 -6.4; 486 -6.4; 535 -6.3; 588 -6.3; 647 -6.2; 712 -6.1; 783 -6.0; 861 -5.8; 947 -5.9; 1042 -6.1; 1146 -6.7; 1261 -7.4; 1387 -7.9; 1526 -7.8; 1678 -7.2; 1846 -6.4; 2031 -5.4; 2234 -4.4; 2457 -2.5; 2703 -0.5; 2973 -1.6; 3270 -4.9; 3597 -6.3; 3957 -5.8; 4353 -5.2; 4788 -3.5; 5267 -2.6; 5793 -4.2; 6373 -5.7; 7010 -4.1; 7711 -6.0; 8482 -6.8; 9330 -6.4; 10263 -6.3; 11289 -6.4; 12418 -8.1; 13660 -8.1; 15026 -8.5; 16529 -10.8; 18182 -11.8; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony IER-Z1R sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony IER-Z1R sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 53 Hz    | 0.5  | -2.5 dB |
| Peaking | 135 Hz   | 1.02 | -2.4 dB |
| Peaking | 2726 Hz  | 4.71 | 6.4 dB  |
| Peaking | 5259 Hz  | 3.92 | 3.8 dB  |
| Peaking | 17595 Hz | 1.13 | -5.9 dB |
| Peaking | 959 Hz   | 2.87 | 0.5 dB  |
| Peaking | 1454 Hz  | 1.99 | -2.9 dB |
| Peaking | 2007 Hz  | 0.43 | 1.1 dB  |
| Peaking | 3649 Hz  | 3.55 | -1.7 dB |
| Peaking | 12724 Hz | 6.68 | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.4 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.9 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20IER-Z1R%20sample%201/Sony%20IER-Z1R%20sample%201.png)