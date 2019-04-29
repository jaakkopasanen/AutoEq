# Jomo Tango
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.1; 25 -8.3; 28 -8.6; 31 -8.8; 34 -9.0; 37 -9.1; 41 -9.3; 45 -9.5; 49 -9.7; 54 -9.8; 60 -10.1; 66 -10.3; 72 -10.6; 79 -10.9; 87 -11.2; 96 -11.6; 106 -11.8; 116 -12.0; 128 -12.1; 141 -12.2; 155 -12.3; 170 -12.2; 187 -12.0; 206 -11.7; 227 -11.3; 249 -11.1; 274 -10.9; 302 -10.2; 332 -9.5; 365 -8.8; 402 -8.1; 442 -7.4; 486 -6.6; 535 -5.8; 588 -4.9; 647 -4.1; 712 -3.2; 783 -2.3; 861 -1.6; 947 -1.3; 1042 -1.3; 1146 -1.7; 1261 -2.1; 1387 -2.2; 1526 -2.0; 1678 -1.6; 1846 -1.2; 2031 -0.8; 2234 -0.5; 2457 -0.6; 2703 -1.0; 2973 -1.1; 3270 -1.2; 3597 -1.4; 3957 -2.3; 4353 -3.6; 4788 -6.0; 5267 -7.5; 5793 -5.3; 6373 -2.7; 7010 -3.1; 7711 -5.2; 8482 -5.4; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -8.4; 15026 -17.3; 16529 -20.2; 18182 -17.2; 20000 -11.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jomo Tango GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jomo Tango ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.3  | -2.7 dB  |
| Peaking | 182 Hz   | 0.48 | -5.8 dB  |
| Peaking | 866 Hz   | 1.21 | 4.2 dB   |
| Peaking | 2497 Hz  | 0.83 | 4.7 dB   |
| Peaking | 17101 Hz | 1.27 | -16.3 dB |
| Peaking | 3861 Hz  | 3.41 | 1.2 dB   |
| Peaking | 5207 Hz  | 3.64 | -4.3 dB  |
| Peaking | 6504 Hz  | 4.48 | 3.6 dB   |
| Peaking | 13073 Hz | 1.81 | 5.3 dB   |
| Peaking | 15060 Hz | 2.87 | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -2.9 dB  |
| Peaking | 62 Hz    | 1.41 | -3.4 dB  |
| Peaking | 125 Hz   | 1.41 | -5.7 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.3 dB   |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -15.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Jomo%20Tango/Jomo%20Tango.png)