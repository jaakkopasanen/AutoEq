# FitEar Air 2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.2; 23 -4.7; 25 -5.1; 28 -5.7; 31 -6.2; 34 -6.6; 37 -7.0; 41 -7.3; 45 -7.7; 49 -8.0; 54 -8.3; 60 -8.7; 66 -9.1; 72 -9.5; 79 -9.9; 87 -10.2; 96 -10.5; 106 -10.9; 116 -11.1; 128 -11.3; 141 -11.4; 155 -11.4; 170 -11.3; 187 -11.2; 206 -10.9; 227 -10.7; 249 -10.4; 274 -10.0; 302 -9.6; 332 -9.0; 365 -8.4; 402 -8.0; 442 -7.5; 486 -7.0; 535 -6.5; 588 -6.0; 647 -5.6; 712 -5.1; 783 -4.7; 861 -4.5; 947 -4.6; 1042 -5.0; 1146 -5.6; 1261 -6.2; 1387 -6.9; 1526 -7.5; 1678 -8.4; 1846 -9.5; 2031 -9.3; 2234 -7.0; 2457 -4.3; 2703 -2.1; 2973 -0.6; 3270 -0.5; 3597 -0.5; 3957 -1.0; 4353 -1.8; 4788 -1.9; 5267 -2.7; 5793 -4.6; 6373 -8.5; 7010 -7.7; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -7.7; 11289 -11.1; 12418 -15.1; 13660 -22.9; 15026 -27.3; 16529 -22.9; 18182 -16.6; 20000 -12.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Air 2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Air 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 18 Hz    | 1.15 | 2.9 dB   |
| Peaking | 155 Hz   | 0.46 | -5.2 dB  |
| Peaking | 1826 Hz  | 1.74 | -9.6 dB  |
| Peaking | 7047 Hz  | 0.16 | 10.9 dB  |
| Peaking | 15114 Hz | 0.7  | -30.4 dB |
| Peaking | 1287 Hz  | 2.49 | -2.3 dB  |
| Peaking | 2115 Hz  | 0.96 | 3.3 dB   |
| Peaking | 2163 Hz  | 3.02 | -4.3 dB  |
| Peaking | 6490 Hz  | 5.34 | -5.7 dB  |
| Peaking | 9948 Hz  | 3.37 | 3.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB   |
| Peaking | 62 Hz    | 1.41 | -2.1 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB   |
| Peaking | 1000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 16000 Hz | 1.41 | -24.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Air%202/FitEar%20Air%202.png)