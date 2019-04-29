# AAW A2H V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -13.9; 23 -13.9; 25 -13.9; 28 -13.9; 31 -13.8; 34 -13.8; 37 -13.7; 41 -13.7; 45 -13.6; 49 -13.5; 54 -13.5; 60 -13.5; 66 -13.6; 72 -13.6; 79 -13.7; 87 -13.7; 96 -13.9; 106 -14.0; 116 -14.0; 128 -14.0; 141 -14.0; 155 -13.9; 170 -13.8; 187 -13.5; 206 -13.3; 227 -13.0; 249 -12.7; 274 -12.3; 302 -11.8; 332 -11.3; 365 -10.7; 402 -10.2; 442 -9.7; 486 -9.1; 535 -8.4; 588 -7.8; 647 -7.2; 712 -6.5; 783 -5.8; 861 -5.3; 947 -5.0; 1042 -5.1; 1146 -5.5; 1261 -5.9; 1387 -5.9; 1526 -5.8; 1678 -5.4; 1846 -4.9; 2031 -3.8; 2234 -2.3; 2457 -0.7; 2703 -0.6; 2973 -0.6; 3270 -0.9; 3597 -3.8; 3957 -3.1; 4353 -0.5; 4788 -1.4; 5267 -3.4; 5793 -7.4; 6373 -3.5; 7010 -4.0; 7711 -6.3; 8482 -6.5; 9330 -6.6; 10263 -6.6; 11289 -6.6; 12418 -6.6; 13660 -6.6; 15026 -13.8; 16529 -24.5; 18182 -29.6; 20000 -24.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW A2H V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW A2H V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.1dB**.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 65 Hz    |  0.17 | -7.7 dB  |
| Peaking | 3863 Hz  |  0.51 | 7.8 dB   |
| Peaking | 11252 Hz |  0.78 | 8.4 dB   |
| Peaking | 14045 Hz |  1.84 | 11.3 dB  |
| Peaking | 17798 Hz |  0.32 | -26.3 dB |
| Peaking | 871 Hz   |  0.97 | 6.8 dB   |
| Peaking | 1045 Hz  |  0.55 | -5.4 dB  |
| Peaking | 2602 Hz  |  2.87 | 3.1 dB   |
| Peaking | 5867 Hz  | 10.61 | -4.2 dB  |
| Peaking | 6587 Hz  |  6.69 | 3.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -7.5 dB  |
| Peaking | 62 Hz    | 1.41 | -4.8 dB  |
| Peaking | 125 Hz   | 1.41 | -6.1 dB  |
| Peaking | 250 Hz   | 1.41 | -5.3 dB  |
| Peaking | 500 Hz   | 1.41 | -1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.0 dB   |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB   |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.5 dB   |
| Peaking | 16000 Hz | 1.41 | -17.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AAW%20A2H%20V2/AAW%20A2H%20V2.png)