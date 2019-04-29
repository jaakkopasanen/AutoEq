# AAW A3H
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.3; 23 -5.8; 25 -6.2; 28 -6.7; 31 -7.1; 34 -7.5; 37 -7.7; 41 -8.1; 45 -8.3; 49 -8.6; 54 -8.8; 60 -9.1; 66 -9.4; 72 -9.7; 79 -10.0; 87 -10.2; 96 -10.6; 106 -10.9; 116 -11.1; 128 -11.3; 141 -11.5; 155 -11.6; 170 -11.6; 187 -11.6; 206 -11.6; 227 -11.5; 249 -11.4; 274 -11.2; 302 -11.0; 332 -10.7; 365 -10.3; 402 -10.1; 442 -9.8; 486 -9.5; 535 -9.1; 588 -8.7; 647 -8.3; 712 -7.8; 783 -7.3; 861 -6.9; 947 -6.7; 1042 -6.7; 1146 -7.1; 1261 -7.6; 1387 -7.7; 1526 -7.4; 1678 -6.9; 1846 -6.2; 2031 -5.2; 2234 -4.1; 2457 -3.5; 2703 -2.7; 2973 -1.2; 3270 -0.5; 3597 -0.5; 3957 -0.7; 4353 -3.0; 4788 -4.1; 5267 -3.7; 5793 -2.8; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.3; 16529 -10.3; 18182 -7.8; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW A3H GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW A3H ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 100 Hz   | 0.64 | -2.8 dB |
| Peaking | 251 Hz   | 0.6  | -4.0 dB |
| Peaking | 3387 Hz  | 1.45 | 7.4 dB  |
| Peaking | 6373 Hz  | 3.8  | 4.7 dB  |
| Peaking | 11253 Hz | 0.08 | -1.2 dB |
| Peaking | 18 Hz    | 2.23 | 1.7 dB  |
| Peaking | 934 Hz   | 3.17 | 1.0 dB  |
| Peaking | 1414 Hz  | 3.64 | -1.2 dB |
| Peaking | 13697 Hz | 1.37 | 1.8 dB  |
| Peaking | 16238 Hz | 2.24 | -3.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.5 dB |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/harman_in-ear_2017-1/AAW%20A3H/AAW%20A3H.png)