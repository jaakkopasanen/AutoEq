# Audio-Technica ATH-M40x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.7; 23 -5.5; 25 -6.2; 28 -7.3; 31 -8.1; 34 -8.9; 37 -9.5; 41 -10.1; 45 -10.4; 49 -10.4; 54 -10.3; 60 -10.2; 66 -9.9; 72 -9.4; 79 -8.7; 87 -8.6; 96 -9.7; 106 -11.0; 116 -12.0; 128 -12.5; 141 -12.2; 155 -11.6; 170 -10.6; 187 -9.5; 206 -8.1; 227 -6.8; 249 -5.7; 274 -4.9; 302 -4.1; 332 -3.3; 365 -2.7; 402 -2.4; 442 -2.4; 486 -2.2; 535 -2.1; 588 -2.1; 647 -2.3; 712 -2.4; 783 -2.6; 861 -3.1; 947 -3.6; 1042 -4.2; 1146 -4.8; 1261 -4.9; 1387 -4.5; 1526 -3.9; 1678 -3.2; 1846 -2.3; 2031 -1.2; 2234 -0.5; 2457 -0.9; 2703 -2.2; 2973 -3.5; 3270 -4.5; 3597 -5.2; 3957 -6.5; 4353 -7.6; 4788 -7.1; 5267 -6.3; 5793 -6.9; 6373 -7.6; 7010 -7.0; 7711 -4.9; 8482 -5.0; 9330 -5.0; 10263 -5.0; 11289 -5.0; 12418 -5.2; 13660 -5.2; 15026 -5.0; 16529 -5.0; 18182 -5.0; 20000 -5.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 47 Hz   | 1.24 | -5.1 dB |
| Peaking | 139 Hz  | 1.25 | -7.6 dB |
| Peaking | 463 Hz  | 0.86 | 3.6 dB  |
| Peaking | 2317 Hz | 2.28 | 5.0 dB  |
| Peaking | 4899 Hz | 1.27 | -2.6 dB |
| Peaking | 777 Hz  | 3.83 | 0.7 dB  |
| Peaking | 1205 Hz | 4.13 | -1.2 dB |
| Peaking | 6750 Hz | 4.46 | -3.2 dB |
| Peaking | 6956 Hz | 1.9  | 1.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -2.9 dB |
| Peaking | 125 Hz   | 1.41 | -7.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.3 dB |
| Peaking | 500 Hz   | 1.41 | 4.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.2 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.1 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-M40x/Audio-Technica%20ATH-M40x.png)