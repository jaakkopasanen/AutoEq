# Mee Audio Planamic IEM
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.8; 23 -11.9; 25 -12.1; 28 -12.2; 31 -12.4; 34 -12.5; 37 -12.6; 41 -12.7; 45 -12.8; 49 -13.0; 54 -13.1; 60 -13.3; 66 -13.5; 72 -13.7; 79 -13.9; 87 -14.1; 96 -14.2; 106 -14.3; 116 -14.3; 128 -14.3; 141 -14.3; 155 -14.3; 170 -14.1; 187 -13.7; 206 -13.5; 227 -13.6; 249 -13.3; 274 -12.8; 302 -12.2; 332 -11.4; 365 -10.4; 402 -9.8; 442 -9.4; 486 -8.9; 535 -8.3; 588 -7.8; 647 -7.3; 712 -6.8; 783 -6.3; 861 -6.1; 947 -6.3; 1042 -6.6; 1146 -7.0; 1261 -7.4; 1387 -7.6; 1526 -7.8; 1678 -8.2; 1846 -8.3; 2031 -8.3; 2234 -8.5; 2457 -9.4; 2703 -9.6; 2973 -9.7; 3270 -10.0; 3597 -11.1; 3957 -12.5; 4353 -9.8; 4788 -4.7; 5267 -0.7; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.7; 15026 -21.2; 16529 -20.5; 18182 -14.8; 20000 -7.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Mee Audio Planamic IEM GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Mee Audio Planamic IEM ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 55 Hz    | 0.29 | -6.5 dB  |
| Peaking | 206 Hz   | 0.79 | -4.3 dB  |
| Peaking | 4204 Hz  | 1.04 | -21.4 dB |
| Peaking | 5129 Hz  | 0.97 | 21.8 dB  |
| Peaking | 16068 Hz | 1.32 | -17.2 dB |
| Peaking | 839 Hz   | 2.89 | 1.6 dB   |
| Peaking | 7985 Hz  | 4.63 | -2.4 dB  |
| Peaking | 12500 Hz | 2.95 | 4.6 dB   |
| Peaking | 14361 Hz | 4.22 | -4.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -5.7 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -6.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.8 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB   |
| Peaking | 2000 Hz  | 1.41 | -2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB  |
| Peaking | 8000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 16000 Hz | 1.41 | -17.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/Mee%20Audio%20Planamic%20IEM/Mee%20Audio%20Planamic%20IEM.png)