# Simgot EN700
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.9; 25 -1.3; 28 -1.8; 31 -2.2; 34 -2.6; 37 -2.9; 41 -3.3; 45 -3.6; 49 -3.9; 54 -4.3; 60 -4.7; 66 -5.2; 72 -5.6; 79 -6.0; 87 -6.6; 96 -7.1; 106 -7.5; 116 -8.0; 128 -8.3; 141 -8.8; 155 -9.0; 170 -9.2; 187 -9.4; 206 -9.4; 227 -9.4; 249 -9.4; 274 -9.3; 302 -9.0; 332 -8.7; 365 -8.4; 402 -8.0; 442 -7.7; 486 -7.3; 535 -6.9; 588 -6.5; 647 -6.1; 712 -5.6; 783 -5.2; 861 -4.8; 947 -4.7; 1042 -5.0; 1146 -5.6; 1261 -6.1; 1387 -6.3; 1526 -6.3; 1678 -6.3; 1846 -6.4; 2031 -6.6; 2234 -7.2; 2457 -7.9; 2703 -7.8; 2973 -6.5; 3270 -5.3; 3597 -5.2; 3957 -6.0; 4353 -9.7; 4788 -12.2; 5267 -6.7; 5793 -1.5; 6373 -1.2; 7010 -4.1; 7711 -6.3; 8482 -6.6; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -10.7; 16529 -16.3; 18182 -20.4; 20000 -17.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Simgot EN700 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Simgot EN700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 16 Hz    | 0.41 | 6.3 dB   |
| Peaking | 195 Hz   | 0.9  | -3.4 dB  |
| Peaking | 4798 Hz  | 5.5  | -9.2 dB  |
| Peaking | 5939 Hz  | 2.34 | 7.0 dB   |
| Peaking | 18637 Hz | 1.01 | -15.6 dB |
| Peaking | 903 Hz   | 2.12 | 2.2 dB   |
| Peaking | 2564 Hz  | 4.37 | -1.8 dB  |
| Peaking | 3460 Hz  | 4.95 | 1.8 dB   |
| Peaking | 13580 Hz | 2.32 | 3.3 dB   |
| Peaking | 16600 Hz | 2.39 | -3.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB   |
| Peaking | 62 Hz    | 1.41 | 1.2 dB   |
| Peaking | 125 Hz   | 1.41 | -1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 3.2 dB   |
| Peaking | 16000 Hz | 1.41 | -10.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Simgot%20EN700/Simgot%20EN700.png)