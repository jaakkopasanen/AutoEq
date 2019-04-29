# AAW A2H V2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.6; 23 -11.6; 25 -11.6; 28 -11.6; 31 -11.6; 34 -11.5; 37 -11.5; 41 -11.4; 45 -11.3; 49 -11.3; 54 -11.2; 60 -11.3; 66 -11.3; 72 -11.4; 79 -11.4; 87 -11.5; 96 -11.6; 106 -11.7; 116 -11.7; 128 -11.7; 141 -11.7; 155 -11.6; 170 -11.5; 187 -11.3; 206 -11.0; 227 -10.7; 249 -10.4; 274 -10.0; 302 -9.6; 332 -9.2; 365 -8.7; 402 -8.2; 442 -7.7; 486 -7.2; 535 -6.6; 588 -6.0; 647 -5.4; 712 -4.7; 783 -4.0; 861 -3.4; 947 -3.1; 1042 -3.1; 1146 -3.6; 1261 -4.2; 1387 -4.7; 1526 -4.7; 1678 -4.5; 1846 -4.0; 2031 -3.3; 2234 -2.3; 2457 -1.3; 2703 -0.5; 2973 -0.6; 3270 -2.0; 3597 -4.7; 3957 -3.5; 4353 -0.5; 4788 -1.2; 5267 -3.1; 5793 -7.4; 6373 -3.9; 7010 -2.9; 7711 -5.1; 8482 -5.4; 9330 -5.4; 10263 -5.4; 11289 -5.4; 12418 -5.4; 13660 -5.4; 15026 -5.4; 16529 -5.8; 18182 -12.0; 20000 -11.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`AAW A2H V2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AAW A2H V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 62 Hz    | 0.13 | -6.3 dB |
| Peaking | 833 Hz   | 1.43 | 3.3 dB  |
| Peaking | 3035 Hz  | 0.95 | 4.0 dB  |
| Peaking | 16137 Hz | 1.32 | 3.6 dB  |
| Peaking | 18861 Hz | 0.8  | -8.6 dB |
| Peaking | 2993 Hz  | 2.61 | 4.6 dB  |
| Peaking | 3716 Hz  | 1.72 | -6.6 dB |
| Peaking | 4413 Hz  | 3.86 | 6.7 dB  |
| Peaking | 16972 Hz | 2.85 | 0.7 dB  |
| Peaking | 17430 Hz | 3.2  | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.3 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -1.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/AAW%20A2H%20V2/AAW%20A2H%20V2.png)