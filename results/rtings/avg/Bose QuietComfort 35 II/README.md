# Bose QuietComfort 35 II
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.8; 23 -7.2; 25 -6.8; 28 -6.5; 31 -6.4; 34 -6.4; 37 -6.4; 41 -6.4; 45 -6.5; 49 -6.5; 54 -6.4; 60 -6.4; 66 -6.3; 72 -6.2; 79 -6.2; 87 -6.1; 96 -6.1; 106 -6.0; 116 -6.0; 128 -5.9; 141 -5.8; 155 -5.8; 170 -5.6; 187 -5.4; 206 -5.2; 227 -4.9; 249 -4.7; 274 -4.6; 302 -4.5; 332 -4.3; 365 -4.1; 402 -4.0; 442 -3.9; 486 -3.9; 535 -3.7; 588 -3.5; 647 -3.2; 712 -2.9; 783 -2.6; 861 -2.2; 947 -2.2; 1042 -2.0; 1146 -1.5; 1261 -1.3; 1387 -1.8; 1526 -2.4; 1678 -4.0; 1846 -5.8; 2031 -7.1; 2234 -6.6; 2457 -5.2; 2703 -4.2; 2973 -3.7; 3270 -2.2; 3597 -4.9; 3957 -6.8; 4353 -5.4; 4788 -3.5; 5267 -0.5; 5793 -3.6; 6373 -8.2; 7010 -3.7; 7711 -3.7; 8482 -3.9; 9330 -4.0; 10263 -4.0; 11289 -4.0; 12418 -6.3; 13660 -7.8; 15026 -7.3; 16529 -4.8; 18182 -4.0; 20000 -4.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Bose QuietComfort 35 II GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose QuietComfort 35 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 1.41 | -4.2 dB |
| Peaking | 69 Hz    | 0.36 | -2.3 dB |
| Peaking | 1262 Hz  | 1.02 | 3.1 dB  |
| Peaking | 2030 Hz  | 2.9  | -4.8 dB |
| Peaking | 14163 Hz | 2.25 | -4.3 dB |
| Peaking | 3319 Hz  | 5.57 | 3.3 dB  |
| Peaking | 3863 Hz  | 3.75 | -4.0 dB |
| Peaking | 5441 Hz  | 5.65 | 6.2 dB  |
| Peaking | 6212 Hz  | 5.45 | -7.3 dB |
| Peaking | 7139 Hz  | 3.26 | 2.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -2.8 dB |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 3.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | -0.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -3.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Bose%20QuietComfort%2035%20II/Bose%20QuietComfort%2035%20II.png)