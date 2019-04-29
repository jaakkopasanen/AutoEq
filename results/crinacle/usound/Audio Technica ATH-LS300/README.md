# Audio Technica ATH-LS300
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.3; 23 -10.4; 25 -10.4; 28 -10.4; 31 -10.4; 34 -10.4; 37 -10.4; 41 -10.4; 45 -10.4; 49 -10.4; 54 -10.3; 60 -10.3; 66 -10.4; 72 -10.6; 79 -10.6; 87 -10.8; 96 -10.9; 106 -11.0; 116 -11.1; 128 -11.1; 141 -11.2; 155 -11.3; 170 -11.2; 187 -11.2; 206 -11.1; 227 -11.0; 249 -10.9; 274 -10.7; 302 -10.6; 332 -10.4; 365 -10.2; 402 -10.0; 442 -9.7; 486 -9.4; 535 -9.0; 588 -8.6; 647 -8.2; 712 -7.7; 783 -7.2; 861 -6.8; 947 -6.6; 1042 -6.7; 1146 -7.4; 1261 -8.1; 1387 -8.4; 1526 -8.2; 1678 -7.5; 1846 -6.6; 2031 -5.6; 2234 -4.8; 2457 -4.2; 2703 -3.9; 2973 -3.9; 3270 -3.6; 3597 -2.0; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -7.3; 7711 -10.1; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-LS300 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-LS300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.12 | -3.7 dB |
| Peaking | 263 Hz   | 0.56 | -2.9 dB |
| Peaking | 1465 Hz  | 3.58 | -2.4 dB |
| Peaking | 4988 Hz  | 1.02 | 7.1 dB  |
| Peaking | 7578 Hz  | 4.66 | -7.6 dB |
| Peaking | 906 Hz   | 5.18 | 0.9 dB  |
| Peaking | 2434 Hz  | 6.3  | 0.8 dB  |
| Peaking | 4988 Hz  | 6.14 | -0.8 dB |
| Peaking | 6301 Hz  | 8.59 | 1.9 dB  |
| Peaking | 10914 Hz | 1.67 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.0 dB |
| Peaking | 62 Hz    | 1.41 | -2.7 dB |
| Peaking | 125 Hz   | 1.41 | -3.7 dB |
| Peaking | 250 Hz   | 1.41 | -3.7 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 7.3 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.0 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/crinacle/usound/Audio%20Technica%20ATH-LS300/Audio%20Technica%20ATH-LS300.png)