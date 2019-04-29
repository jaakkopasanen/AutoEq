# qdc Anole V3 Bass
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -12.2; 23 -12.3; 25 -12.5; 28 -12.7; 31 -12.8; 34 -12.9; 37 -13.0; 41 -13.1; 45 -13.2; 49 -13.3; 54 -13.3; 60 -13.5; 66 -13.6; 72 -13.9; 79 -14.1; 87 -14.3; 96 -14.6; 106 -14.8; 116 -14.9; 128 -15.1; 141 -15.1; 155 -15.1; 170 -15.0; 187 -14.9; 206 -14.6; 227 -14.3; 249 -14.0; 274 -13.6; 302 -13.1; 332 -12.5; 365 -11.9; 402 -11.3; 442 -10.7; 486 -9.9; 535 -9.2; 588 -8.3; 647 -7.5; 712 -6.5; 783 -5.6; 861 -4.7; 947 -4.1; 1042 -3.8; 1146 -3.8; 1261 -3.8; 1387 -3.4; 1526 -2.6; 1678 -1.8; 1846 -1.0; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -1.3; 6373 -3.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -12.7; 15026 -21.6; 16529 -20.6; 18182 -15.8; 20000 -18.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`qdc Anole V3 Bass GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `qdc Anole V3 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.63 | -2.3 dB  |
| Peaking | 50 Hz    | 0.32 | -4.0 dB  |
| Peaking | 211 Hz   | 0.42 | -7.0 dB  |
| Peaking | 6663 Hz  | 0.14 | 7.9 dB   |
| Peaking | 16265 Hz | 0.65 | -21.1 dB |
| Peaking | 1380 Hz  | 4.3  | -1.3 dB  |
| Peaking | 2788 Hz  | 0.32 | 0.3 dB   |
| Peaking | 7893 Hz  | 3.6  | -3.0 dB  |
| Peaking | 11104 Hz | 2.1  | -0.4 dB  |
| Peaking | 12587 Hz | 4.86 | 5.0 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -6.1 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB  |
| Peaking | 125 Hz   | 1.41 | -7.0 dB  |
| Peaking | 250 Hz   | 1.41 | -6.5 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 2000 Hz  | 1.41 | 4.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 6.3 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.3 dB   |
| Peaking | 16000 Hz | 1.41 | -17.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/qdc%20Anole%20V3%20Bass/qdc%20Anole%20V3%20Bass.png)