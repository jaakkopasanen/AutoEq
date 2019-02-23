# Audio-Technica ATH-ANC70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.2; 23 -2.0; 25 -1.8; 28 -1.6; 31 -1.5; 34 -1.4; 37 -1.4; 41 -1.4; 45 -1.4; 49 -1.6; 54 -1.8; 60 -2.1; 66 -2.5; 72 -2.9; 79 -3.3; 87 -3.9; 96 -4.4; 106 -5.0; 116 -5.5; 128 -6.0; 141 -6.3; 155 -6.5; 170 -6.7; 187 -6.8; 206 -6.7; 227 -6.7; 249 -6.6; 274 -6.4; 302 -6.3; 332 -6.2; 365 -5.9; 402 -5.6; 442 -5.2; 486 -4.8; 535 -4.4; 588 -3.9; 647 -3.8; 712 -4.2; 783 -5.3; 861 -6.8; 947 -8.3; 1042 -10.2; 1146 -11.9; 1261 -12.8; 1387 -12.4; 1526 -11.4; 1678 -10.2; 1846 -10.2; 2031 -10.3; 2234 -9.1; 2457 -9.2; 2703 -9.6; 2973 -10.6; 3270 -11.2; 3597 -9.1; 3957 -6.7; 4353 -4.7; 4788 -1.6; 5267 -0.5; 5793 -1.6; 6373 -5.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -8.7; 12418 -11.8; 13660 -12.9; 15026 -12.0; 16529 -8.4; 18182 -9.4; 20000 -21.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.63 | 5.6 dB  |
| Peaking | 1321 Hz  | 2.74 | -6.5 dB |
| Peaking | 3331 Hz  | 1.33 | -6.2 dB |
| Peaking | 5093 Hz  | 1.62 | 8.8 dB  |
| Peaking | 20887 Hz | 0.09 | -6.3 dB |
| Peaking | 637 Hz   | 2.04 | 3.4 dB  |
| Peaking | 1067 Hz  | 4.54 | -1.9 dB |
| Peaking | 9580 Hz  | 3.57 | 1.2 dB  |
| Peaking | 10568 Hz | 5.93 | 2.0 dB  |
| Peaking | 13144 Hz | 3.16 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.7 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | 3.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | -5.1 dB |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -6.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC70/Audio-Technica%20ATH-ANC70.png)