# Advanced 747 NC
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -12.2; 25 -12.7; 28 -13.4; 31 -13.9; 34 -14.3; 37 -14.6; 41 -15.0; 45 -15.3; 49 -15.5; 54 -15.8; 60 -16.1; 66 -16.3; 72 -16.6; 79 -16.8; 87 -17.1; 96 -17.3; 106 -17.4; 116 -17.5; 128 -17.4; 141 -17.3; 155 -17.1; 170 -16.8; 187 -16.3; 206 -15.9; 227 -15.3; 249 -14.6; 274 -13.9; 302 -13.1; 332 -12.2; 365 -11.3; 402 -10.5; 442 -9.6; 486 -8.7; 535 -7.8; 588 -6.8; 647 -5.9; 712 -4.8; 783 -3.8; 861 -2.9; 947 -2.2; 1042 -1.8; 1146 -1.5; 1261 -1.2; 1387 -1.0; 1526 -0.9; 1678 -0.9; 1846 -0.8; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.8; 3270 -0.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.9; 5267 -2.9; 5793 -5.7; 6373 -4.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -11.2; 15026 -17.5; 16529 -21.4; 18182 -26.2; 20000 -22.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced 747 NC GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced 747 NC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 56 Hz    | 0.3  | -7.3 dB  |
| Peaking | 226 Hz   | 0.41 | -7.7 dB  |
| Peaking | 4445 Hz  | 0.09 | 7.3 dB   |
| Peaking | 18320 Hz | 0.47 | -24.6 dB |
| Peaking | 4616 Hz  | 3.08 | 1.2 dB   |
| Peaking | 5764 Hz  | 6.97 | -3.7 dB  |
| Peaking | 8071 Hz  | 4.23 | -2.1 dB  |
| Peaking | 12847 Hz | 2.29 | 6.4 dB   |
| Peaking | 14575 Hz | 2.05 | -4.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -7.4 dB  |
| Peaking | 125 Hz   | 1.41 | -9.3 dB  |
| Peaking | 250 Hz   | 1.41 | -6.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.6 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.2 dB   |
| Peaking | 16000 Hz | 1.41 | -18.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Advanced%20747%20NC/Advanced%20747%20NC.png)