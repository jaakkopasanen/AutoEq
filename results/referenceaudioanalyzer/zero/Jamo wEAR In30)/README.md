# Jamo wEAR In30)
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -14.6; 23 -14.7; 25 -14.7; 28 -14.8; 31 -14.8; 34 -14.8; 37 -14.8; 41 -14.8; 45 -14.8; 49 -14.8; 54 -14.8; 60 -14.8; 66 -14.8; 72 -14.6; 79 -14.4; 87 -14.5; 96 -14.3; 106 -14.1; 116 -13.9; 128 -13.7; 141 -13.5; 155 -13.2; 170 -12.8; 187 -12.5; 206 -12.1; 227 -11.6; 249 -11.1; 274 -10.7; 302 -10.2; 332 -9.7; 365 -9.1; 402 -8.5; 442 -7.8; 486 -7.2; 535 -6.5; 588 -5.7; 647 -4.9; 712 -4.1; 783 -3.3; 861 -2.6; 947 -1.9; 1042 -1.2; 1146 -0.7; 1261 -0.5; 1387 -0.5; 1526 -0.8; 1678 -1.1; 1846 -1.4; 2031 -1.6; 2234 -1.9; 2457 -2.4; 2703 -3.0; 2973 -3.4; 3270 -3.8; 3597 -3.4; 3957 -3.1; 4353 -3.5; 4788 -3.8; 5267 -3.8; 5793 -4.9; 6373 -7.4; 7010 -8.4; 7711 -6.6; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -7.9; 13660 -6.5; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jamo wEAR In30) GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jamo wEAR In30) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 51 Hz    | 0.1  | -9.0 dB |
| Peaking | 1184 Hz  | 0.94 | 3.8 dB  |
| Peaking | 1244 Hz  | 0.18 | 3.1 dB  |
| Peaking | 6908 Hz  | 4.29 | -4.2 dB |
| Peaking | 12659 Hz | 4.53 | -2.6 dB |
| Peaking | 2120 Hz  | 4.29 | 0.3 dB  |
| Peaking | 3186 Hz  | 2.73 | -1.3 dB |
| Peaking | 3969 Hz  | 1.52 | 0.8 dB  |
| Peaking | 9353 Hz  | 4.08 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -8.9 dB |
| Peaking | 62 Hz    | 1.41 | -6.4 dB |
| Peaking | 125 Hz   | 1.41 | -6.3 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.1 dB |
| Peaking | 1000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 2.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.4 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Jamo%20wEAR%20In30)/Jamo%20wEAR%20In30).png)