# Master Dynamic ME05
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.5; 23 -7.9; 25 -8.3; 28 -8.7; 31 -9.1; 34 -9.4; 37 -9.6; 41 -9.8; 45 -10.0; 49 -10.1; 54 -10.2; 60 -10.4; 66 -10.5; 72 -10.6; 79 -10.7; 87 -10.8; 96 -10.9; 106 -10.7; 116 -10.6; 128 -10.4; 141 -10.2; 155 -9.9; 170 -9.6; 187 -9.2; 206 -8.8; 227 -8.1; 249 -7.7; 274 -7.2; 302 -6.6; 332 -6.0; 365 -5.4; 402 -4.8; 442 -4.1; 486 -3.6; 535 -3.1; 588 -2.4; 647 -2.0; 712 -1.8; 783 -1.3; 861 -1.5; 947 -1.7; 1042 -2.1; 1146 -2.4; 1261 -2.6; 1387 -3.3; 1526 -3.9; 1678 -4.6; 1846 -4.8; 2031 -4.9; 2234 -5.3; 2457 -5.2; 2703 -5.5; 2973 -4.6; 3270 -2.8; 3597 -1.8; 3957 -2.9; 4353 -5.8; 4788 -7.6; 5267 -6.7; 5793 -3.7; 6373 -1.5; 7010 -0.5; 7711 -1.6; 8482 -3.0; 9330 -2.9; 10263 -1.9; 11289 -1.9; 12418 -1.9; 13660 -1.9; 15026 -1.9; 16529 -1.9; 18182 -1.9; 20000 -1.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Master Dynamic ME05 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Master Dynamic ME05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.38 | -7.2 dB |
| Peaking | 131 Hz  | 0.78 | -4.7 dB |
| Peaking | 262 Hz  | 1.37 | -2.5 dB |
| Peaking | 2219 Hz | 1.78 | -3.7 dB |
| Peaking | 4886 Hz | 4.94 | -6.2 dB |
| Peaking | 805 Hz  | 1.69 | 1.7 dB  |
| Peaking | 1719 Hz | 0.21 | -0.6 dB |
| Peaking | 3543 Hz | 6.92 | 2.2 dB  |
| Peaking | 6940 Hz | 5.05 | 2.5 dB  |
| Peaking | 8819 Hz | 7.23 | -1.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -6.7 dB |
| Peaking | 62 Hz    | 1.41 | -6.7 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.2 dB |
| Peaking | 4000 Hz  | 1.41 | -2.4 dB |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Master%20Dynamic%20ME05/Master%20Dynamic%20ME05.png)