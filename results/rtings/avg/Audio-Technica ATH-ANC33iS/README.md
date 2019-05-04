# Audio-Technica ATH-ANC33iS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.8; 31 -1.3; 34 -1.9; 37 -2.3; 41 -2.9; 45 -3.4; 49 -3.8; 54 -4.3; 60 -4.9; 66 -5.5; 72 -6.0; 79 -6.5; 87 -7.1; 96 -7.7; 106 -8.2; 116 -8.7; 128 -9.2; 141 -9.6; 155 -9.9; 170 -10.2; 187 -10.4; 206 -10.6; 227 -10.6; 249 -10.7; 274 -10.8; 302 -10.9; 332 -10.9; 365 -10.8; 402 -10.6; 442 -10.2; 486 -9.7; 535 -8.8; 588 -8.0; 647 -6.2; 712 -4.9; 783 -3.3; 861 -2.6; 947 -2.3; 1042 -1.5; 1146 -0.9; 1261 -2.0; 1387 -5.0; 1526 -7.4; 1678 -7.7; 1846 -6.5; 2031 -4.8; 2234 -3.0; 2457 -1.2; 2703 -0.5; 2973 -0.8; 3270 -2.4; 3597 -4.0; 3957 -5.1; 4353 -6.1; 4788 -7.8; 5267 -9.2; 5793 -8.0; 6373 -6.0; 7010 -4.6; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC33iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC33iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.39 | 6.4 dB  |
| Peaking | 514 Hz  | 0.19 | -5.8 dB |
| Peaking | 960 Hz  | 1.23 | 10.5 dB |
| Peaking | 2789 Hz | 2.02 | 8.2 dB  |
| Peaking | 5231 Hz | 6.22 | -3.0 dB |
| Peaking | 976 Hz  | 4.37 | -3.2 dB |
| Peaking | 1235 Hz | 1.79 | 4.3 dB  |
| Peaking | 1536 Hz | 2.64 | -4.5 dB |
| Peaking | 2235 Hz | 5.61 | 1.2 dB  |
| Peaking | 6917 Hz | 7.64 | 2.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 0.8 dB  |
| Peaking | 125 Hz   | 1.41 | -2.4 dB |
| Peaking | 250 Hz   | 1.41 | -4.2 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | 5.3 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC33iS/Audio-Technica%20ATH-ANC33iS.png)