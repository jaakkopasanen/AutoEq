# Hifiman RE400
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.9; 23 -3.1; 25 -3.2; 28 -3.5; 31 -3.6; 34 -3.8; 37 -4.0; 41 -4.2; 45 -4.4; 49 -4.6; 54 -4.8; 60 -5.1; 66 -5.5; 72 -5.8; 79 -6.2; 87 -6.7; 96 -7.1; 106 -7.5; 116 -7.9; 128 -8.2; 141 -8.5; 155 -8.8; 170 -8.9; 187 -9.0; 206 -9.0; 227 -9.0; 249 -8.9; 274 -8.8; 302 -8.7; 332 -8.5; 365 -8.2; 402 -8.1; 442 -7.9; 486 -7.5; 535 -7.2; 588 -6.9; 647 -6.6; 712 -6.3; 783 -6.0; 861 -5.8; 947 -6.0; 1042 -6.5; 1146 -7.2; 1261 -7.8; 1387 -8.2; 1526 -8.3; 1678 -8.4; 1846 -8.7; 2031 -8.8; 2234 -7.7; 2457 -6.9; 2703 -4.8; 2973 -2.3; 3270 -0.6; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.0; 5267 -3.4; 5793 -7.6; 6373 -7.7; 7010 -4.3; 7711 -6.2; 8482 -6.5; 9330 -8.1; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -10.7; 15026 -22.5; 16529 -26.9; 18182 -23.1; 20000 -17.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Hifiman RE400 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Hifiman RE400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.25 | 3.6 dB   |
| Peaking | 196 Hz   | 0.62 | -3.2 dB  |
| Peaking | 2395 Hz  | 0.44 | -27.5 dB |
| Peaking | 2985 Hz  | 0.38 | 29.7 dB  |
| Peaking | 17115 Hz | 0.87 | -23.9 dB |
| Peaking | 841 Hz   | 4.67 | 1.1 dB   |
| Peaking | 4670 Hz  | 3.73 | 2.2 dB   |
| Peaking | 5952 Hz  | 4.93 | -5.7 dB  |
| Peaking | 12898 Hz | 2.72 | 7.1 dB   |
| Peaking | 15336 Hz | 3.3  | -6.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 3.4 dB   |
| Peaking | 62 Hz    | 1.41 | 1.1 dB   |
| Peaking | 125 Hz   | 1.41 | -1.8 dB  |
| Peaking | 250 Hz   | 1.41 | -2.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.8 dB   |
| Peaking | 16000 Hz | 1.41 | -21.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Hifiman%20RE400/Hifiman%20RE400.png)