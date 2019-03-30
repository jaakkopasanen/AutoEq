# Audio-Technica ATH-M70x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.5; 25 -8.6; 28 -8.8; 31 -8.8; 34 -8.8; 37 -8.6; 41 -8.3; 45 -8.3; 49 -8.3; 54 -8.3; 60 -8.0; 66 -7.7; 72 -7.5; 79 -7.5; 87 -7.1; 96 -6.4; 106 -5.9; 116 -6.1; 128 -6.6; 141 -6.8; 155 -6.2; 170 -5.2; 187 -4.2; 206 -3.2; 227 -2.7; 249 -2.7; 274 -3.5; 302 -4.5; 332 -4.8; 365 -4.4; 402 -4.3; 442 -4.1; 486 -3.9; 535 -3.5; 588 -2.8; 647 -1.6; 712 -0.5; 783 -0.5; 861 -0.8; 947 -0.8; 1042 -0.7; 1146 -0.6; 1261 -0.6; 1387 -0.8; 1526 -1.2; 1678 -1.7; 1846 -2.3; 2031 -2.9; 2234 -3.7; 2457 -4.7; 2703 -5.8; 2973 -6.8; 3270 -7.7; 3597 -8.1; 3957 -8.8; 4353 -10.7; 4788 -11.5; 5267 -10.1; 5793 -7.9; 6373 -7.0; 7010 -5.8; 7711 -4.1; 8482 -4.2; 9330 -4.2; 10263 -4.2; 11289 -4.2; 12418 -4.2; 13660 -4.2; 15026 -4.2; 16529 -4.2; 18182 -4.2; 20000 -4.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.44 | -4.5 dB |
| Peaking | 231 Hz  | 1.89 | 5.1 dB  |
| Peaking | 251 Hz  | 0.61 | -3.5 dB |
| Peaking | 969 Hz  | 0.7  | 4.7 dB  |
| Peaking | 4490 Hz | 1.61 | -7.4 dB |
| Peaking | 65 Hz   | 3.13 | -0.2 dB |
| Peaking | 1996 Hz | 1.37 | 1.6 dB  |
| Peaking | 3391 Hz | 0.74 | -2.3 dB |
| Peaking | 3893 Hz | 3.68 | 2.8 dB  |
| Peaking | 8107 Hz | 1.68 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.8 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | -0.4 dB |
| Peaking | 1000 Hz  | 1.41 | 4.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.1 dB |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-M70x/Audio-Technica%20ATH-M70x.png)