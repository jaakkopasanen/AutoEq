# Audio-Technica ATH-M30x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.0; 23 -5.6; 25 -6.1; 28 -6.9; 31 -7.5; 34 -8.0; 37 -8.4; 41 -8.7; 45 -9.0; 49 -9.1; 54 -9.1; 60 -9.1; 66 -8.9; 72 -8.7; 79 -8.4; 87 -8.5; 96 -8.8; 106 -9.1; 116 -9.3; 128 -9.2; 141 -8.8; 155 -8.3; 170 -7.5; 187 -6.4; 206 -5.0; 227 -3.6; 249 -2.7; 274 -2.7; 302 -4.1; 332 -5.2; 365 -6.1; 402 -6.9; 442 -7.3; 486 -7.6; 535 -7.7; 588 -7.7; 647 -7.6; 712 -7.5; 783 -7.3; 861 -7.1; 947 -6.9; 1042 -6.8; 1146 -7.1; 1261 -7.8; 1387 -8.5; 1526 -9.4; 1678 -10.4; 1846 -11.4; 2031 -12.0; 2234 -11.6; 2457 -10.0; 2703 -8.5; 2973 -7.7; 3270 -5.7; 3597 -4.9; 3957 -5.8; 4353 -2.9; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.5; 7010 -6.7; 7711 -9.7; 8482 -9.1; 9330 -7.7; 10263 -10.4; 11289 -14.3; 12418 -13.9; 13660 -10.2; 15026 -8.9; 16529 -8.4; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M30x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M30x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 148 Hz   | 0.31 | -3.3 dB |
| Peaking | 254 Hz   | 1.79 | 7.1 dB  |
| Peaking | 2041 Hz  | 2.07 | -5.9 dB |
| Peaking | 5272 Hz  | 2.24 | 7.8 dB  |
| Peaking | 11825 Hz | 1.54 | -8.0 dB |
| Peaking | 13 Hz    | 0.34 | 2.9 dB  |
| Peaking | 39 Hz    | 1.19 | -2.5 dB |
| Peaking | 6306 Hz  | 7.5  | 3.4 dB  |
| Peaking | 7719 Hz  | 3.04 | -3.6 dB |
| Peaking | 9387 Hz  | 4.86 | 3.1 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.7 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 4.4 dB  |
| Peaking | 500 Hz   | 1.41 | -2.1 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.9 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.2 dB |
| Peaking | 16000 Hz | 1.41 | -4.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M30x/Audio-Technica%20ATH-M30x.png)