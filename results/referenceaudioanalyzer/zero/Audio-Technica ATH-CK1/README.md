# Audio-Technica ATH-CK1
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.6; 25 -0.9; 28 -1.6; 31 -2.4; 34 -2.9; 37 -3.4; 41 -3.8; 45 -4.2; 49 -4.6; 54 -5.0; 60 -5.4; 66 -5.7; 72 -5.8; 79 -5.8; 87 -5.7; 96 -5.9; 106 -6.1; 116 -6.0; 128 -5.7; 141 -5.8; 155 -5.6; 170 -5.2; 187 -4.7; 206 -4.3; 227 -4.4; 249 -4.8; 274 -5.3; 302 -5.5; 332 -5.4; 365 -5.1; 402 -4.9; 442 -4.6; 486 -4.3; 535 -4.0; 588 -3.8; 647 -3.5; 712 -3.5; 783 -3.2; 861 -3.0; 947 -2.6; 1042 -2.5; 1146 -2.5; 1261 -2.6; 1387 -2.9; 1526 -3.3; 1678 -3.7; 1846 -4.4; 2031 -5.7; 2234 -8.0; 2457 -10.3; 2703 -12.7; 2973 -14.6; 3270 -14.8; 3597 -13.4; 3957 -11.2; 4353 -9.6; 4788 -8.7; 5267 -9.0; 5793 -10.4; 6373 -11.5; 7010 -11.1; 7711 -9.9; 8482 -9.2; 9330 -9.0; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-CK1 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-CK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.01 | 6.0 dB   |
| Peaking | 448 Hz   | 0.29 | 1.1 dB   |
| Peaking | 1456 Hz  | 0.61 | 4.3 dB   |
| Peaking | 3047 Hz  | 1.79 | -10.9 dB |
| Peaking | 6892 Hz  | 2.08 | -4.5 dB  |
| Peaking | 211 Hz   | 2.12 | 2.9 dB   |
| Peaking | 213 Hz   | 1.1  | -1.8 dB  |
| Peaking | 4826 Hz  | 8.03 | 0.9 dB   |
| Peaking | 9522 Hz  | 4.75 | -2.0 dB  |
| Peaking | 10445 Hz | 2.28 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.2 dB  |
| Peaking | 62 Hz    | 1.41 | -0.2 dB |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 1.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.0 dB |
| Peaking | 4000 Hz  | 1.41 | -6.5 dB |
| Peaking | 8000 Hz  | 1.41 | -2.3 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-CK1/Audio-Technica%20ATH-CK1.png)