# Audio-Technica ATH-ANC23
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.6; 45 -0.9; 49 -1.3; 54 -1.8; 60 -2.6; 66 -3.4; 72 -4.0; 79 -4.7; 87 -5.6; 96 -6.5; 106 -7.4; 116 -8.4; 128 -9.3; 141 -10.1; 155 -10.8; 170 -11.4; 187 -11.8; 206 -12.2; 227 -12.5; 249 -12.6; 274 -12.7; 302 -12.8; 332 -12.8; 365 -12.8; 402 -12.6; 442 -12.3; 486 -11.8; 535 -11.0; 588 -9.9; 647 -8.6; 712 -8.3; 783 -7.6; 861 -7.1; 947 -6.7; 1042 -6.4; 1146 -6.4; 1261 -6.8; 1387 -7.8; 1526 -9.0; 1678 -9.5; 1846 -9.3; 2031 -8.5; 2234 -7.0; 2457 -5.7; 2703 -5.7; 2973 -6.7; 3270 -8.2; 3597 -9.3; 3957 -10.0; 4353 -10.9; 4788 -11.9; 5267 -13.7; 5793 -14.4; 6373 -12.5; 7010 -9.9; 7711 -9.6; 8482 -11.5; 9330 -10.5; 10263 -6.6; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -7.0; 20000 -12.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC23 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC23 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.41 | 6.7 dB  |
| Peaking | 195 Hz   | 0.66 | -6.2 dB |
| Peaking | 411 Hz   | 1.51 | -3.7 dB |
| Peaking | 5664 Hz  | 1.47 | -7.4 dB |
| Peaking | 19756 Hz | 2.08 | -6.1 dB |
| Peaking | 1176 Hz  | 1.19 | 4.9 dB  |
| Peaking | 1799 Hz  | 0.75 | -6.9 dB |
| Peaking | 2538 Hz  | 1.9  | 6.3 dB  |
| Peaking | 8745 Hz  | 1.3  | 3.7 dB  |
| Peaking | 8896 Hz  | 3.83 | -6.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.0dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 3.5 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -6.1 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -0.5 dB |
| Peaking | 4000 Hz  | 1.41 | -3.5 dB |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.6 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC23/Audio-Technica%20ATH-ANC23.png)