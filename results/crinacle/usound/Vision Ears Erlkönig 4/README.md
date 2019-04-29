# Vision Ears Erlkönig 4
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -1.0; 25 -1.5; 28 -2.0; 31 -2.4; 34 -2.8; 37 -3.2; 41 -3.6; 45 -4.1; 49 -4.5; 54 -4.9; 60 -5.4; 66 -5.9; 72 -6.3; 79 -6.7; 87 -7.3; 96 -7.8; 106 -8.3; 116 -8.8; 128 -9.1; 141 -9.4; 155 -9.6; 170 -9.8; 187 -9.9; 206 -10.0; 227 -10.0; 249 -9.8; 274 -9.7; 302 -9.6; 332 -9.4; 365 -9.1; 402 -8.9; 442 -8.5; 486 -8.2; 535 -7.9; 588 -7.5; 647 -7.0; 712 -6.5; 783 -5.9; 861 -5.5; 947 -5.2; 1042 -5.4; 1146 -5.9; 1261 -6.5; 1387 -6.8; 1526 -6.5; 1678 -6.0; 1846 -5.5; 2031 -5.5; 2234 -5.8; 2457 -6.1; 2703 -6.1; 2973 -5.4; 3270 -5.4; 3597 -5.5; 3957 -4.9; 4353 -4.6; 4788 -4.5; 5267 -3.9; 5793 -2.9; 6373 -2.6; 7010 -4.2; 7711 -6.4; 8482 -6.7; 9330 -6.7; 10263 -6.7; 11289 -6.7; 12418 -6.7; 13660 -6.7; 15026 -6.7; 16529 -6.7; 18182 -6.7; 20000 -6.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Vision Ears Erlkönig 4 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Vision Ears Erlkönig 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.45 | 6.9 dB  |
| Peaking | 63 Hz   | 0.86 | 1.2 dB  |
| Peaking | 252 Hz  | 0.31 | -4.2 dB |
| Peaking | 816 Hz  | 0.56 | 2.9 dB  |
| Peaking | 5778 Hz | 2.1  | 4.0 dB  |
| Peaking | 971 Hz  | 2    | 1.9 dB  |
| Peaking | 1388 Hz | 0.92 | -2.2 dB |
| Peaking | 1889 Hz | 2.7  | 1.8 dB  |
| Peaking | 3338 Hz | 1.89 | 0.9 dB  |
| Peaking | 8324 Hz | 4.21 | -1.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 0.7 dB  |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Vision%20Ears%20Erlk%C3%B6nig%204/Vision%20Ears%20Erlk%C3%B6nig%204.png)