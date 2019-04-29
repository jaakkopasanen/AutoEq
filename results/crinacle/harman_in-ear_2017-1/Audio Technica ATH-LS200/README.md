# Audio Technica ATH-LS200
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.4; 23 -5.5; 25 -5.7; 28 -5.8; 31 -6.0; 34 -6.1; 37 -6.3; 41 -6.4; 45 -6.6; 49 -6.8; 54 -7.1; 60 -7.3; 66 -7.6; 72 -8.0; 79 -8.4; 87 -8.7; 96 -9.2; 106 -9.6; 116 -9.9; 128 -10.2; 141 -10.5; 155 -10.6; 170 -10.8; 187 -10.8; 206 -10.8; 227 -10.7; 249 -10.6; 274 -10.5; 302 -10.2; 332 -9.8; 365 -9.5; 402 -9.2; 442 -8.8; 486 -8.5; 535 -8.1; 588 -7.6; 647 -7.2; 712 -6.7; 783 -6.2; 861 -5.8; 947 -5.7; 1042 -6.0; 1146 -6.5; 1261 -7.0; 1387 -7.2; 1526 -6.9; 1678 -6.5; 1846 -6.2; 2031 -6.1; 2234 -5.9; 2457 -5.9; 2703 -5.0; 2973 -2.9; 3270 -1.6; 3597 -1.0; 3957 -1.5; 4353 -3.0; 4788 -4.5; 5267 -3.0; 5793 -0.5; 6373 -0.9; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -12.2; 15026 -24.2; 16529 -26.8; 18182 -12.0; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-LS200 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-LS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 19 Hz    | 0.53 | 1.1 dB   |
| Peaking | 190 Hz   | 0.55 | -4.6 dB  |
| Peaking | 5119 Hz  | 0.79 | 5.4 dB   |
| Peaking | 12459 Hz | 2.83 | 7.2 dB   |
| Peaking | 15883 Hz | 1.64 | -24.3 dB |
| Peaking | 872 Hz   | 3.35 | 1.5 dB   |
| Peaking | 3556 Hz  | 2.17 | 8.1 dB   |
| Peaking | 3905 Hz  | 0.95 | -6.2 dB  |
| Peaking | 6060 Hz  | 4.26 | 4.7 dB   |
| Peaking | 17062 Hz | 7.86 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB   |
| Peaking | 62 Hz    | 1.41 | -0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.5 dB   |
| Peaking | 16000 Hz | 1.41 | -19.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Audio%20Technica%20ATH-LS200/Audio%20Technica%20ATH-LS200.png)