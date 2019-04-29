# Kinera Odin
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.2; 25 -5.5; 28 -6.0; 31 -6.3; 34 -6.6; 37 -6.8; 41 -7.0; 45 -7.2; 49 -7.5; 54 -7.8; 60 -8.1; 66 -8.4; 72 -8.7; 79 -9.1; 87 -9.4; 96 -9.8; 106 -10.1; 116 -10.5; 128 -10.6; 141 -10.8; 155 -10.9; 170 -10.9; 187 -10.8; 206 -10.7; 227 -10.5; 249 -10.3; 274 -10.0; 302 -9.5; 332 -9.0; 365 -8.5; 402 -8.1; 442 -7.7; 486 -7.2; 535 -6.7; 588 -6.3; 647 -5.9; 712 -5.6; 783 -5.4; 861 -5.5; 947 -6.1; 1042 -7.3; 1146 -9.0; 1261 -10.6; 1387 -11.5; 1526 -11.3; 1678 -10.4; 1846 -9.0; 2031 -7.5; 2234 -5.7; 2457 -3.6; 2703 -1.2; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -3.9; 4788 -1.5; 5267 -0.5; 5793 -1.1; 6373 -3.7; 7010 -4.9; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -8.9; 15026 -12.7; 16529 -19.1; 18182 -23.8; 20000 -16.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kinera Odin GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kinera Odin ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 157 Hz   | 0.71 | -4.7 dB  |
| Peaking | 1530 Hz  | 2.4  | -6.2 dB  |
| Peaking | 3137 Hz  | 1.74 | 6.6 dB   |
| Peaking | 5505 Hz  | 2.56 | 5.3 dB   |
| Peaking | 18384 Hz | 1.09 | -19.3 dB |
| Peaking | 21 Hz    | 2    | 2.0 dB   |
| Peaking | 793 Hz   | 2.11 | 2.1 dB   |
| Peaking | 1231 Hz  | 5.31 | -1.7 dB  |
| Peaking | 12448 Hz | 2.18 | 3.1 dB   |
| Peaking | 16674 Hz | 2.89 | -3.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.7 dB  |
| Peaking | 250 Hz   | 1.41 | -3.8 dB  |
| Peaking | 500 Hz   | 1.41 | 1.1 dB   |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -13.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kinera%20Odin/Kinera%20Odin.png)