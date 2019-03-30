# Pioneer SE-DJ5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.8; 116 -1.1; 128 -1.1; 141 -1.1; 155 -1.1; 170 -1.1; 187 -0.9; 206 -0.8; 227 -0.8; 249 -1.1; 274 -2.1; 302 -3.8; 332 -5.5; 365 -6.8; 402 -7.8; 442 -8.4; 486 -8.8; 535 -9.0; 588 -9.2; 647 -9.2; 712 -9.2; 783 -9.2; 861 -9.0; 947 -8.9; 1042 -8.9; 1146 -8.6; 1261 -8.4; 1387 -8.1; 1526 -7.8; 1678 -7.7; 1846 -7.9; 2031 -7.7; 2234 -6.9; 2457 -5.2; 2703 -2.1; 2973 -0.5; 3270 -0.5; 3597 -3.7; 3957 -8.3; 4353 -10.9; 4788 -11.8; 5267 -11.6; 5793 -10.7; 6373 -10.4; 7010 -11.8; 7711 -12.8; 8482 -13.0; 9330 -13.0; 10263 -12.7; 11289 -13.0; 12418 -14.3; 13660 -13.9; 15026 -9.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Pioneer SE-DJ5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-DJ5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 50 Hz    | 0.26 | 6.6 dB  |
| Peaking | 223 Hz   | 1.56 | 5.2 dB  |
| Peaking | 1555 Hz  | 0.11 | -3.3 dB |
| Peaking | 3035 Hz  | 2.56 | 11.0 dB |
| Peaking | 10703 Hz | 0.62 | -5.5 dB |
| Peaking | 498 Hz   | 1.36 | -1.7 dB |
| Peaking | 4241 Hz  | 0.05 | 0.8 dB  |
| Peaking | 4542 Hz  | 3.64 | -3.4 dB |
| Peaking | 13664 Hz | 2.65 | -4.1 dB |
| Peaking | 16289 Hz | 1.74 | 2.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 4.3 dB  |
| Peaking | 250 Hz   | 1.41 | 5.1 dB  |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | -2.6 dB |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.8 dB |
| Peaking | 16000 Hz | 1.41 | -3.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Pioneer%20SE-DJ5000/Pioneer%20SE-DJ5000.png)