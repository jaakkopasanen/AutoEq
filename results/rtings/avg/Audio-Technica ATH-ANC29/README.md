# Audio-Technica ATH-ANC29
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.5; 23 -5.0; 25 -4.7; 28 -4.5; 31 -4.4; 34 -4.3; 37 -4.3; 41 -4.3; 45 -4.4; 49 -4.5; 54 -4.7; 60 -4.9; 66 -5.1; 72 -5.4; 79 -5.6; 87 -6.0; 96 -6.3; 106 -6.7; 116 -7.0; 128 -7.3; 141 -7.6; 155 -7.9; 170 -8.0; 187 -8.1; 206 -8.1; 227 -8.1; 249 -8.0; 274 -8.1; 302 -8.2; 332 -8.4; 365 -8.4; 402 -8.7; 442 -9.1; 486 -9.4; 535 -9.7; 588 -9.9; 647 -9.9; 712 -10.0; 783 -9.9; 861 -8.2; 947 -7.6; 1042 -10.7; 1146 -13.8; 1261 -13.1; 1387 -10.6; 1526 -7.5; 1678 -5.3; 1846 -4.2; 2031 -3.7; 2234 -2.8; 2457 -2.7; 2703 -3.9; 2973 -4.0; 3270 -1.7; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -3.3; 5793 -4.2; 6373 -11.0; 7010 -11.4; 7711 -8.8; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC29 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 527 Hz  | 0.62 | -3.0 dB |
| Peaking | 1220 Hz | 4    | -7.4 dB |
| Peaking | 2044 Hz | 2.09 | 3.1 dB  |
| Peaking | 4302 Hz | 1.33 | 6.8 dB  |
| Peaking | 6764 Hz | 4.16 | -8.6 dB |
| Peaking | 39 Hz   | 0.66 | 2.3 dB  |
| Peaking | 153 Hz  | 1.79 | -1.2 dB |
| Peaking | 787 Hz  | 3.42 | -2.0 dB |
| Peaking | 914 Hz  | 3.83 | 3.2 dB  |
| Peaking | 1078 Hz | 7.25 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -1.0 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.5 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC29/Audio-Technica%20ATH-ANC29.png)