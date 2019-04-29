# AAW W500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.4; 23 -6.6; 25 -6.8; 28 -7.0; 31 -7.1; 34 -7.3; 37 -7.5; 41 -7.6; 45 -7.8; 49 -8.0; 54 -8.2; 60 -8.5; 66 -8.8; 72 -9.1; 79 -9.4; 87 -9.8; 96 -10.2; 106 -10.5; 116 -10.7; 128 -10.9; 141 -11.1; 155 -11.3; 170 -11.3; 187 -11.2; 206 -11.1; 227 -11.0; 249 -10.7; 274 -10.5; 302 -10.1; 332 -9.9; 365 -9.6; 402 -9.2; 442 -8.9; 486 -8.5; 535 -8.2; 588 -7.8; 647 -7.5; 712 -7.2; 783 -6.9; 861 -6.7; 947 -6.8; 1042 -7.1; 1146 -7.7; 1261 -8.2; 1387 -8.5; 1526 -9.1; 1678 -10.3; 1846 -9.4; 2031 -5.6; 2234 -1.7; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.9; 3597 -2.2; 3957 -3.0; 4353 -0.7; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.3; 7010 -4.0; 7711 -6.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -19.4; 16529 -21.6; 18182 -13.3; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW W500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW W500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 171 Hz   | 0.48 | -4.9 dB  |
| Peaking | 1772 Hz  | 2.02 | -9.3 dB  |
| Peaking | 2383 Hz  | 1.29 | 9.3 dB   |
| Peaking | 5428 Hz  | 1.79 | 5.6 dB   |
| Peaking | 16296 Hz | 2.05 | -17.9 dB |
| Peaking | 13 Hz    | 1.35 | 0.7 dB   |
| Peaking | 850 Hz   | 3.08 | 0.6 dB   |
| Peaking | 1198 Hz  | 5.99 | -0.8 dB  |
| Peaking | 7904 Hz  | 7.14 | -1.9 dB  |
| Peaking | 13076 Hz | 4.36 | 4.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.4 dB  |
| Peaking | 125 Hz   | 1.41 | -3.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.9 dB  |
| Peaking | 500 Hz   | 1.41 | -0.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.2 dB   |
| Peaking | 8000 Hz  | 1.41 | 2.1 dB   |
| Peaking | 16000 Hz | 1.41 | -14.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AAW%20W500/AAW%20W500.png)