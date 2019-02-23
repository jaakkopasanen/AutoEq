# Audio-Technica ATH-ANC9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.3; 23 -9.7; 25 -10.0; 28 -10.3; 31 -10.4; 34 -10.3; 37 -10.1; 41 -9.7; 45 -9.4; 49 -9.0; 54 -8.5; 60 -8.2; 66 -8.1; 72 -8.1; 79 -8.2; 87 -8.6; 96 -9.1; 106 -9.7; 116 -10.2; 128 -10.5; 141 -10.5; 155 -10.2; 170 -9.7; 187 -8.9; 206 -8.1; 227 -7.2; 249 -6.5; 274 -5.9; 302 -5.5; 332 -5.2; 365 -4.7; 402 -4.5; 442 -4.4; 486 -4.5; 535 -4.5; 588 -4.1; 647 -2.9; 712 -1.3; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -2.9; 1146 -5.2; 1261 -6.8; 1387 -7.4; 1526 -7.4; 1678 -7.1; 1846 -7.0; 2031 -6.8; 2234 -6.6; 2457 -6.3; 2703 -6.7; 2973 -7.0; 3270 -7.2; 3597 -7.7; 3957 -9.5; 4353 -8.9; 4788 -10.7; 5267 -11.5; 5793 -11.0; 6373 -8.2; 7010 -7.6; 7711 -7.8; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -6.6; 12418 -11.8; 13660 -14.1; 15026 -11.5; 16529 -8.4; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.89 | -3.9 dB |
| Peaking | 135 Hz   | 1.73 | -4.2 dB |
| Peaking | 791 Hz   | 1.93 | 6.5 dB  |
| Peaking | 5148 Hz  | 2.43 | -5.1 dB |
| Peaking | 13843 Hz | 2.55 | -8.3 dB |
| Peaking | 185 Hz   | 4.29 | -0.9 dB |
| Peaking | 370 Hz   | 1.61 | 1.7 dB  |
| Peaking | 996 Hz   | 3.42 | 4.5 dB  |
| Peaking | 1099 Hz  | 1.35 | -3.4 dB |
| Peaking | 10308 Hz | 3.29 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.4 dB |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -4.3 dB |
| Peaking | 250 Hz   | 1.41 | -0.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.0 dB |
| Peaking | 4000 Hz  | 1.41 | -2.8 dB |
| Peaking | 8000 Hz  | 1.41 | -0.8 dB |
| Peaking | 16000 Hz | 1.41 | -5.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC9/Audio-Technica%20ATH-ANC9.png)