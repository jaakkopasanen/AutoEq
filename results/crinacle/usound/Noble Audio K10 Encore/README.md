# Noble Audio K10 Encore
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.4; 23 -2.8; 25 -3.1; 28 -3.6; 31 -3.9; 34 -4.2; 37 -4.4; 41 -4.7; 45 -4.9; 49 -5.2; 54 -5.4; 60 -5.8; 66 -6.1; 72 -6.5; 79 -6.9; 87 -7.3; 96 -7.7; 106 -8.1; 116 -8.4; 128 -8.7; 141 -9.0; 155 -9.1; 170 -9.2; 187 -9.2; 206 -9.2; 227 -9.1; 249 -8.9; 274 -8.7; 302 -8.5; 332 -8.3; 365 -8.0; 402 -7.7; 442 -7.4; 486 -7.2; 535 -6.8; 588 -6.5; 647 -6.2; 712 -5.8; 783 -5.3; 861 -5.0; 947 -4.8; 1042 -5.1; 1146 -5.7; 1261 -6.3; 1387 -6.6; 1526 -6.4; 1678 -5.8; 1846 -5.3; 2031 -5.1; 2234 -5.2; 2457 -5.5; 2703 -5.1; 2973 -3.8; 3270 -2.7; 3597 -1.2; 3957 -0.5; 4353 -0.5; 4788 -1.7; 5267 -4.7; 5793 -8.5; 6373 -10.3; 7010 -11.4; 7711 -12.4; 8482 -8.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.8; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio K10 Encore GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio K10 Encore ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.3  | 4.4 dB  |
| Peaking | 179 Hz  | 0.61 | -3.0 dB |
| Peaking | 873 Hz  | 2.13 | 1.9 dB  |
| Peaking | 4165 Hz | 1.73 | 7.3 dB  |
| Peaking | 6943 Hz | 2.31 | -7.2 dB |
| Peaking | 1469 Hz | 3.11 | -1.4 dB |
| Peaking | 1740 Hz | 1.44 | 1.0 dB  |
| Peaking | 2555 Hz | 5.64 | -1.0 dB |
| Peaking | 7934 Hz | 7.32 | -3.2 dB |
| Peaking | 8807 Hz | 2.96 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.4 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -2.4 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.6 dB |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -5.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Noble%20Audio%20K10%20Encore/Noble%20Audio%20K10%20Encore.png)