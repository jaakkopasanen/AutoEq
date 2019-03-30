# Audio-Technica ATH-PRO5 MK2
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.6; 25 -7.2; 28 -8.0; 31 -8.7; 34 -9.3; 37 -9.8; 41 -10.5; 45 -11.0; 49 -11.5; 54 -11.7; 60 -11.9; 66 -12.1; 72 -12.2; 79 -12.1; 87 -11.9; 96 -11.7; 106 -11.2; 116 -10.8; 128 -10.7; 141 -10.7; 155 -10.7; 170 -10.7; 187 -10.4; 206 -10.1; 227 -9.5; 249 -8.8; 274 -8.1; 302 -7.2; 332 -6.0; 365 -4.5; 402 -3.3; 442 -3.1; 486 -3.8; 535 -5.0; 588 -6.2; 647 -7.4; 712 -8.4; 783 -9.3; 861 -9.8; 947 -9.7; 1042 -9.0; 1146 -7.6; 1261 -6.1; 1387 -4.2; 1526 -1.9; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.9; 2973 -7.6; 3270 -11.8; 3597 -12.3; 3957 -10.6; 4353 -9.1; 4788 -7.9; 5267 -7.0; 5793 -8.3; 6373 -11.0; 7010 -11.6; 7711 -9.0; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-PRO5 MK2 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-PRO5 MK2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 0.78 | -5.9 dB |
| Peaking | 176 Hz  | 2.14 | -2.9 dB |
| Peaking | 2291 Hz | 1.65 | 8.7 dB  |
| Peaking | 3455 Hz | 2.84 | -9.3 dB |
| Peaking | 6796 Hz | 4.5  | -5.8 dB |
| Peaking | 18 Hz   | 2.46 | 1.6 dB  |
| Peaking | 444 Hz  | 2.5  | 4.9 dB  |
| Peaking | 960 Hz  | 1.22 | -5.0 dB |
| Peaking | 1619 Hz | 1.69 | 4.2 dB  |
| Peaking | 2132 Hz | 5.38 | -2.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -5.3 dB |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.9 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -5.5 dB |
| Peaking | 2000 Hz  | 1.41 | 9.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -5.9 dB |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | 0.3 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-PRO5%20MK2/Audio-Technica%20ATH-PRO5%20MK2.png)