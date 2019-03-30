# Audio-Technica ATH-MSR7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.3; 23 -1.8; 25 -2.3; 28 -3.0; 31 -3.5; 34 -4.0; 37 -4.3; 41 -4.7; 45 -5.0; 49 -5.2; 54 -5.3; 60 -5.3; 66 -5.3; 72 -5.5; 79 -5.6; 87 -5.4; 96 -5.3; 106 -5.5; 116 -5.8; 128 -6.2; 141 -6.5; 155 -6.7; 170 -6.9; 187 -6.7; 206 -6.5; 227 -5.9; 249 -5.4; 274 -4.8; 302 -4.2; 332 -3.3; 365 -2.2; 402 -1.2; 442 -0.7; 486 -0.5; 535 -0.8; 588 -1.1; 647 -1.5; 712 -1.9; 783 -2.4; 861 -2.9; 947 -3.2; 1042 -3.5; 1146 -3.8; 1261 -4.0; 1387 -3.9; 1526 -3.7; 1678 -3.5; 1846 -3.1; 2031 -3.2; 2234 -3.8; 2457 -4.5; 2703 -5.0; 2973 -4.7; 3270 -3.7; 3597 -2.4; 3957 -2.6; 4353 -4.4; 4788 -6.3; 5267 -7.5; 5793 -8.5; 6373 -8.7; 7010 -7.2; 7711 -6.8; 8482 -7.5; 9330 -6.9; 10263 -5.5; 11289 -6.1; 12418 -7.4; 13660 -6.0; 15026 -4.4; 16529 -4.4; 18182 -4.4; 20000 -4.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-MSR7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-MSR7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 2.1  | 3.2 dB  |
| Peaking | 250 Hz   | 0.56 | -4.8 dB |
| Peaking | 437 Hz   | 0.78 | 6.9 dB  |
| Peaking | 6085 Hz  | 3.37 | -4.1 dB |
| Peaking | 10569 Hz | 1.02 | -2.1 dB |
| Peaking | 1957 Hz  | 4.67 | 1.3 dB  |
| Peaking | 2803 Hz  | 3.13 | -1.1 dB |
| Peaking | 3752 Hz  | 3.56 | 3.1 dB  |
| Peaking | 4965 Hz  | 4.75 | -1.4 dB |
| Peaking | 12734 Hz | 8.65 | -1.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.8 dB |
| Peaking | 500 Hz   | 1.41 | 4.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-MSR7/Audio-Technica%20ATH-MSR7.png)