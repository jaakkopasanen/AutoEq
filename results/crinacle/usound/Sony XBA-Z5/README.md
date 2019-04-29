# Sony XBA-Z5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.3; 25 -5.7; 28 -6.0; 31 -6.4; 34 -6.6; 37 -6.9; 41 -7.2; 45 -7.5; 49 -7.7; 54 -7.9; 60 -8.3; 66 -8.7; 72 -8.9; 79 -9.2; 87 -9.5; 96 -9.9; 106 -10.3; 116 -10.5; 128 -10.7; 141 -10.8; 155 -10.7; 170 -10.7; 187 -10.5; 206 -10.3; 227 -9.8; 249 -9.4; 274 -9.0; 302 -8.6; 332 -8.2; 365 -7.8; 402 -7.8; 442 -7.7; 486 -7.0; 535 -6.7; 588 -6.4; 647 -6.0; 712 -5.6; 783 -5.2; 861 -4.7; 947 -4.4; 1042 -4.7; 1146 -5.4; 1261 -6.1; 1387 -6.4; 1526 -6.1; 1678 -5.3; 1846 -4.2; 2031 -3.1; 2234 -2.3; 2457 -2.0; 2703 -2.0; 2973 -2.5; 3270 -3.0; 3597 -2.3; 3957 -2.8; 4353 -5.1; 4788 -6.5; 5267 -6.2; 5793 -3.2; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -6.1; 15026 -8.4; 16529 -7.9; 18182 -5.9; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-Z5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-Z5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 76 Hz    | 1.03 | -0.8 dB |
| Peaking | 156 Hz   | 0.6  | -4.7 dB |
| Peaking | 892 Hz   | 3.34 | 1.8 dB  |
| Peaking | 2707 Hz  | 1.66 | 4.3 dB  |
| Peaking | 6385 Hz  | 6.7  | 5.6 dB  |
| Peaking | 19 Hz    | 2.1  | 1.3 dB  |
| Peaking | 1418 Hz  | 5.43 | -1.3 dB |
| Peaking | 3819 Hz  | 6.66 | 2.1 dB  |
| Peaking | 4849 Hz  | 5.74 | -2.1 dB |
| Peaking | 15679 Hz | 2.94 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -2.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Sony%20XBA-Z5/Sony%20XBA-Z5.png)