# Kinera Idun sample 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.2; 23 -3.4; 25 -3.6; 28 -3.8; 31 -3.9; 34 -4.1; 37 -4.2; 41 -4.4; 45 -4.6; 49 -4.8; 54 -5.0; 60 -5.2; 66 -5.5; 72 -5.8; 79 -6.2; 87 -6.5; 96 -6.9; 106 -7.3; 116 -7.6; 128 -8.0; 141 -8.3; 155 -8.4; 170 -8.6; 187 -8.6; 206 -8.6; 227 -8.6; 249 -8.4; 274 -8.3; 302 -8.0; 332 -7.6; 365 -7.2; 402 -6.7; 442 -6.3; 486 -6.1; 535 -5.8; 588 -5.6; 647 -5.5; 712 -5.5; 783 -5.6; 861 -6.0; 947 -7.0; 1042 -8.3; 1146 -8.9; 1261 -8.9; 1387 -8.1; 1526 -6.8; 1678 -5.4; 1846 -4.0; 2031 -2.6; 2234 -1.5; 2457 -1.1; 2703 -1.5; 2973 -2.3; 3270 -2.4; 3597 -1.2; 3957 -0.6; 4353 -0.5; 4788 -0.5; 5267 -2.4; 5793 -4.3; 6373 -3.5; 7010 -3.7; 7711 -5.9; 8482 -5.7; 9330 -5.5; 10263 -5.5; 11289 -5.8; 12418 -9.2; 13660 -16.2; 15026 -23.5; 16529 -22.7; 18182 -17.7; 20000 -21.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera Idun sample 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera Idun sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 217 Hz   | 0.74 | -3.6 dB  |
| Peaking | 1256 Hz  | 1.31 | -8.4 dB  |
| Peaking | 7091 Hz  | 0.17 | 15.1 dB  |
| Peaking | 11883 Hz | 1.51 | 9.0 dB   |
| Peaking | 15082 Hz | 0.36 | -32.0 dB |
| Peaking | 22 Hz    | 1.27 | 2.3 dB   |
| Peaking | 42 Hz    | 1.89 | 0.8 dB   |
| Peaking | 4518 Hz  | 2.87 | 4.8 dB   |
| Peaking | 4569 Hz  | 1.51 | -3.2 dB  |
| Peaking | 13498 Hz | 3.86 | 0.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB   |
| Peaking | 62 Hz    | 1.41 | 0.3 dB   |
| Peaking | 125 Hz   | 1.41 | -2.2 dB  |
| Peaking | 250 Hz   | 1.41 | -3.1 dB  |
| Peaking | 500 Hz   | 1.41 | 1.2 dB   |
| Peaking | 1000 Hz  | 1.41 | -3.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.1 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.9 dB   |
| Peaking | 16000 Hz | 1.41 | -22.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kinera%20Idun%20sample%202/Kinera%20Idun%20sample%202.png)