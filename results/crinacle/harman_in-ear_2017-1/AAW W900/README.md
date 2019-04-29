# AAW W900
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.3; 23 -6.5; 25 -6.6; 28 -6.8; 31 -7.0; 34 -7.1; 37 -7.2; 41 -7.3; 45 -7.4; 49 -7.5; 54 -7.6; 60 -7.8; 66 -8.0; 72 -8.2; 79 -8.4; 87 -8.7; 96 -9.0; 106 -9.3; 116 -9.4; 128 -9.6; 141 -9.8; 155 -9.9; 170 -9.9; 187 -9.9; 206 -9.8; 227 -9.8; 249 -9.7; 274 -9.7; 302 -9.6; 332 -9.4; 365 -9.3; 402 -9.3; 442 -9.3; 486 -9.3; 535 -9.4; 588 -9.5; 647 -9.6; 712 -9.8; 783 -10.0; 861 -10.3; 947 -10.7; 1042 -11.0; 1146 -11.0; 1261 -10.3; 1387 -8.8; 1526 -7.2; 1678 -6.2; 1846 -6.1; 2031 -6.2; 2234 -5.5; 2457 -3.9; 2703 -2.4; 2973 -1.8; 3270 -1.7; 3597 -0.8; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.8; 13660 -19.9; 15026 -32.2; 16529 -33.4; 18182 -31.8; 20000 -33.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW W900 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW W900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 167 Hz   | 0.5  | -3.3 dB  |
| Peaking | 541 Hz   | 0.56 | -3.1 dB  |
| Peaking | 1143 Hz  | 0.88 | -7.6 dB  |
| Peaking | 7528 Hz  | 0.17 | 27.9 dB  |
| Peaking | 16786 Hz | 0.23 | -46.0 dB |
| Peaking | 2157 Hz  | 4.92 | -2.1 dB  |
| Peaking | 7185 Hz  | 0.41 | 1.4 dB   |
| Peaking | 7889 Hz  | 2.66 | -5.2 dB  |
| Peaking | 12410 Hz | 2.83 | 9.5 dB   |
| Peaking | 14666 Hz | 3.12 | -10.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB  |
| Peaking | 125 Hz   | 1.41 | -2.7 dB  |
| Peaking | 250 Hz   | 1.41 | -2.6 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -4.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 10.0 dB  |
| Peaking | 16000 Hz | 1.41 | -36.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AAW%20W900/AAW%20W900.png)