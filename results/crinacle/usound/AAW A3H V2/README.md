# AAW A3H V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.3; 25 -5.6; 28 -6.0; 31 -6.2; 34 -6.4; 37 -6.6; 41 -6.8; 45 -7.1; 49 -7.2; 54 -7.4; 60 -7.7; 66 -8.0; 72 -8.3; 79 -8.6; 87 -8.9; 96 -9.3; 106 -9.6; 116 -9.8; 128 -10.0; 141 -10.2; 155 -10.4; 170 -10.4; 187 -10.4; 206 -10.3; 227 -10.2; 249 -10.1; 274 -9.9; 302 -9.8; 332 -9.6; 365 -9.4; 402 -9.2; 442 -8.9; 486 -8.7; 535 -8.5; 588 -8.2; 647 -7.9; 712 -7.4; 783 -7.0; 861 -6.6; 947 -6.5; 1042 -6.6; 1146 -7.3; 1261 -8.2; 1387 -8.9; 1526 -9.2; 1678 -9.3; 1846 -9.3; 2031 -9.1; 2234 -8.2; 2457 -6.5; 2703 -4.8; 2973 -3.9; 3270 -4.3; 3597 -3.5; 3957 -0.6; 4353 -0.5; 4788 -2.8; 5267 -3.1; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW A3H V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW A3H V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.83 | 2.3 dB  |
| Peaking | 184 Hz  | 0.48 | -4.0 dB |
| Peaking | 1750 Hz | 2.24 | -3.4 dB |
| Peaking | 4099 Hz | 2.21 | 5.7 dB  |
| Peaking | 6105 Hz | 4.64 | 5.3 dB  |
| Peaking | 929 Hz  | 1.93 | 2.5 dB  |
| Peaking | 959 Hz  | 0.92 | -1.5 dB |
| Peaking | 2871 Hz | 5.58 | 1.8 dB  |
| Peaking | 3504 Hz | 9.75 | -1.4 dB |
| Peaking | 8247 Hz | 4.47 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -1.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AAW%20A3H%20V2/AAW%20A3H%20V2.png)