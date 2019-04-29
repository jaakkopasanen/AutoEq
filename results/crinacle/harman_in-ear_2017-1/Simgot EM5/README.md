# Simgot EM5
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.4; 25 -6.7; 28 -7.2; 31 -7.6; 34 -7.9; 37 -8.1; 41 -8.4; 45 -8.6; 49 -8.8; 54 -9.1; 60 -9.4; 66 -9.8; 72 -10.1; 79 -10.5; 87 -10.9; 96 -11.3; 106 -11.6; 116 -11.9; 128 -12.2; 141 -12.4; 155 -12.5; 170 -12.5; 187 -12.5; 206 -12.4; 227 -12.2; 249 -12.0; 274 -11.7; 302 -11.3; 332 -10.8; 365 -10.3; 402 -9.9; 442 -9.4; 486 -8.9; 535 -8.2; 588 -7.6; 647 -7.0; 712 -6.3; 783 -5.6; 861 -5.0; 947 -4.7; 1042 -4.8; 1146 -5.3; 1261 -5.7; 1387 -5.9; 1526 -5.9; 1678 -5.9; 1846 -5.6; 2031 -4.8; 2234 -3.6; 2457 -2.7; 2703 -0.7; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -1.9; 4353 -3.7; 4788 -2.7; 5267 -2.2; 5793 -2.3; 6373 -4.3; 7010 -4.2; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.6; 15026 -20.4; 16529 -17.6; 18182 -7.7; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EM5 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EM5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 125 Hz   | 0.6  | -5.2 dB  |
| Peaking | 274 Hz   | 1.2  | -3.1 dB  |
| Peaking | 3123 Hz  | 1.45 | 6.1 dB   |
| Peaking | 5717 Hz  | 2.24 | 3.0 dB   |
| Peaking | 15530 Hz | 2.28 | -16.0 dB |
| Peaking | 15 Hz    | 2.52 | 1.2 dB   |
| Peaking | 934 Hz   | 2.67 | 2.1 dB   |
| Peaking | 1789 Hz  | 3.23 | -0.9 dB  |
| Peaking | 12529 Hz | 2.99 | 3.7 dB   |
| Peaking | 14188 Hz | 4.84 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.3 dB  |
| Peaking | 62 Hz    | 1.41 | -2.3 dB  |
| Peaking | 125 Hz   | 1.41 | -4.9 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 16000 Hz | 1.41 | -13.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Simgot%20EM5/Simgot%20EM5.png)