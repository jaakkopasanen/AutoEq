# Audio-Technica ATH-CK9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.3; 23 -4.9; 25 -5.4; 28 -6.0; 31 -6.5; 34 -6.9; 37 -7.2; 41 -7.5; 45 -7.7; 49 -7.8; 54 -8.0; 60 -8.2; 66 -8.3; 72 -8.3; 79 -8.4; 87 -8.6; 96 -8.6; 106 -8.5; 116 -8.5; 128 -8.4; 141 -8.2; 155 -8.3; 170 -8.3; 187 -8.2; 206 -8.4; 227 -8.6; 249 -8.4; 274 -8.3; 302 -8.3; 332 -8.1; 365 -7.9; 402 -7.9; 442 -8.1; 486 -8.3; 535 -8.2; 588 -8.0; 647 -7.9; 712 -7.9; 783 -7.8; 861 -7.9; 947 -7.7; 1042 -7.8; 1146 -7.9; 1261 -7.8; 1387 -7.6; 1526 -7.6; 1678 -7.4; 1846 -7.2; 2031 -7.0; 2234 -6.8; 2457 -6.4; 2703 -6.0; 2973 -6.0; 3270 -6.0; 3597 -6.7; 3957 -7.3; 4353 -6.7; 4788 -5.6; 5267 -4.2; 5793 -2.0; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-CK9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-CK9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.18 | 3.6 dB  |
| Peaking | 110 Hz  | 0.13 | -2.5 dB |
| Peaking | 1315 Hz | 1.22 | -1.1 dB |
| Peaking | 3988 Hz | 5.54 | -1.6 dB |
| Peaking | 6191 Hz | 4.37 | 6.1 dB  |
| Peaking | 6789 Hz | 9.2  | 1.2 dB  |
| Peaking | 7651 Hz | 2.95 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.1 dB  |
| Peaking | 62 Hz    | 1.41 | -2.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -1.6 dB |
| Peaking | 2000 Hz  | 1.41 | -0.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.9 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-CK9/Audio-Technica%20ATH-CK9.png)