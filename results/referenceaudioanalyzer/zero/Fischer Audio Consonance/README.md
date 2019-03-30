# Fischer Audio Consonance
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -19.1; 23 -19.1; 25 -19.1; 28 -19.0; 31 -18.9; 34 -18.8; 37 -18.7; 41 -18.6; 45 -18.4; 49 -18.3; 54 -18.1; 60 -17.8; 66 -17.5; 72 -17.3; 79 -17.0; 87 -16.6; 96 -16.2; 106 -15.6; 116 -15.0; 128 -14.2; 141 -13.3; 155 -13.6; 170 -14.4; 187 -14.4; 206 -13.7; 227 -13.0; 249 -12.4; 274 -11.8; 302 -11.1; 332 -10.5; 365 -9.9; 402 -9.3; 442 -8.8; 486 -8.3; 535 -7.7; 588 -7.2; 647 -6.8; 712 -6.3; 783 -5.8; 861 -5.3; 947 -4.7; 1042 -4.0; 1146 -3.5; 1261 -4.0; 1387 -4.4; 1526 -4.0; 1678 -3.5; 1846 -2.9; 2031 -2.1; 2234 -1.7; 2457 -1.9; 2703 -1.8; 2973 -1.2; 3270 -0.8; 3597 -0.8; 3957 -1.3; 4353 -2.2; 4788 -2.5; 5267 -1.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -6.4; 12418 -6.4; 13660 -6.4; 15026 -6.4; 16529 -6.4; 18182 -6.4; 20000 -6.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Fischer Audio Consonance GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio Consonance ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.59 | -10.1 dB |
| Peaking | 67 Hz   | 0.54 | -7.9 dB  |
| Peaking | 225 Hz  | 0.92 | -4.4 dB  |
| Peaking | 2739 Hz | 0.63 | 5.2 dB   |
| Peaking | 5924 Hz | 4.42 | 4.2 dB   |
| Peaking | 446 Hz  | 3.01 | -0.4 dB  |
| Peaking | 1123 Hz | 2.26 | 2.4 dB   |
| Peaking | 1361 Hz | 1.58 | -1.6 dB  |
| Peaking | 3675 Hz | 4.6  | 1.1 dB   |
| Peaking | 8619 Hz | 2.68 | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -13.2 dB |
| Peaking | 62 Hz    | 1.41 | -8.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.8 dB  |
| Peaking | 250 Hz   | 1.41 | -5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB   |
| Peaking | 2000 Hz  | 1.41 | 3.1 dB   |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB   |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 16000 Hz | 1.41 | -0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Fischer%20Audio%20Consonance/Fischer%20Audio%20Consonance.png)