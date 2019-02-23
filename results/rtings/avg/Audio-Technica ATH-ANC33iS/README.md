# Audio-Technica ATH-ANC33iS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.7; 66 -1.4; 72 -2.1; 79 -2.9; 87 -3.8; 96 -4.7; 106 -5.7; 116 -6.7; 128 -7.6; 141 -8.5; 155 -9.2; 170 -9.8; 187 -10.3; 206 -10.7; 227 -10.9; 249 -10.9; 274 -11.1; 302 -11.2; 332 -11.2; 365 -11.1; 402 -10.9; 442 -10.5; 486 -9.9; 535 -9.0; 588 -8.1; 647 -6.4; 712 -5.1; 783 -3.4; 861 -2.8; 947 -2.5; 1042 -1.6; 1146 -1.0; 1261 -2.1; 1387 -5.0; 1526 -7.5; 1678 -7.7; 1846 -6.5; 2031 -4.7; 2234 -2.3; 2457 -0.6; 2703 -0.5; 2973 -1.0; 3270 -2.9; 3597 -4.6; 3957 -5.6; 4353 -6.8; 4788 -7.7; 5267 -9.1; 5793 -8.3; 6373 -7.3; 7010 -4.9; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC33iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC33iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 0.41 | 9.0 dB  |
| Peaking | 428 Hz  | 0.17 | -7.8 dB |
| Peaking | 952 Hz  | 1.08 | 11.8 dB |
| Peaking | 2710 Hz | 2.08 | 8.8 dB  |
| Peaking | 5353 Hz | 6.1  | -2.7 dB |
| Peaking | 971 Hz  | 3.99 | -3.2 dB |
| Peaking | 1218 Hz | 1.8  | 4.4 dB  |
| Peaking | 1542 Hz | 2.61 | -4.5 dB |
| Peaking | 2246 Hz | 7.26 | 1.5 dB  |
| Peaking | 7095 Hz | 8.92 | 2.2 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | -1.3 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | -3.4 dB |
| Peaking | 1000 Hz  | 1.41 | 5.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.6 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC33iS/Audio-Technica%20ATH-ANC33iS.png)