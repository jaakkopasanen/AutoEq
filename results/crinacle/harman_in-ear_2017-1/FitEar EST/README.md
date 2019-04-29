# FitEar EST
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.7; 25 -4.0; 28 -4.3; 31 -4.6; 34 -4.8; 37 -5.0; 41 -5.2; 45 -5.5; 49 -5.7; 54 -6.0; 60 -6.3; 66 -6.6; 72 -6.9; 79 -7.3; 87 -7.7; 96 -8.1; 106 -8.5; 116 -8.8; 128 -9.2; 141 -9.5; 155 -9.6; 170 -9.8; 187 -9.9; 206 -9.9; 227 -9.9; 249 -9.8; 274 -9.7; 302 -9.5; 332 -9.2; 365 -8.9; 402 -8.6; 442 -8.4; 486 -8.1; 535 -7.7; 588 -7.3; 647 -6.9; 712 -6.4; 783 -6.0; 861 -5.6; 947 -5.5; 1042 -5.7; 1146 -6.1; 1261 -6.4; 1387 -6.2; 1526 -5.6; 1678 -4.8; 1846 -3.9; 2031 -2.9; 2234 -1.8; 2457 -1.0; 2703 -0.5; 2973 -0.5; 3270 -0.8; 3597 -1.4; 3957 -2.3; 4353 -3.7; 4788 -5.4; 5267 -6.1; 5793 -4.6; 6373 -4.1; 7010 -4.4; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -11.4; 16529 -17.1; 18182 -13.4; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar EST GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar EST ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.36 | 3.2 dB   |
| Peaking | 203 Hz   | 0.53 | -4.1 dB  |
| Peaking | 2895 Hz  | 1.37 | 6.0 dB   |
| Peaking | 13739 Hz | 1.51 | 4.7 dB   |
| Peaking | 16595 Hz | 1.3  | -13.4 dB |
| Peaking | 903 Hz   | 2.89 | 1.1 dB   |
| Peaking | 1340 Hz  | 2.65 | -1.2 dB  |
| Peaking | 2162 Hz  | 4.83 | 0.6 dB   |
| Peaking | 5128 Hz  | 6.54 | -2.1 dB  |
| Peaking | 6413 Hz  | 3.69 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | -2.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 16000 Hz | 1.41 | -9.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20EST/FitEar%20EST.png)