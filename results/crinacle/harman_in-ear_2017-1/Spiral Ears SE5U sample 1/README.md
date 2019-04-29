# Spiral Ears SE5U sample 1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.3; 28 -2.2; 31 -2.9; 34 -3.5; 37 -4.0; 41 -4.6; 45 -5.2; 49 -5.8; 54 -6.4; 60 -6.9; 66 -7.4; 72 -7.9; 79 -8.4; 87 -8.9; 96 -9.4; 106 -10.0; 116 -10.3; 128 -10.6; 141 -10.9; 155 -10.9; 170 -11.1; 187 -11.1; 206 -11.1; 227 -10.9; 249 -10.7; 274 -10.4; 302 -10.1; 332 -9.6; 365 -9.1; 402 -8.6; 442 -8.2; 486 -7.7; 535 -7.2; 588 -6.6; 647 -6.1; 712 -5.6; 783 -5.1; 861 -4.8; 947 -4.8; 1042 -5.2; 1146 -6.0; 1261 -7.0; 1387 -7.7; 1526 -8.6; 1678 -10.0; 1846 -12.3; 2031 -12.1; 2234 -8.5; 2457 -6.4; 2703 -5.5; 2973 -5.8; 3270 -2.6; 3597 -0.5; 3957 -0.5; 4353 -2.3; 4788 -4.2; 5267 -0.7; 5793 -0.6; 6373 -1.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -9.4; 10263 -9.0; 11289 -7.8; 12418 -12.2; 13660 -21.9; 15026 -30.3; 16529 -30.7; 18182 -22.3; 20000 -8.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Spiral Ears SE5U sample 1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spiral Ears SE5U sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 24 Hz    | 2.26 | 6.0 dB   |
| Peaking | 1924 Hz  | 2.89 | -8.1 dB  |
| Peaking | 5682 Hz  | 0.64 | 10.0 dB  |
| Peaking | 11659 Hz | 3    | 9.1 dB   |
| Peaking | 15708 Hz | 0.77 | -28.5 dB |
| Peaking | 187 Hz   | 0.64 | -4.9 dB  |
| Peaking | 844 Hz   | 1.96 | 2.4 dB   |
| Peaking | 3693 Hz  | 4.31 | 6.1 dB   |
| Peaking | 3783 Hz  | 1.93 | -3.5 dB  |
| Peaking | 19962 Hz | 3.32 | 5.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.0 dB   |
| Peaking | 62 Hz    | 1.41 | -1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -30.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Spiral%20Ears%20SE5U%20sample%201/Spiral%20Ears%20SE5U%20sample%201.png)