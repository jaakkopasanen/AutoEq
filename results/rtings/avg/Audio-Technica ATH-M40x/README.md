# Audio-Technica ATH-M40x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.6; 25 -2.2; 28 -3.0; 31 -3.6; 34 -4.2; 37 -4.6; 41 -5.0; 45 -5.3; 49 -5.5; 54 -5.6; 60 -5.7; 66 -5.8; 72 -5.6; 79 -5.4; 87 -5.5; 96 -6.3; 106 -7.2; 116 -7.9; 128 -8.1; 141 -7.7; 155 -7.4; 170 -7.2; 187 -6.5; 206 -5.5; 227 -4.4; 249 -3.3; 274 -2.3; 302 -1.5; 332 -0.6; 365 -0.7; 402 -1.3; 442 -1.3; 486 -1.6; 535 -1.8; 588 -2.0; 647 -2.1; 712 -2.1; 783 -2.0; 861 -2.0; 947 -2.3; 1042 -3.0; 1146 -3.7; 1261 -4.3; 1387 -4.5; 1526 -4.8; 1678 -5.0; 1846 -5.1; 2031 -5.2; 2234 -4.7; 2457 -3.7; 2703 -2.9; 2973 -2.9; 3270 -3.4; 3597 -3.5; 3957 -3.6; 4353 -4.6; 4788 -3.9; 5267 -2.5; 5793 -0.8; 6373 -0.5; 7010 -3.7; 7711 -7.0; 8482 -7.8; 9330 -7.1; 10263 -7.7; 11289 -7.5; 12418 -5.6; 13660 -7.2; 15026 -11.6; 16529 -11.0; 18182 -7.5; 20000 -8.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 2.45 | 3.0 dB  |
| Peaking | 168 Hz   | 0.69 | -6.7 dB |
| Peaking | 307 Hz   | 0.73 | 6.3 dB  |
| Peaking | 9337 Hz  | 3.02 | -3.3 dB |
| Peaking | 16051 Hz | 1.33 | -8.3 dB |
| Peaking | 23 Hz    | 2.46 | 1.0 dB  |
| Peaking | 1864 Hz  | 2.07 | -1.8 dB |
| Peaking | 2805 Hz  | 3.96 | 1.6 dB  |
| Peaking | 6157 Hz  | 4.14 | 4.8 dB  |
| Peaking | 7827 Hz  | 5.62 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.6 dB  |
| Peaking | 62 Hz    | 1.41 | -0.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.1 dB  |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.6 dB |
| Peaking | 4000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.7 dB |
| Peaking | 16000 Hz | 1.41 | -8.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M40x/Audio-Technica%20ATH-M40x.png)