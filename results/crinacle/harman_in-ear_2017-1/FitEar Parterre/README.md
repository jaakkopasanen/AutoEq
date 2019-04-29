# FitEar Parterre
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.9; 23 -10.9; 25 -10.9; 28 -11.0; 31 -11.1; 34 -11.1; 37 -11.2; 41 -11.4; 45 -11.5; 49 -11.6; 54 -11.7; 60 -12.0; 66 -12.2; 72 -12.5; 79 -12.7; 87 -13.1; 96 -13.4; 106 -13.6; 116 -13.9; 128 -14.0; 141 -14.2; 155 -14.3; 170 -14.2; 187 -14.2; 206 -14.0; 227 -13.8; 249 -13.5; 274 -13.2; 302 -12.7; 332 -12.2; 365 -11.6; 402 -11.1; 442 -10.6; 486 -10.0; 535 -9.3; 588 -8.6; 647 -7.9; 712 -7.1; 783 -6.2; 861 -5.5; 947 -4.9; 1042 -4.7; 1146 -4.8; 1261 -4.7; 1387 -4.2; 1526 -3.3; 1678 -2.4; 1846 -1.8; 2031 -1.3; 2234 -0.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.8; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.3; 7711 -6.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.2; 15026 -20.9; 16529 -18.9; 18182 -7.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`FitEar Parterre GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FitEar Parterre ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.19 | -4.2 dB  |
| Peaking | 139 Hz   | 0.72 | -3.6 dB  |
| Peaking | 302 Hz   | 0.73 | -4.2 dB  |
| Peaking | 3254 Hz  | 0.49 | 6.7 dB   |
| Peaking | 15673 Hz | 2.35 | -17.6 dB |
| Peaking | 5570 Hz  | 2.21 | 0.1 dB   |
| Peaking | 6336 Hz  | 3.04 | 4.2 dB   |
| Peaking | 7423 Hz  | 2.3  | -4.2 dB  |
| Peaking | 12764 Hz | 5.47 | 3.5 dB   |
| Peaking | 22048 Hz | 1.75 | -0.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB  |
| Peaking | 62 Hz    | 1.41 | -3.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -6.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 16000 Hz | 1.41 | -13.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/FitEar%20Parterre/FitEar%20Parterre.png)