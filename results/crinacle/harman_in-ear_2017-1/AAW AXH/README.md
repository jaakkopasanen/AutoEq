# AAW AXH
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -4.7; 25 -4.7; 28 -4.8; 31 -5.0; 34 -5.1; 37 -5.2; 41 -5.4; 45 -5.5; 49 -5.6; 54 -5.7; 60 -5.8; 66 -5.9; 72 -6.1; 79 -6.3; 87 -6.5; 96 -6.8; 106 -7.0; 116 -7.2; 128 -7.4; 141 -7.6; 155 -7.8; 170 -8.0; 187 -8.1; 206 -8.2; 227 -8.2; 249 -8.3; 274 -8.4; 302 -8.4; 332 -8.3; 365 -8.2; 402 -8.3; 442 -8.3; 486 -8.3; 535 -8.2; 588 -8.0; 647 -7.9; 712 -7.6; 783 -7.3; 861 -7.0; 947 -7.0; 1042 -7.2; 1146 -7.6; 1261 -7.8; 1387 -7.5; 1526 -6.8; 1678 -5.9; 1846 -5.3; 2031 -4.9; 2234 -4.5; 2457 -3.7; 2703 -2.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -1.1; 5267 -6.9; 5793 -8.8; 6373 -12.8; 7010 -16.1; 7711 -11.9; 8482 -6.8; 9330 -6.6; 10263 -8.0; 11289 -8.3; 12418 -11.7; 13660 -21.0; 15026 -32.3; 16529 -38.3; 18182 -34.1; 20000 -21.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW AXH GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW AXH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.75 | 1.8 dB   |
| Peaking | 825 Hz   | 0.35 | -6.8 dB  |
| Peaking | 6806 Hz  | 3.14 | -18.4 dB |
| Peaking | 7156 Hz  | 0.21 | 29.4 dB  |
| Peaking | 16576 Hz | 0.37 | -50.2 dB |
| Peaking | 1513 Hz  | 2.18 | -1.7 dB  |
| Peaking | 4056 Hz  | 1.6  | 2.3 dB   |
| Peaking | 5464 Hz  | 5.35 | -4.7 dB  |
| Peaking | 11964 Hz | 2.93 | 5.3 dB   |
| Peaking | 14899 Hz | 2.98 | -6.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 1.8 dB   |
| Peaking | 62 Hz    | 1.41 | 0.6 dB   |
| Peaking | 125 Hz   | 1.41 | -0.8 dB  |
| Peaking | 250 Hz   | 1.41 | -1.7 dB  |
| Peaking | 500 Hz   | 1.41 | -1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB   |
| Peaking | 4000 Hz  | 1.41 | 7.7 dB   |
| Peaking | 8000 Hz  | 1.41 | 3.0 dB   |
| Peaking | 16000 Hz | 1.41 | -37.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AAW%20AXH/AAW%20AXH.png)