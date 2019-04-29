# FitEar MH334SR custom
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.6; 25 -4.1; 28 -4.7; 31 -5.1; 34 -5.4; 37 -5.7; 41 -6.1; 45 -6.4; 49 -6.8; 54 -7.1; 60 -7.4; 66 -7.8; 72 -8.2; 79 -8.6; 87 -9.0; 96 -9.4; 106 -9.8; 116 -10.2; 128 -10.5; 141 -10.7; 155 -10.8; 170 -11.0; 187 -11.1; 206 -11.1; 227 -11.0; 249 -10.8; 274 -10.7; 302 -10.5; 332 -10.2; 365 -9.9; 402 -9.6; 442 -9.2; 486 -8.8; 535 -8.3; 588 -7.9; 647 -7.3; 712 -6.7; 783 -6.1; 861 -5.5; 947 -5.2; 1042 -5.3; 1146 -5.8; 1261 -6.4; 1387 -6.7; 1526 -6.7; 1678 -6.2; 1846 -5.3; 2031 -4.2; 2234 -3.7; 2457 -3.5; 2703 -2.5; 2973 -1.7; 3270 -1.2; 3597 -1.0; 3957 -1.3; 4353 -0.5; 4788 -0.5; 5267 -1.7; 5793 -3.9; 6373 -2.6; 7010 -4.0; 7711 -6.2; 8482 -8.0; 9330 -9.8; 10263 -6.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar MH334SR custom GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar MH334SR custom ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.58 | 4.7 dB  |
| Peaking | 198 Hz  | 0.44 | -4.7 dB |
| Peaking | 879 Hz  | 2.76 | 2.0 dB  |
| Peaking | 4073 Hz | 0.91 | 6.2 dB  |
| Peaking | 9109 Hz | 4.24 | -4.9 dB |
| Peaking | 1554 Hz | 2.42 | -2.2 dB |
| Peaking | 1950 Hz | 0.84 | 1.2 dB  |
| Peaking | 2452 Hz | 7.18 | -0.7 dB |
| Peaking | 3891 Hz | 6.7  | -1.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/FitEar%20MH334SR%20custom/FitEar%20MH334SR%20custom.png)