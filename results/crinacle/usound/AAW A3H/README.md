# AAW A3H
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.5; 25 -4.9; 28 -5.4; 31 -5.8; 34 -6.2; 37 -6.4; 41 -6.8; 45 -7.0; 49 -7.3; 54 -7.5; 60 -7.8; 66 -8.1; 72 -8.4; 79 -8.7; 87 -8.9; 96 -9.3; 106 -9.6; 116 -9.8; 128 -10.0; 141 -10.2; 155 -10.3; 170 -10.3; 187 -10.3; 206 -10.3; 227 -10.2; 249 -10.1; 274 -9.9; 302 -9.8; 332 -9.5; 365 -9.3; 402 -9.1; 442 -8.8; 486 -8.5; 535 -8.2; 588 -7.9; 647 -7.5; 712 -7.0; 783 -6.5; 861 -6.0; 947 -5.8; 1042 -5.7; 1146 -6.2; 1261 -7.0; 1387 -7.4; 1526 -7.4; 1678 -6.9; 1846 -6.2; 2031 -5.6; 2234 -5.1; 2457 -5.0; 2703 -4.7; 2973 -3.3; 3270 -1.4; 3597 -0.5; 3957 -1.8; 4353 -4.0; 4788 -4.8; 5267 -4.4; 5793 -3.7; 6373 -2.9; 7010 -3.8; 7711 -6.1; 8482 -6.3; 9330 -6.3; 10263 -6.3; 11289 -6.3; 12418 -6.3; 13660 -6.3; 15026 -6.3; 16529 -6.3; 18182 -6.3; 20000 -6.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW A3H GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW A3H ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.4  | 2.7 dB  |
| Peaking | 153 Hz  | 0.58 | -3.8 dB |
| Peaking | 358 Hz  | 1.22 | -1.4 dB |
| Peaking | 3534 Hz | 2.76 | 6.0 dB  |
| Peaking | 6403 Hz | 4.44 | 3.4 dB  |
| Peaking | 1009 Hz | 1.9  | 3.0 dB  |
| Peaking | 1293 Hz | 0.97 | -2.5 dB |
| Peaking | 2113 Hz | 2.14 | 1.4 dB  |
| Peaking | 8207 Hz | 5.43 | -0.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -3.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.6 dB |
| Peaking | 1000 Hz  | 1.41 | 0.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AAW%20A3H/AAW%20A3H.png)