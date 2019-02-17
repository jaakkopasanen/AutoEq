# Bose QuietComfort 35
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.9; 23 -6.4; 25 -6.1; 28 -5.9; 31 -5.9; 34 -5.9; 37 -6.0; 41 -6.1; 45 -6.2; 49 -6.2; 54 -6.1; 60 -6.0; 66 -6.0; 72 -5.9; 79 -5.9; 87 -5.9; 96 -5.8; 106 -5.8; 116 -5.8; 128 -5.7; 141 -5.6; 155 -5.5; 170 -5.4; 187 -5.2; 206 -5.0; 227 -4.8; 249 -4.6; 274 -4.4; 302 -4.3; 332 -4.1; 365 -3.9; 402 -3.8; 442 -3.7; 486 -3.6; 535 -3.4; 588 -3.0; 647 -2.6; 712 -2.2; 783 -1.8; 861 -1.3; 947 -1.0; 1042 -0.8; 1146 -0.7; 1261 -1.2; 1387 -2.8; 1526 -4.4; 1678 -6.5; 1846 -8.6; 2031 -8.9; 2234 -7.0; 2457 -5.8; 2703 -6.8; 2973 -6.8; 3270 -5.3; 3597 -5.5; 3957 -6.6; 4353 -5.4; 4788 -3.4; 5267 -0.5; 5793 -5.5; 6373 -9.4; 7010 -4.5; 7711 -1.0; 8482 -0.9; 9330 -0.9; 10263 -0.9; 11289 -3.2; 12418 -8.4; 13660 -8.6; 15026 -7.6; 16529 -5.4; 18182 -3.8; 20000 -5.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.09 | -5.3 dB |
| Peaking | 1935 Hz  | 3.48 | -6.5 dB |
| Peaking | 3539 Hz  | 0.95 | -4.8 dB |
| Peaking | 13263 Hz | 3.04 | -6.5 dB |
| Peaking | 16408 Hz | 0.97 | -4.6 dB |
| Peaking | 1082 Hz  | 2.12 | 2.4 dB  |
| Peaking | 5231 Hz  | 5.77 | 5.2 dB  |
| Peaking | 6232 Hz  | 4.85 | -8.4 dB |
| Peaking | 8506 Hz  | 1.4  | 3.3 dB  |
| Peaking | 11978 Hz | 0.02 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.2 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.8 dB |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 2.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | -8.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2035/Bose%20QuietComfort%2035.png)