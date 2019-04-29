# Sony MH755 sample 3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.7; 23 -10.4; 25 -10.1; 28 -9.7; 31 -9.3; 34 -8.9; 37 -8.6; 41 -8.1; 45 -7.6; 49 -7.3; 54 -7.0; 60 -6.5; 66 -6.2; 72 -6.0; 79 -5.8; 87 -5.5; 96 -5.4; 106 -5.3; 116 -5.1; 128 -5.0; 141 -4.8; 155 -4.6; 170 -4.4; 187 -4.1; 206 -3.9; 227 -3.6; 249 -3.4; 274 -3.1; 302 -2.8; 332 -2.6; 365 -2.4; 402 -2.2; 442 -2.0; 486 -1.8; 535 -1.6; 588 -1.4; 647 -1.2; 712 -0.9; 783 -0.7; 861 -0.5; 947 -0.5; 1042 -0.9; 1146 -1.8; 1261 -2.6; 1387 -3.2; 1526 -3.3; 1678 -3.1; 1846 -2.8; 2031 -2.8; 2234 -3.0; 2457 -3.5; 2703 -4.8; 2973 -5.6; 3270 -5.5; 3597 -4.9; 3957 -3.9; 4353 -2.8; 4788 -1.9; 5267 -1.3; 5793 -0.7; 6373 -0.7; 7010 -2.2; 7711 -3.8; 8482 -2.8; 9330 -2.7; 10263 -2.7; 11289 -2.7; 12418 -2.7; 13660 -4.7; 15026 -5.2; 16529 -3.2; 18182 -3.6; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony MH755 sample 3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MH755 sample 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.65 | -7.3 dB |
| Peaking | 82 Hz    | 0.47 | -1.9 dB |
| Peaking | 747 Hz   | 1.21 | 2.3 dB  |
| Peaking | 3161 Hz  | 2.36 | -3.2 dB |
| Peaking | 5740 Hz  | 3.34 | 2.5 dB  |
| Peaking | 1017 Hz  | 3.21 | 1.4 dB  |
| Peaking | 1449 Hz  | 1.23 | -1.3 dB |
| Peaking | 2031 Hz  | 2.4  | 1.0 dB  |
| Peaking | 4655 Hz  | 4.61 | 0.4 dB  |
| Peaking | 14658 Hz | 3.26 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -7.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.8 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB |
| Peaking | 8000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 16000 Hz | 1.41 | -2.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20MH755%20sample%203/Sony%20MH755%20sample%203.png)