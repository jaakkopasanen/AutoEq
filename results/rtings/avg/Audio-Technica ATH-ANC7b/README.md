# Audio-Technica ATH-ANC7b
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.0; 23 -4.5; 25 -4.9; 28 -5.6; 31 -6.2; 34 -6.6; 37 -7.0; 41 -7.5; 45 -7.8; 49 -8.1; 54 -8.4; 60 -8.8; 66 -9.2; 72 -9.6; 79 -9.9; 87 -10.3; 96 -10.7; 106 -11.0; 116 -11.4; 128 -11.6; 141 -11.8; 155 -11.8; 170 -11.8; 187 -11.6; 206 -11.3; 227 -11.1; 249 -10.9; 274 -10.7; 302 -10.7; 332 -10.6; 365 -10.6; 402 -10.7; 442 -10.7; 486 -10.6; 535 -10.1; 588 -9.4; 647 -8.8; 712 -8.5; 783 -9.5; 861 -10.8; 947 -10.5; 1042 -7.5; 1146 -4.4; 1261 -4.8; 1387 -4.6; 1526 -3.6; 1678 -3.8; 1846 -3.5; 2031 -2.8; 2234 -4.0; 2457 -2.2; 2703 -0.5; 2973 -0.5; 3270 -0.6; 3597 -1.4; 3957 -2.3; 4353 -2.6; 4788 -1.2; 5267 -3.8; 5793 -5.5; 6373 -3.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -8.1; 16529 -7.3; 18182 -6.5; 20000 -12.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7b GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.9dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 144 Hz   |  0.62 | -5.1 dB |
| Peaking | 454 Hz   |  1.14 | -3.0 dB |
| Peaking | 924 Hz   |  3.18 | -6.9 dB |
| Peaking | 1094 Hz  |  1.66 | 3.7 dB  |
| Peaking | 3228 Hz  |  0.94 | 5.7 dB  |
| Peaking | 22 Hz    |  2.08 | 2.8 dB  |
| Peaking | 3842 Hz  | 10.09 | -0.7 dB |
| Peaking | 6700 Hz  |  9.62 | 3.4 dB  |
| Peaking | 8268 Hz  |  1.58 | -1.0 dB |
| Peaking | 20019 Hz |  1.96 | -5.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.2 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -3.5 dB |
| Peaking | 500 Hz   | 1.41 | -3.2 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC7b/Audio-Technica%20ATH-ANC7b.png)