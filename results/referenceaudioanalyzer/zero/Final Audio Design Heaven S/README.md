# Final Audio Design Heaven S
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -11.0; 23 -11.1; 25 -11.3; 28 -11.5; 31 -11.6; 34 -11.7; 37 -11.7; 41 -11.8; 45 -11.7; 49 -11.7; 54 -11.7; 60 -11.7; 66 -11.6; 72 -11.4; 79 -11.4; 87 -11.1; 96 -11.1; 106 -10.8; 116 -10.6; 128 -10.3; 141 -10.0; 155 -9.7; 170 -9.4; 187 -9.1; 206 -8.7; 227 -8.3; 249 -8.0; 274 -7.7; 302 -7.3; 332 -6.9; 365 -6.5; 402 -6.1; 442 -5.7; 486 -5.3; 535 -4.9; 588 -4.6; 647 -4.2; 712 -3.8; 783 -3.5; 861 -3.1; 947 -2.8; 1042 -2.5; 1146 -2.3; 1261 -2.2; 1387 -2.0; 1526 -2.0; 1678 -2.0; 1846 -2.4; 2031 -3.0; 2234 -4.1; 2457 -6.2; 2703 -8.6; 2973 -10.6; 3270 -9.8; 3597 -6.7; 3957 -3.5; 4353 -1.4; 4788 -0.5; 5267 -1.2; 5793 -4.2; 6373 -7.7; 7010 -8.2; 7711 -6.9; 8482 -7.0; 9330 -7.0; 10263 -5.8; 11289 -5.8; 12418 -5.8; 13660 -5.8; 15026 -5.8; 16529 -5.8; 18182 -5.8; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Final Audio Design Heaven S GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Final Audio Design Heaven S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.54 | -3.6 dB |
| Peaking | 84 Hz   | 0.39 | -4.7 dB |
| Peaking | 1363 Hz | 0.67 | 4.4 dB  |
| Peaking | 3016 Hz | 3.06 | -7.4 dB |
| Peaking | 4667 Hz | 3.91 | 6.1 dB  |
| Peaking | 4006 Hz | 7.73 | 1.5 dB  |
| Peaking | 5496 Hz | 4.81 | 4.5 dB  |
| Peaking | 6321 Hz | 1.91 | -4.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -5.8 dB |
| Peaking | 62 Hz    | 1.41 | -4.6 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Final%20Audio%20Design%20Heaven%20S/Final%20Audio%20Design%20Heaven%20S.png)