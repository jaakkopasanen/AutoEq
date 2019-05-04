# Audio-Technica ATH-ANC9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -9.1; 23 -9.5; 25 -9.8; 28 -10.1; 31 -10.2; 34 -10.1; 37 -9.9; 41 -9.6; 45 -9.2; 49 -8.8; 54 -8.4; 60 -8.0; 66 -7.9; 72 -7.8; 79 -8.0; 87 -8.4; 96 -8.9; 106 -9.5; 116 -10.0; 128 -10.3; 141 -10.3; 155 -10.0; 170 -9.5; 187 -8.7; 206 -7.9; 227 -7.1; 249 -6.5; 274 -5.9; 302 -5.5; 332 -5.2; 365 -4.7; 402 -4.5; 442 -4.4; 486 -4.5; 535 -4.5; 588 -4.2; 647 -3.0; 712 -1.4; 783 -0.5; 861 -0.5; 947 -0.7; 1042 -3.0; 1146 -5.4; 1261 -7.0; 1387 -7.6; 1526 -7.7; 1678 -7.3; 1846 -7.4; 2031 -7.2; 2234 -7.4; 2457 -7.2; 2703 -7.3; 2973 -7.1; 3270 -7.0; 3597 -7.5; 3957 -9.1; 4353 -8.7; 4788 -10.9; 5267 -12.1; 5793 -10.8; 6373 -7.3; 7010 -7.7; 7711 -8.6; 8482 -6.6; 9330 -6.5; 10263 -6.5; 11289 -7.1; 12418 -12.2; 13660 -13.3; 15026 -10.9; 16529 -8.2; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 0.92 | -3.7 dB |
| Peaking | 134 Hz   | 1.82 | -4.0 dB |
| Peaking | 793 Hz   | 2.08 | 6.6 dB  |
| Peaking | 5143 Hz  | 2.78 | -5.5 dB |
| Peaking | 13703 Hz | 2.4  | -7.5 dB |
| Peaking | 184 Hz   | 4.05 | -1.0 dB |
| Peaking | 387 Hz   | 1.43 | 1.9 dB  |
| Peaking | 979 Hz   | 3.26 | 4.6 dB  |
| Peaking | 1117 Hz  | 1.09 | -3.4 dB |
| Peaking | 10331 Hz | 4.1  | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.2 dB |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 4.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -2.5 dB |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC9/Audio-Technica%20ATH-ANC9.png)