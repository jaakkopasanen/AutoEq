# Noble Audio K10
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -3.8; 25 -4.1; 28 -4.5; 31 -4.9; 34 -5.1; 37 -5.3; 41 -5.6; 45 -5.9; 49 -6.1; 54 -6.4; 60 -6.6; 66 -7.0; 72 -7.3; 79 -7.7; 87 -8.0; 96 -8.4; 106 -8.7; 116 -9.0; 128 -9.2; 141 -9.3; 155 -9.5; 170 -9.4; 187 -9.4; 206 -9.2; 227 -9.1; 249 -8.9; 274 -8.6; 302 -8.3; 332 -8.0; 365 -7.7; 402 -7.4; 442 -7.0; 486 -6.7; 535 -6.3; 588 -6.0; 647 -5.6; 712 -5.2; 783 -4.9; 861 -4.7; 947 -4.8; 1042 -5.3; 1146 -6.3; 1261 -7.4; 1387 -8.0; 1526 -8.1; 1678 -7.6; 1846 -6.9; 2031 -6.2; 2234 -5.9; 2457 -5.7; 2703 -5.3; 2973 -4.6; 3270 -3.6; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -3.3; 5793 -3.6; 6373 -7.8; 7010 -8.9; 7711 -11.3; 8482 -10.7; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.9; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio K10 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio K10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 12 Hz    |  0.45 | 3.8 dB  |
| Peaking | 156 Hz   |  0.64 | -3.1 dB |
| Peaking | 791 Hz   |  2.67 | 2.2 dB  |
| Peaking | 4284 Hz  |  2.03 | 7.0 dB  |
| Peaking | 7785 Hz  |  3.51 | -6.1 dB |
| Peaking | 1005 Hz  |  4.52 | 1.2 dB  |
| Peaking | 1460 Hz  |  2.63 | -2.1 dB |
| Peaking | 3642 Hz  | 12.35 | 1.2 dB  |
| Peaking | 9595 Hz  |  8.71 | 1.2 dB  |
| Peaking | 18414 Hz |  2.63 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.3 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Audio%20K10/Noble%20Audio%20K10.png)