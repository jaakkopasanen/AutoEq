# Rhapsodio Clipper
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.2; 23 -9.5; 25 -9.7; 28 -9.9; 31 -10.1; 34 -10.2; 37 -10.3; 41 -10.4; 45 -10.6; 49 -10.6; 54 -10.7; 60 -10.8; 66 -11.0; 72 -11.1; 79 -11.2; 87 -11.4; 96 -11.5; 106 -11.6; 116 -11.7; 128 -11.6; 141 -11.5; 155 -11.4; 170 -11.2; 187 -10.9; 206 -10.5; 227 -10.1; 249 -9.6; 274 -9.0; 302 -8.4; 332 -7.9; 365 -7.2; 402 -6.6; 442 -6.0; 486 -5.3; 535 -4.7; 588 -4.1; 647 -3.4; 712 -2.7; 783 -2.0; 861 -1.3; 947 -0.5; 1042 -0.5; 1146 -1.5; 1261 -2.1; 1387 -2.4; 1526 -2.4; 1678 -2.3; 1846 -2.2; 2031 -2.6; 2234 -3.4; 2457 -4.8; 2703 -6.1; 2973 -6.4; 3270 -5.7; 3597 -5.1; 3957 -5.5; 4353 -7.7; 4788 -11.2; 5267 -8.4; 5793 -2.9; 6373 -0.6; 7010 -3.0; 7711 -5.3; 8482 -5.4; 9330 -5.5; 10263 -5.5; 11289 -5.5; 12418 -5.5; 13660 -5.5; 15026 -5.5; 16529 -5.5; 18182 -5.5; 20000 -5.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Rhapsodio Clipper GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Rhapsodio Clipper ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.39 | -3.7 dB |
| Peaking | 151 Hz  | 0.49 | -5.4 dB |
| Peaking | 991 Hz  | 0.82 | 5.1 dB  |
| Peaking | 4878 Hz | 4.73 | -7.2 dB |
| Peaking | 6263 Hz | 4.53 | 6.0 dB  |
| Peaking | 1358 Hz | 3.19 | -1.4 dB |
| Peaking | 2093 Hz | 1.29 | 2.1 dB  |
| Peaking | 2782 Hz | 2.48 | -3.1 dB |
| Peaking | 3735 Hz | 4.76 | 0.9 dB  |
| Peaking | 7827 Hz | 6.32 | -0.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | -4.0 dB |
| Peaking | 125 Hz   | 1.41 | -5.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.4 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Rhapsodio%20Clipper/Rhapsodio%20Clipper.png)