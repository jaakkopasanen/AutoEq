# StereoPravda SB7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.6; 87 -1.4; 96 -2.2; 106 -2.9; 116 -3.9; 128 -4.5; 141 -4.7; 155 -5.1; 170 -5.7; 187 -6.0; 206 -6.3; 227 -6.5; 249 -6.6; 274 -6.8; 302 -6.9; 332 -6.8; 365 -6.8; 402 -6.9; 442 -6.9; 486 -6.9; 535 -6.8; 588 -6.8; 647 -6.7; 712 -6.6; 783 -6.5; 861 -6.4; 947 -6.6; 1042 -6.9; 1146 -7.4; 1261 -7.8; 1387 -8.0; 1526 -8.0; 1678 -8.1; 1846 -9.0; 2031 -10.1; 2234 -10.3; 2457 -9.7; 2703 -8.6; 2973 -7.3; 3270 -4.7; 3597 -2.3; 3957 -1.8; 4353 -2.3; 4788 -3.9; 5267 -7.0; 5793 -11.0; 6373 -9.0; 7010 -4.9; 7711 -6.2; 8482 -6.7; 9330 -8.9; 10263 -7.2; 11289 -6.5; 12418 -6.6; 13660 -11.6; 15026 -17.0; 16529 -14.9; 18182 -8.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`StereoPravda SB7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `StereoPravda SB7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.5  | 6.9 dB   |
| Peaking | 2574 Hz  | 1.12 | -7.7 dB  |
| Peaking | 3789 Hz  | 1.15 | 9.0 dB   |
| Peaking | 5818 Hz  | 5    | -7.6 dB  |
| Peaking | 15577 Hz | 2.02 | -11.9 dB |
| Peaking | 20 Hz    | 2.75 | 1.4 dB   |
| Peaking | 82 Hz    | 3.26 | 1.5 dB   |
| Peaking | 245 Hz   | 0.91 | -1.0 dB  |
| Peaking | 9364 Hz  | 8.08 | -2.6 dB  |
| Peaking | 12024 Hz | 4.43 | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.6 dB  |
| Peaking | 125 Hz   | 1.41 | 1.5 dB  |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -9.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/StereoPravda%20SB7/StereoPravda%20SB7.png)