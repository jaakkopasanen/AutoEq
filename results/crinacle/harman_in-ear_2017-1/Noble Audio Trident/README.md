# Noble Audio Trident
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.8; 23 -7.0; 25 -7.1; 28 -7.3; 31 -7.5; 34 -7.6; 37 -7.8; 41 -8.0; 45 -8.2; 49 -8.4; 54 -8.6; 60 -8.9; 66 -9.3; 72 -9.6; 79 -10.0; 87 -10.3; 96 -10.8; 106 -11.2; 116 -11.5; 128 -11.8; 141 -12.1; 155 -12.3; 170 -12.4; 187 -12.5; 206 -12.4; 227 -12.3; 249 -12.2; 274 -12.0; 302 -11.7; 332 -11.3; 365 -10.9; 402 -10.5; 442 -10.1; 486 -9.6; 535 -9.0; 588 -8.4; 647 -7.8; 712 -7.1; 783 -6.3; 861 -5.7; 947 -5.2; 1042 -5.2; 1146 -5.4; 1261 -5.5; 1387 -5.2; 1526 -4.6; 1678 -3.9; 1846 -3.3; 2031 -2.6; 2234 -1.7; 2457 -0.7; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.1; 4788 -6.4; 5267 -7.3; 5793 -10.4; 6373 -13.2; 7010 -11.4; 7711 -7.6; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.8; 15026 -14.4; 16529 -21.8; 18182 -22.3; 20000 -11.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Noble Audio Trident GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noble Audio Trident ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 123 Hz   | 0.45 | -1.7 dB  |
| Peaking | 229 Hz   | 0.45 | -4.8 dB  |
| Peaking | 5994 Hz  | 0.34 | 11.3 dB  |
| Peaking | 6393 Hz  | 1.63 | -16.7 dB |
| Peaking | 17472 Hz | 0.89 | -20.1 dB |
| Peaking | 1497 Hz  | 3.32 | -1.4 dB  |
| Peaking | 4386 Hz  | 2.3  | 2.8 dB   |
| Peaking | 4721 Hz  | 5.32 | -4.4 dB  |
| Peaking | 9987 Hz  | 3.83 | -1.4 dB  |
| Peaking | 13582 Hz | 5.36 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB  |
| Peaking | 125 Hz   | 1.41 | -4.5 dB  |
| Peaking | 250 Hz   | 1.41 | -5.2 dB  |
| Peaking | 500 Hz   | 1.41 | -2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.2 dB   |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB  |
| Peaking | 16000 Hz | 1.41 | -13.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Noble%20Audio%20Trident/Noble%20Audio%20Trident.png)