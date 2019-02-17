# Audio-Technica ATH-M30x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.9; 23 -5.5; 25 -6.0; 28 -6.8; 31 -7.4; 34 -7.9; 37 -8.3; 41 -8.6; 45 -8.8; 49 -8.9; 54 -8.9; 60 -8.8; 66 -8.7; 72 -8.5; 79 -8.3; 87 -8.4; 96 -8.7; 106 -9.0; 116 -9.2; 128 -9.2; 141 -8.8; 155 -8.2; 170 -7.4; 187 -6.3; 206 -4.8; 227 -3.4; 249 -2.5; 274 -2.4; 302 -3.9; 332 -5.0; 365 -5.9; 402 -6.6; 442 -7.0; 486 -7.2; 535 -7.3; 588 -7.3; 647 -7.3; 712 -7.1; 783 -6.9; 861 -6.8; 947 -6.6; 1042 -6.4; 1146 -6.8; 1261 -7.3; 1387 -8.0; 1526 -8.9; 1678 -9.9; 1846 -10.8; 2031 -11.3; 2234 -10.2; 2457 -8.8; 2703 -7.6; 2973 -7.2; 3270 -5.7; 3597 -4.7; 3957 -5.8; 4353 -3.2; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.7; 7010 -6.5; 7711 -8.7; 8482 -9.2; 9330 -9.1; 10263 -10.5; 11289 -13.1; 12418 -13.6; 13660 -10.9; 15026 -9.1; 16529 -8.3; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M30x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M30x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 139 Hz   | 0.35 | -3.2 dB |
| Peaking | 253 Hz   | 1.83 | 7.0 dB  |
| Peaking | 1981 Hz  | 2.33 | -5.1 dB |
| Peaking | 5352 Hz  | 2.15 | 8.0 dB  |
| Peaking | 11800 Hz | 1.13 | -7.0 dB |
| Peaking | 14 Hz    | 0.36 | 2.8 dB  |
| Peaking | 39 Hz    | 1.28 | -2.4 dB |
| Peaking | 1048 Hz  | 5.2  | 0.8 dB  |
| Peaking | 7727 Hz  | 3.72 | -4.2 dB |
| Peaking | 7987 Hz  | 1.72 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.6 dB |
| Peaking | 62 Hz    | 1.41 | -1.8 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 4.5 dB  |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.1 dB |
| Peaking | 16000 Hz | 1.41 | -4.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M30x/Audio-Technica%20ATH-M30x.png)