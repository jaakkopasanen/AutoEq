# VSonic VSD1S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.1; 23 -3.6; 25 -4.2; 28 -4.8; 31 -5.4; 34 -5.9; 37 -6.3; 41 -6.8; 45 -7.2; 49 -7.6; 54 -8.0; 60 -8.5; 66 -8.9; 72 -9.4; 79 -9.9; 87 -10.4; 96 -10.9; 106 -11.3; 116 -11.7; 128 -12.0; 141 -12.3; 155 -12.5; 170 -12.6; 187 -12.6; 206 -12.6; 227 -12.5; 249 -12.2; 274 -12.0; 302 -11.5; 332 -11.0; 365 -10.5; 402 -10.1; 442 -9.6; 486 -9.0; 535 -8.3; 588 -7.6; 647 -6.9; 712 -6.2; 783 -5.4; 861 -4.8; 947 -4.5; 1042 -4.6; 1146 -5.2; 1261 -5.7; 1387 -5.9; 1526 -5.6; 1678 -5.0; 1846 -4.6; 2031 -3.9; 2234 -3.1; 2457 -2.3; 2703 -1.6; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.4; 5267 -3.8; 5793 -5.4; 6373 -3.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -13.4; 15026 -19.3; 16529 -18.8; 18182 -19.8; 20000 -25.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD1S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.03 | 4.1 dB  |
| Peaking | 111 Hz   | 0.65 | -2.5 dB |
| Peaking | 231 Hz   | 0.56 | -4.9 dB |
| Peaking | 875 Hz   | 1.85 | 2.7 dB  |
| Peaking | 3489 Hz  | 1.2  | 6.7 dB  |
| Peaking | 8356 Hz  | 0.74 | 5.4 dB  |
| Peaking | 12123 Hz | 2.59 | 8.0 dB  |
| Peaking | 19771 Hz | 0.13 | -8.0 dB |
| Peaking | 19781 Hz | 0.13 | -7.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.4 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -16.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/VSonic%20VSD1S/VSonic%20VSD1S.png)