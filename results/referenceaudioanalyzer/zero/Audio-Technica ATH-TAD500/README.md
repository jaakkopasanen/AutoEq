# Audio-Technica ATH-TAD500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.9; 45 -1.5; 49 -2.0; 54 -2.6; 60 -3.1; 66 -3.5; 72 -3.8; 79 -4.1; 87 -4.4; 96 -4.6; 106 -4.8; 116 -5.0; 128 -5.2; 141 -5.3; 155 -5.3; 170 -5.3; 187 -5.3; 206 -5.3; 227 -5.2; 249 -4.8; 274 -4.7; 302 -4.7; 332 -4.8; 365 -5.0; 402 -5.0; 442 -5.0; 486 -5.0; 535 -5.3; 588 -5.3; 647 -5.6; 712 -5.6; 783 -5.9; 861 -6.2; 947 -6.6; 1042 -7.0; 1146 -7.3; 1261 -7.7; 1387 -8.1; 1526 -8.5; 1678 -8.8; 1846 -9.5; 2031 -10.1; 2234 -9.9; 2457 -9.0; 2703 -7.6; 2973 -6.1; 3270 -4.9; 3597 -5.9; 3957 -8.5; 4353 -10.0; 4788 -10.2; 5267 -9.9; 5793 -9.6; 6373 -9.5; 7010 -8.2; 7711 -6.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-TAD500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-TAD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.57 | 6.3 dB  |
| Peaking | 386 Hz  | 0.65 | 1.7 dB  |
| Peaking | 2105 Hz | 1.22 | -3.8 dB |
| Peaking | 3324 Hz | 2.89 | 4.8 dB  |
| Peaking | 4784 Hz | 1.65 | -4.2 dB |
| Peaking | 6639 Hz | 4.34 | -2.5 dB |
| Peaking | 7405 Hz | 2.36 | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.5 dB  |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -2.7 dB |
| Peaking | 4000 Hz  | 1.41 | -1.2 dB |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-TAD500/Audio-Technica%20ATH-TAD500.png)