# TFZ Balance 2M
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -15.2; 23 -15.1; 25 -15.1; 28 -15.0; 31 -14.9; 34 -14.7; 37 -14.6; 41 -14.5; 45 -14.4; 49 -14.2; 54 -14.1; 60 -13.9; 66 -13.8; 72 -13.8; 79 -13.7; 87 -13.6; 96 -13.5; 106 -13.4; 116 -13.3; 128 -13.1; 141 -12.9; 155 -12.6; 170 -12.3; 187 -11.9; 206 -11.5; 227 -11.1; 249 -10.6; 274 -10.2; 302 -9.6; 332 -9.0; 365 -8.5; 402 -8.1; 442 -7.7; 486 -7.2; 535 -6.8; 588 -6.4; 647 -5.8; 712 -5.3; 783 -5.1; 861 -5.0; 947 -5.2; 1042 -5.7; 1146 -6.6; 1261 -7.5; 1387 -8.1; 1526 -8.4; 1678 -8.7; 1846 -9.1; 2031 -9.1; 2234 -8.0; 2457 -5.8; 2703 -3.2; 2973 -1.1; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -1.4; 4788 -4.6; 5267 -6.3; 5793 -2.2; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.9; 15026 -22.3; 16529 -22.0; 18182 -19.6; 20000 -21.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`TFZ Balance 2M GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TFZ Balance 2M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 0.2  | -8.5 dB  |
| Peaking | 162 Hz   | 0.89 | -3.3 dB  |
| Peaking | 3765 Hz  | 1.5  | 8.2 dB   |
| Peaking | 12121 Hz | 0.4  | 25.5 dB  |
| Peaking | 15597 Hz | 0.33 | -35.4 dB |
| Peaking | 846 Hz   | 1.74 | 2.8 dB   |
| Peaking | 2143 Hz  | 1.34 | -4.6 dB  |
| Peaking | 2836 Hz  | 1.98 | 4.8 dB   |
| Peaking | 5787 Hz  | 1.47 | -4.8 dB  |
| Peaking | 6250 Hz  | 3.79 | 9.7 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB  |
| Peaking | 62 Hz    | 1.41 | -5.1 dB  |
| Peaking | 125 Hz   | 1.41 | -5.5 dB  |
| Peaking | 250 Hz   | 1.41 | -3.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.4 dB   |
| Peaking | 1000 Hz  | 1.41 | 1.3 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.7 dB   |
| Peaking | 16000 Hz | 1.41 | -19.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/TFZ%20Balance%202M/TFZ%20Balance%202M.png)