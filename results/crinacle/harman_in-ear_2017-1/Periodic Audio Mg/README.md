# Periodic Audio Mg
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.6; 25 -11.9; 28 -12.1; 31 -12.2; 34 -12.3; 37 -12.4; 41 -12.5; 45 -12.6; 49 -12.6; 54 -12.6; 60 -12.7; 66 -12.8; 72 -13.0; 79 -13.1; 87 -13.2; 96 -13.3; 106 -13.4; 116 -13.4; 128 -13.3; 141 -13.2; 155 -13.1; 170 -12.8; 187 -12.5; 206 -12.2; 227 -11.7; 249 -11.3; 274 -10.7; 302 -10.1; 332 -9.4; 365 -8.8; 402 -8.1; 442 -7.5; 486 -6.8; 535 -6.1; 588 -5.4; 647 -4.8; 712 -4.1; 783 -3.2; 861 -2.5; 947 -2.2; 1042 -2.2; 1146 -2.5; 1261 -2.6; 1387 -2.4; 1526 -2.2; 1678 -3.3; 1846 -4.4; 2031 -3.8; 2234 -2.9; 2457 -2.5; 2703 -2.4; 2973 -2.2; 3270 -1.9; 3597 -1.9; 3957 -2.5; 4353 -4.0; 4788 -5.3; 5267 -4.4; 5793 -1.9; 6373 -0.5; 7010 -3.4; 7711 -5.6; 8482 -5.9; 9330 -5.9; 10263 -5.9; 11289 -5.9; 12418 -5.9; 13660 -15.0; 15026 -28.4; 16529 -34.2; 18182 -32.1; 20000 -23.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Periodic Audio Mg GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Periodic Audio Mg ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.5dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 45 Hz    | 0.24 | -6.3 dB  |
| Peaking | 202 Hz   | 0.61 | -4.1 dB  |
| Peaking | 5567 Hz  | 0.87 | -2.4 dB  |
| Peaking | 8953 Hz  | 0.19 | 27.6 dB  |
| Peaking | 16809 Hz | 0.3  | -48.5 dB |
| Peaking | 1657 Hz  | 0.76 | 1.6 dB   |
| Peaking | 1880 Hz  | 2.73 | -3.4 dB  |
| Peaking | 8453 Hz  | 4.01 | -3.2 dB  |
| Peaking | 12675 Hz | 3.06 | 8.1 dB   |
| Peaking | 14994 Hz | 3.1  | -7.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.2 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -6.3 dB  |
| Peaking | 250 Hz   | 1.41 | -4.6 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB   |
| Peaking | 4000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 8000 Hz  | 1.41 | 9.1 dB   |
| Peaking | 16000 Hz | 1.41 | -33.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Periodic%20Audio%20Mg/Periodic%20Audio%20Mg.png)