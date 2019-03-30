# Audio-Technica ATH-ADX5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.8; 23 -1.4; 25 -1.9; 28 -2.6; 31 -3.2; 34 -3.7; 37 -4.2; 41 -4.7; 45 -5.2; 49 -5.5; 54 -5.8; 60 -6.1; 66 -6.4; 72 -6.6; 79 -6.8; 87 -7.0; 96 -7.1; 106 -7.3; 116 -7.1; 128 -7.0; 141 -6.7; 155 -6.5; 170 -6.2; 187 -5.8; 206 -5.4; 227 -4.9; 249 -4.3; 274 -3.7; 302 -2.9; 332 -2.1; 365 -1.4; 402 -0.8; 442 -0.5; 486 -0.8; 535 -1.4; 588 -2.1; 647 -2.7; 712 -3.3; 783 -3.7; 861 -4.0; 947 -4.3; 1042 -4.4; 1146 -4.4; 1261 -4.4; 1387 -4.6; 1526 -4.1; 1678 -3.4; 1846 -2.8; 2031 -2.6; 2234 -2.9; 2457 -3.6; 2703 -3.7; 2973 -3.6; 3270 -6.4; 3597 -9.4; 3957 -11.4; 4353 -12.6; 4788 -12.0; 5267 -11.3; 5793 -13.5; 6373 -14.7; 7010 -12.4; 7711 -8.3; 8482 -5.4; 9330 -5.3; 10263 -5.3; 11289 -7.3; 12418 -11.2; 13660 -11.1; 15026 -7.4; 16529 -5.3; 18182 -5.3; 20000 -5.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ADX5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ADX5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 2.5  | 4.7 dB   |
| Peaking | 2886 Hz  | 0.1  | 2.8 dB   |
| Peaking | 4274 Hz  | 2.4  | -8.7 dB  |
| Peaking | 6345 Hz  | 2.83 | -10.8 dB |
| Peaking | 13186 Hz | 2.26 | -8.6 dB  |
| Peaking | 30 Hz    | 1.16 | 1.6 dB   |
| Peaking | 114 Hz   | 0.62 | -2.4 dB  |
| Peaking | 418 Hz   | 1.52 | 3.5 dB   |
| Peaking | 1043 Hz  | 1.63 | -2.1 dB  |
| Peaking | 8567 Hz  | 6.66 | 1.1 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 3.1 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 4.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 4.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -6.7 dB |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | -2.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-ADX5000/Audio-Technica%20ATH-ADX5000.png)