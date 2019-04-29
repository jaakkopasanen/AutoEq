# StereoPravda SB7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -1.1; 106 -1.8; 116 -2.8; 128 -3.4; 141 -3.6; 155 -4.0; 170 -4.6; 187 -4.9; 206 -5.2; 227 -5.3; 249 -5.4; 274 -5.6; 302 -5.8; 332 -5.9; 365 -6.0; 402 -6.0; 442 -6.1; 486 -6.1; 535 -6.1; 588 -6.1; 647 -6.0; 712 -5.9; 783 -5.8; 861 -5.7; 947 -5.8; 1042 -6.1; 1146 -6.7; 1261 -7.3; 1387 -7.9; 1526 -8.0; 1678 -8.2; 1846 -9.2; 2031 -10.6; 2234 -11.5; 2457 -11.4; 2703 -10.7; 2973 -9.6; 3270 -7.0; 3597 -4.3; 3957 -3.4; 4353 -3.5; 4788 -4.7; 5267 -7.9; 5793 -12.1; 6373 -10.5; 7010 -6.6; 7711 -6.2; 8482 -7.7; 9330 -8.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`StereoPravda SB7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `StereoPravda SB7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 43 Hz   |  0.36 | 6.6 dB  |
| Peaking | 2479 Hz |  1.69 | -6.3 dB |
| Peaking | 4072 Hz |  1.92 | 5.4 dB  |
| Peaking | 5890 Hz |  4.9  | -7.4 dB |
| Peaking | 17 Hz   |  1.21 | 2.0 dB  |
| Peaking | 57 Hz   |  0.29 | -1.1 dB |
| Peaking | 87 Hz   |  1.81 | 1.9 dB  |
| Peaking | 855 Hz  |  2.59 | 1.1 dB  |
| Peaking | 9042 Hz | 10.19 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.4 dB  |
| Peaking | 125 Hz   | 1.41 | 2.7 dB  |
| Peaking | 250 Hz   | 1.41 | 0.2 dB  |
| Peaking | 500 Hz   | 1.41 | 0.1 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/StereoPravda%20SB7/StereoPravda%20SB7.png)