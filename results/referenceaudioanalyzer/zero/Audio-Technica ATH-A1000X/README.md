# Audio-Technica ATH-A1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.3; 28 -2.5; 31 -3.7; 34 -4.7; 37 -5.4; 41 -6.2; 45 -7.0; 49 -7.6; 54 -8.3; 60 -8.8; 66 -9.1; 72 -9.4; 79 -9.9; 87 -10.3; 96 -10.6; 106 -10.4; 116 -10.1; 128 -9.8; 141 -9.1; 155 -8.5; 170 -7.6; 187 -6.5; 206 -5.1; 227 -3.4; 249 -1.9; 274 -0.8; 302 -0.6; 332 -1.3; 365 -2.3; 402 -3.0; 442 -3.5; 486 -3.9; 535 -4.3; 588 -4.4; 647 -4.6; 712 -4.8; 783 -5.0; 861 -5.1; 947 -5.1; 1042 -5.5; 1146 -6.1; 1261 -6.7; 1387 -7.3; 1526 -7.7; 1678 -7.7; 1846 -7.1; 2031 -6.2; 2234 -5.6; 2457 -5.4; 2703 -5.4; 2973 -6.1; 3270 -6.7; 3597 -6.8; 3957 -9.6; 4353 -13.4; 4788 -14.9; 5267 -14.6; 5793 -12.3; 6373 -7.7; 7010 -6.2; 7711 -8.3; 8482 -8.3; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -8.1; 13660 -8.1; 15026 -6.6; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-A1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-A1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.12 | 6.7 dB  |
| Peaking | 117 Hz   | 0.53 | -5.9 dB |
| Peaking | 260 Hz   | 0.85 | -5.3 dB |
| Peaking | 277 Hz   | 0.94 | 13.8 dB |
| Peaking | 4954 Hz  | 3.2  | -9.6 dB |
| Peaking | 1645 Hz  | 1.74 | -4.3 dB |
| Peaking | 2003 Hz  | 0.87 | 3.1 dB  |
| Peaking | 4292 Hz  | 8.62 | -2.6 dB |
| Peaking | 10944 Hz | 5.4  | 0.7 dB  |
| Peaking | 12910 Hz | 2.96 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.5 dB  |
| Peaking | 62 Hz    | 1.41 | -3.2 dB |
| Peaking | 125 Hz   | 1.41 | -4.9 dB |
| Peaking | 250 Hz   | 1.41 | 5.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -4.8 dB |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-A1000X/Audio-Technica%20ATH-A1000X.png)