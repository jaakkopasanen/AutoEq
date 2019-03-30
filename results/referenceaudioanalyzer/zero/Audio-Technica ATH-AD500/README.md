# Audio-Technica ATH-AD500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.6; 31 -1.3; 34 -2.3; 37 -3.2; 41 -4.2; 45 -5.0; 49 -5.6; 54 -6.1; 60 -6.2; 66 -6.4; 72 -6.7; 79 -7.1; 87 -7.6; 96 -7.9; 106 -8.1; 116 -8.3; 128 -8.5; 141 -8.5; 155 -8.4; 170 -8.2; 187 -8.0; 206 -7.6; 227 -7.1; 249 -6.6; 274 -5.9; 302 -5.0; 332 -3.7; 365 -2.1; 402 -1.0; 442 -1.9; 486 -4.0; 535 -5.8; 588 -7.0; 647 -7.7; 712 -7.8; 783 -7.8; 861 -7.7; 947 -7.5; 1042 -7.4; 1146 -7.0; 1261 -6.6; 1387 -6.5; 1526 -6.2; 1678 -6.5; 1846 -6.5; 2031 -6.5; 2234 -6.5; 2457 -6.5; 2703 -6.1; 2973 -5.2; 3270 -3.8; 3597 -3.3; 3957 -3.6; 4353 -2.2; 4788 -0.5; 5267 -0.7; 5793 -7.1; 6373 -9.7; 7010 -10.5; 7711 -12.4; 8482 -14.5; 9330 -14.5; 10263 -12.5; 11289 -11.0; 12418 -10.4; 13660 -8.7; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 24 Hz    |  0.97 | 6.7 dB  |
| Peaking | 243 Hz   |  0.25 | -2.5 dB |
| Peaking | 391 Hz   |  2.02 | 7.9 dB  |
| Peaking | 4784 Hz  |  1.77 | 8.8 dB  |
| Peaking | 8492 Hz  |  1.08 | -9.2 dB |
| Peaking | 722 Hz   |  1.46 | -1.6 dB |
| Peaking | 1172 Hz  |  0.35 | 0.9 dB  |
| Peaking | 2330 Hz  |  3.09 | -0.9 dB |
| Peaking | 6082 Hz  | 10.42 | -2.4 dB |
| Peaking | 15235 Hz |  3.47 | 1.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | 0.6 dB  |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | 6.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -8.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-AD500/Audio-Technica%20ATH-AD500.png)