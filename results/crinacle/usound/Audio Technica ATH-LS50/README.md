# Audio Technica ATH-LS50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.5; 23 -9.7; 25 -9.9; 28 -10.1; 31 -10.2; 34 -10.3; 37 -10.4; 41 -10.5; 45 -10.6; 49 -10.7; 54 -10.8; 60 -11.0; 66 -11.1; 72 -11.2; 79 -11.4; 87 -11.5; 96 -11.7; 106 -11.8; 116 -11.8; 128 -11.8; 141 -11.7; 155 -11.6; 170 -11.4; 187 -11.1; 206 -10.7; 227 -10.2; 249 -9.8; 274 -9.3; 302 -8.7; 332 -8.2; 365 -7.6; 402 -7.0; 442 -6.4; 486 -5.9; 535 -5.3; 588 -4.7; 647 -4.1; 712 -3.5; 783 -2.9; 861 -2.6; 947 -2.7; 1042 -3.4; 1146 -4.8; 1261 -7.4; 1387 -9.7; 1526 -10.4; 1678 -9.7; 1846 -8.6; 2031 -7.7; 2234 -6.4; 2457 -4.6; 2703 -2.9; 2973 -1.6; 3270 -0.8; 3597 -0.6; 3957 -0.9; 4353 -2.1; 4788 -3.7; 5267 -3.6; 5793 -1.1; 6373 -0.5; 7010 -3.4; 7711 -5.7; 8482 -5.9; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-LS50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-LS50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.41 | -4.7 dB |
| Peaking | 160 Hz  | 1.04 | -4.0 dB |
| Peaking | 1627 Hz | 3.65 | -5.5 dB |
| Peaking | 3489 Hz | 1.81 | 5.8 dB  |
| Peaking | 6205 Hz | 5.32 | 5.4 dB  |
| Peaking | 18 Hz   | 1.82 | -0.7 dB |
| Peaking | 305 Hz  | 1.73 | -1.2 dB |
| Peaking | 919 Hz  | 1.1  | 4.1 dB  |
| Peaking | 1349 Hz | 4.35 | -4.0 dB |
| Peaking | 2075 Hz | 4.8  | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -3.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.1 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | 2.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -4.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Technica%20ATH-LS50/Audio%20Technica%20ATH-LS50.png)