# Sony XBA-300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.1; 25 -4.3; 28 -4.7; 31 -5.0; 34 -5.2; 37 -5.4; 41 -5.7; 45 -5.9; 49 -6.1; 54 -6.4; 60 -6.7; 66 -7.0; 72 -7.3; 79 -7.7; 87 -8.0; 96 -8.4; 106 -8.6; 116 -8.9; 128 -9.1; 141 -9.2; 155 -9.3; 170 -9.3; 187 -9.2; 206 -9.0; 227 -8.8; 249 -8.4; 274 -8.1; 302 -7.7; 332 -7.1; 365 -6.6; 402 -6.1; 442 -5.6; 486 -5.0; 535 -4.4; 588 -3.9; 647 -3.3; 712 -2.7; 783 -2.1; 861 -1.7; 947 -1.6; 1042 -1.9; 1146 -2.5; 1261 -3.1; 1387 -3.3; 1526 -3.2; 1678 -3.1; 1846 -3.1; 2031 -3.2; 2234 -3.5; 2457 -4.5; 2703 -5.9; 2973 -6.4; 3270 -6.6; 3597 -6.6; 3957 -7.6; 4353 -8.1; 4788 -5.6; 5267 -3.2; 5793 -1.5; 6373 -0.5; 7010 -3.1; 7711 -5.7; 8482 -8.8; 9330 -10.4; 10263 -11.1; 11289 -11.4; 12418 -11.9; 13660 -14.6; 15026 -20.6; 16529 -27.3; 18182 -29.7; 20000 -24.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 165 Hz   | 0.64 | -4.0 dB  |
| Peaking | 881 Hz   | 1.13 | 4.3 dB   |
| Peaking | 1922 Hz  | 3.18 | 2.2 dB   |
| Peaking | 6415 Hz  | 2.82 | 8.6 dB   |
| Peaking | 18282 Hz | 0.61 | -26.3 dB |
| Peaking | 21 Hz    | 1.44 | 1.9 dB   |
| Peaking | 4415 Hz  | 2.66 | -3.3 dB  |
| Peaking | 5111 Hz  | 4.19 | 3.0 dB   |
| Peaking | 12790 Hz | 2.42 | 3.5 dB   |
| Peaking | 16238 Hz | 2.79 | -4.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB   |
| Peaking | 62 Hz    | 1.41 | -1.0 dB  |
| Peaking | 125 Hz   | 1.41 | -3.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.0 dB  |
| Peaking | 500 Hz   | 1.41 | 0.9 dB   |
| Peaking | 1000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 4000 Hz  | 1.41 | -0.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 16000 Hz | 1.41 | -29.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Sony%20XBA-300/Sony%20XBA-300.png)