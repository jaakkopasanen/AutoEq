# SIA complimentary earphones
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.4; 25 -9.6; 28 -9.7; 31 -9.9; 34 -10.0; 37 -10.1; 41 -10.3; 45 -10.5; 49 -10.7; 54 -10.9; 60 -11.2; 66 -11.6; 72 -12.1; 79 -12.5; 87 -13.0; 96 -13.7; 106 -14.2; 116 -14.8; 128 -15.4; 141 -15.9; 155 -16.5; 170 -17.1; 187 -17.7; 206 -18.2; 227 -18.7; 249 -19.4; 274 -20.0; 302 -20.4; 332 -20.1; 365 -19.0; 402 -17.2; 442 -14.1; 486 -11.1; 535 -8.5; 588 -6.3; 647 -4.2; 712 -2.0; 783 -1.2; 861 -3.3; 947 -5.8; 1042 -7.9; 1146 -10.8; 1261 -15.4; 1387 -18.7; 1526 -15.6; 1678 -9.7; 1846 -4.8; 2031 -0.8; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -3.9; 5793 -1.4; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.2; 16529 -13.4; 18182 -13.0; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`SIA complimentary earphones GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SIA complimentary earphones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 337 Hz   | 0.41 | -24.8 dB |
| Peaking | 723 Hz   | 0.55 | 24.2 dB  |
| Peaking | 1400 Hz  | 1.42 | -28.0 dB |
| Peaking | 2169 Hz  | 0.59 | 13.6 dB  |
| Peaking | 17652 Hz | 1.32 | -8.2 dB  |
| Peaking | 24 Hz    | 1.9  | -1.6 dB  |
| Peaking | 2033 Hz  | 4.68 | 3.9 dB   |
| Peaking | 2105 Hz  | 1.9  | -2.2 dB  |
| Peaking | 6327 Hz  | 5.93 | 3.5 dB   |
| Peaking | 8030 Hz  | 2.82 | -2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB  |
| Peaking | 250 Hz   | 1.41 | -15.0 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 8.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB   |
| Peaking | 16000 Hz | 1.41 | -5.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/SIA%20complimentary%20earphones/SIA%20complimentary%20earphones.png)