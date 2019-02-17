# Sony XBA-N3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.3; 23 -7.5; 25 -7.7; 28 -7.8; 31 -7.9; 34 -8.0; 37 -8.0; 41 -8.0; 45 -8.0; 49 -8.0; 54 -8.0; 60 -8.0; 66 -7.9; 72 -7.9; 79 -7.9; 87 -7.8; 96 -7.6; 106 -7.3; 116 -7.7; 128 -8.1; 141 -8.0; 155 -7.9; 170 -7.5; 187 -7.2; 206 -6.8; 227 -6.4; 249 -6.0; 274 -5.6; 302 -5.2; 332 -4.8; 365 -4.5; 402 -4.2; 442 -3.9; 486 -3.7; 535 -3.5; 588 -3.3; 647 -3.2; 712 -3.0; 783 -2.9; 861 -3.0; 947 -3.2; 1042 -3.7; 1146 -4.3; 1261 -4.8; 1387 -5.0; 1526 -4.0; 1678 -3.3; 1846 -3.5; 2031 -3.5; 2234 -3.2; 2457 -2.6; 2703 -1.8; 2973 -1.1; 3270 -1.0; 3597 -2.4; 3957 -3.3; 4353 -1.4; 4788 -2.2; 5267 -1.7; 5793 -0.5; 6373 -1.1; 7010 -4.5; 7711 -6.6; 8482 -6.8; 9330 -5.5; 10263 -4.6; 11289 -4.7; 12418 -3.7; 13660 -3.6; 15026 -6.3; 16529 -7.9; 18182 -4.9; 20000 -3.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Sony XBA-N3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony XBA-N3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-2.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 39 Hz    | 0.34 | -4.5 dB |
| Peaking | 163 Hz   | 1.05 | -2.7 dB |
| Peaking | 6622 Hz  | 1.07 | 6.1 dB  |
| Peaking | 7910 Hz  | 1.84 | -8.4 dB |
| Peaking | 16427 Hz | 2    | -5.0 dB |
| Peaking | 756 Hz   | 1.69 | 0.9 dB  |
| Peaking | 1308 Hz  | 3.51 | -1.8 dB |
| Peaking | 3133 Hz  | 3.01 | 4.0 dB  |
| Peaking | 3522 Hz  | 1.73 | -2.4 dB |
| Peaking | 6109 Hz  | 8.95 | 1.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -0.3 dB |
| Peaking | 4000 Hz  | 1.41 | 2.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.9 dB |
| Peaking | 16000 Hz | 1.41 | -3.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/usound/Sony%20XBA-N3/Sony%20XBA-N3.png)