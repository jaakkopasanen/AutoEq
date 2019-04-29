# Vision Ears Erlkönig 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.2; 25 -8.4; 28 -8.7; 31 -8.8; 34 -9.0; 37 -9.1; 41 -9.2; 45 -9.4; 49 -9.6; 54 -9.8; 60 -9.9; 66 -10.1; 72 -10.3; 79 -10.5; 87 -10.8; 96 -11.0; 106 -11.2; 116 -11.4; 128 -11.4; 141 -11.4; 155 -11.3; 170 -11.1; 187 -10.9; 206 -10.7; 227 -10.3; 249 -9.8; 274 -9.4; 302 -8.9; 332 -8.4; 365 -7.8; 402 -7.2; 442 -6.6; 486 -6.0; 535 -5.4; 588 -4.7; 647 -4.0; 712 -3.3; 783 -2.7; 861 -2.1; 947 -1.9; 1042 -2.0; 1146 -2.6; 1261 -3.2; 1387 -3.5; 1526 -3.3; 1678 -2.8; 1846 -2.3; 2031 -2.3; 2234 -2.7; 2457 -3.1; 2703 -3.0; 2973 -2.1; 3270 -2.2; 3597 -2.6; 3957 -2.4; 4353 -2.0; 4788 -1.8; 5267 -1.3; 5793 -0.5; 6373 -0.8; 7010 -2.7; 7711 -4.7; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.0; 13660 -5.0; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears Erlkönig 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears Erlkönig 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.27 | -3.5 dB |
| Peaking | 216 Hz  | 0.44 | -5.3 dB |
| Peaking | 927 Hz  | 0.32 | 3.6 dB  |
| Peaking | 5657 Hz | 2.3  | 4.0 dB  |
| Peaking | 921 Hz  | 3.29 | 1.2 dB  |
| Peaking | 1386 Hz | 3.41 | -1.4 dB |
| Peaking | 3250 Hz | 4.02 | 0.9 dB  |
| Peaking | 7909 Hz | 7.38 | -1.1 dB |
| Peaking | 9652 Hz | 2.9  | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.4 dB |
| Peaking | 62 Hz    | 1.41 | -3.6 dB |
| Peaking | 125 Hz   | 1.41 | -5.5 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vision%20Ears%20Erlk%C3%B6nig%201/Vision%20Ears%20Erlk%C3%B6nig%201.png)