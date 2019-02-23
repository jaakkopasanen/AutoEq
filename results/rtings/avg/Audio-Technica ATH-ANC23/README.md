# Audio-Technica ATH-ANC23
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.7; 79 -1.4; 87 -2.2; 96 -3.1; 106 -4.0; 116 -5.0; 128 -5.9; 141 -6.8; 155 -7.5; 170 -8.0; 187 -8.4; 206 -8.8; 227 -9.1; 249 -9.2; 274 -9.4; 302 -9.4; 332 -9.5; 365 -9.4; 402 -9.2; 442 -8.9; 486 -8.4; 535 -7.6; 588 -6.5; 647 -5.2; 712 -4.9; 783 -4.2; 861 -3.7; 947 -3.3; 1042 -3.0; 1146 -3.0; 1261 -3.4; 1387 -4.4; 1526 -5.6; 1678 -6.1; 1846 -5.9; 2031 -5.1; 2234 -3.7; 2457 -2.4; 2703 -2.3; 2973 -3.4; 3270 -4.8; 3597 -5.9; 3957 -6.6; 4353 -7.6; 4788 -8.5; 5267 -10.3; 5793 -11.0; 6373 -9.1; 7010 -6.5; 7711 -6.3; 8482 -8.1; 9330 -7.2; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.3
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC23 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC23 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 57 Hz    | 0.31 | 8.1 dB  |
| Peaking | 214 Hz   | 0.44 | -6.5 dB |
| Peaking | 933 Hz   | 1.25 | 4.7 dB  |
| Peaking | 2650 Hz  | 3.18 | 4.5 dB  |
| Peaking | 5563 Hz  | 3.44 | -5.0 dB |
| Peaking | 19 Hz    | 0.4  | 1.3 dB  |
| Peaking | 37 Hz    | 1.47 | -1.7 dB |
| Peaking | 1237 Hz  | 5.64 | 1.0 dB  |
| Peaking | 1668 Hz  | 4.86 | -1.2 dB |
| Peaking | 17718 Hz | 2.28 | -0.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.9 dB  |
| Peaking | 62 Hz    | 1.41 | 5.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | -3.6 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.2 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC23/Audio-Technica%20ATH-ANC23.png)