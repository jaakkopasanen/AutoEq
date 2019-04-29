# VSonic VSD2S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.7; 25 -3.1; 28 -3.6; 31 -4.1; 34 -4.5; 37 -4.8; 41 -5.2; 45 -5.6; 49 -5.9; 54 -6.3; 60 -6.7; 66 -7.2; 72 -7.6; 79 -8.1; 87 -8.6; 96 -9.2; 106 -9.7; 116 -10.2; 128 -10.6; 141 -11.1; 155 -11.4; 170 -11.7; 187 -12.0; 206 -12.2; 227 -12.3; 249 -12.4; 274 -12.4; 302 -12.3; 332 -12.2; 365 -12.1; 402 -11.9; 442 -11.7; 486 -11.5; 535 -11.1; 588 -10.6; 647 -10.0; 712 -9.3; 783 -8.4; 861 -7.4; 947 -6.3; 1042 -5.5; 1146 -5.1; 1261 -4.7; 1387 -3.8; 1526 -2.4; 1678 -0.8; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.6; 5267 -2.1; 5793 -4.8; 6373 -9.4; 7010 -9.7; 7711 -11.4; 8482 -10.3; 9330 -6.6; 10263 -6.5; 11289 -6.5; 12418 -8.0; 13660 -16.4; 15026 -21.2; 16529 -24.0; 18182 -24.5; 20000 -16.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`VSonic VSD2S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD2S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 0.3  | 5.3 dB   |
| Peaking | 292 Hz   | 0.36 | -6.4 dB  |
| Peaking | 2425 Hz  | 0.63 | 7.7 dB   |
| Peaking | 15704 Hz | 2    | -8.7 dB  |
| Peaking | 18295 Hz | 0.82 | -17.4 dB |
| Peaking | 2625 Hz  | 3.79 | -1.2 dB  |
| Peaking | 4979 Hz  | 1.94 | 5.2 dB   |
| Peaking | 7191 Hz  | 1.47 | -8.1 dB  |
| Peaking | 11432 Hz | 1.23 | 6.3 dB   |
| Peaking | 13995 Hz | 3.44 | -5.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.3 dB   |
| Peaking | 62 Hz    | 1.41 | -0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -3.4 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB   |
| Peaking | 2000 Hz  | 1.41 | 5.8 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB  |
| Peaking | 16000 Hz | 1.41 | -20.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/VSonic%20VSD2S/VSonic%20VSD2S.png)