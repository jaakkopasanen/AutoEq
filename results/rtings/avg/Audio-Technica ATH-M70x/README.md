# Audio-Technica ATH-M70x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.0; 28 -1.2; 31 -1.4; 34 -1.3; 37 -1.3; 41 -1.1; 45 -1.1; 49 -1.1; 54 -1.2; 60 -1.5; 66 -2.0; 72 -2.4; 79 -2.8; 87 -3.3; 96 -3.6; 106 -3.8; 116 -4.0; 128 -4.1; 141 -4.0; 155 -3.8; 170 -3.7; 187 -3.7; 206 -3.6; 227 -3.9; 249 -4.3; 274 -4.4; 302 -4.2; 332 -4.6; 365 -4.5; 402 -3.9; 442 -3.3; 486 -3.1; 535 -2.8; 588 -1.4; 647 -0.6; 712 -0.8; 783 -1.3; 861 -1.7; 947 -2.1; 1042 -2.5; 1146 -2.7; 1261 -3.0; 1387 -3.4; 1526 -4.1; 1678 -4.9; 1846 -6.1; 2031 -7.3; 2234 -7.8; 2457 -7.4; 2703 -6.6; 2973 -6.5; 3270 -7.9; 3597 -8.3; 3957 -8.0; 4353 -10.6; 4788 -11.3; 5267 -9.0; 5793 -5.7; 6373 -3.7; 7010 -5.5; 7711 -8.7; 8482 -9.7; 9330 -8.1; 10263 -8.0; 11289 -8.0; 12418 -5.2; 13660 -4.9; 15026 -4.9; 16529 -5.1; 18182 -6.5; 20000 -5.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-4.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1.31 | 3.9 dB  |
| Peaking | 46 Hz    | 0.71 | 3.4 dB  |
| Peaking | 733 Hz   | 1.33 | 4.3 dB  |
| Peaking | 4215 Hz  | 1.61 | -5.0 dB |
| Peaking | 9185 Hz  | 2.37 | -3.9 dB |
| Peaking | 2231 Hz  | 2.21 | -4.4 dB |
| Peaking | 3498 Hz  | 0.59 | 3.5 dB  |
| Peaking | 5610 Hz  | 1.2  | -6.3 dB |
| Peaking | 6265 Hz  | 3.6  | 7.6 dB  |
| Peaking | 18837 Hz | 1.79 | -1.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.2 dB  |
| Peaking | 62 Hz    | 1.41 | 2.4 dB  |
| Peaking | 125 Hz   | 1.41 | 0.4 dB  |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 1.8 dB  |
| Peaking | 1000 Hz  | 1.41 | 3.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -3.7 dB |
| Peaking | 8000 Hz  | 1.41 | -2.6 dB |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M70x/Audio-Technica%20ATH-M70x.png)