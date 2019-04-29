# Kumitate KL-Meteo
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.4; 23 -11.4; 25 -11.5; 28 -11.5; 31 -11.6; 34 -11.6; 37 -11.6; 41 -11.7; 45 -11.7; 49 -11.6; 54 -11.6; 60 -11.6; 66 -11.6; 72 -11.7; 79 -11.7; 87 -11.6; 96 -11.6; 106 -11.4; 116 -11.1; 128 -10.8; 141 -10.5; 155 -10.0; 170 -9.4; 187 -8.7; 206 -7.9; 227 -7.1; 249 -6.4; 274 -5.5; 302 -4.7; 332 -3.9; 365 -3.3; 402 -2.9; 442 -2.7; 486 -2.7; 535 -2.9; 588 -3.1; 647 -3.6; 712 -4.0; 783 -4.5; 861 -5.0; 947 -5.7; 1042 -6.7; 1146 -7.9; 1261 -8.8; 1387 -9.1; 1526 -8.8; 1678 -8.1; 1846 -7.2; 2031 -6.0; 2234 -4.6; 2457 -3.4; 2703 -2.6; 2973 -2.0; 3270 -1.7; 3597 -1.8; 3957 -1.9; 4353 -1.8; 4788 -1.3; 5267 -0.8; 5793 -0.5; 6373 -1.2; 7010 -4.4; 7711 -5.3; 8482 -5.1; 9330 -5.1; 10263 -5.1; 11289 -5.1; 12418 -5.1; 13660 -7.5; 15026 -15.2; 16529 -16.8; 18182 -14.3; 20000 -14.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Kumitate KL-Meteo GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Kumitate KL-Meteo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 68 Hz    | 0.22 | -7.6 dB  |
| Peaking | 1282 Hz  | 0.2  | 8.8 dB   |
| Peaking | 1400 Hz  | 0.82 | -12.6 dB |
| Peaking | 5794 Hz  | 6    | 2.2 dB   |
| Peaking | 17447 Hz | 0.78 | -12.2 dB |
| Peaking | 19 Hz    | 2.23 | -1.1 dB  |
| Peaking | 377 Hz   | 3.85 | 0.8 dB   |
| Peaking | 7600 Hz  | 5.02 | -2.3 dB  |
| Peaking | 12969 Hz | 2.41 | 4.4 dB   |
| Peaking | 15071 Hz | 3.13 | -4.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.9 dB  |
| Peaking | 125 Hz   | 1.41 | -5.4 dB  |
| Peaking | 250 Hz   | 1.41 | -0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 4.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB   |
| Peaking | 16000 Hz | 1.41 | -12.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/Kumitate%20KL-Meteo/Kumitate%20KL-Meteo.png)