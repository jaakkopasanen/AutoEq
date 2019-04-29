# Advanced Elise
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.6; 25 -10.8; 28 -11.2; 31 -11.4; 34 -11.6; 37 -11.7; 41 -12.0; 45 -12.1; 49 -12.3; 54 -12.5; 60 -12.7; 66 -12.9; 72 -13.1; 79 -13.4; 87 -13.6; 96 -13.8; 106 -14.1; 116 -14.2; 128 -14.2; 141 -14.3; 155 -14.2; 170 -14.0; 187 -13.7; 206 -13.4; 227 -13.0; 249 -12.6; 274 -12.0; 302 -11.5; 332 -10.9; 365 -10.3; 402 -9.6; 442 -8.9; 486 -8.2; 535 -7.4; 588 -6.6; 647 -5.7; 712 -4.8; 783 -3.8; 861 -2.9; 947 -2.1; 1042 -1.8; 1146 -1.8; 1261 -2.1; 1387 -2.5; 1526 -2.5; 1678 -2.4; 1846 -1.8; 2031 -1.0; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -1.2; 3597 -1.8; 3957 -2.1; 4353 -2.0; 4788 -1.8; 5267 -1.8; 5793 -2.7; 6373 -5.4; 7010 -10.3; 7711 -10.5; 8482 -7.8; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -8.3; 18182 -11.9; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Advanced Elise GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Advanced Elise ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.36 | -3.6 dB |
| Peaking | 163 Hz   | 0.43 | -6.9 dB |
| Peaking | 984 Hz   | 1.1  | 4.6 dB  |
| Peaking | 2859 Hz  | 0.93 | 6.0 dB  |
| Peaking | 18947 Hz | 1.06 | -6.1 dB |
| Peaking | 1472 Hz  | 3.34 | -0.2 dB |
| Peaking | 3604 Hz  | 2.43 | -1.5 dB |
| Peaking | 5730 Hz  | 1.51 | 4.2 dB  |
| Peaking | 7243 Hz  | 3.28 | -8.2 dB |
| Peaking | 15184 Hz | 2.91 | 1.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.6 dB |
| Peaking | 250 Hz   | 1.41 | -5.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.2 dB |
| Peaking | 1000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 2000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.7 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Advanced%20Elise/Advanced%20Elise.png)