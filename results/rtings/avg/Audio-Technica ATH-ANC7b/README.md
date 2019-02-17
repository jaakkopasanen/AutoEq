# Audio-Technica ATH-ANC7b
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.9; 23 -1.4; 25 -1.9; 28 -2.5; 31 -3.1; 34 -3.5; 37 -3.9; 41 -4.4; 45 -4.7; 49 -5.0; 54 -5.3; 60 -5.7; 66 -6.1; 72 -6.5; 79 -6.8; 87 -7.2; 96 -7.6; 106 -8.0; 116 -8.3; 128 -8.5; 141 -8.7; 155 -8.8; 170 -8.7; 187 -8.5; 206 -8.2; 227 -8.0; 249 -7.8; 274 -7.7; 302 -7.6; 332 -7.5; 365 -7.5; 402 -7.6; 442 -7.6; 486 -7.5; 535 -7.0; 588 -6.4; 647 -5.7; 712 -5.4; 783 -6.4; 861 -7.7; 947 -7.4; 1042 -4.5; 1146 -1.3; 1261 -1.7; 1387 -1.5; 1526 -0.6; 1678 -0.7; 1846 -0.5; 2031 -0.5; 2234 -1.0; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -1.1; 5793 -2.4; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7b GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 14 Hz   |  0.5  | 6.7 dB  |
| Peaking | 151 Hz  |  0.81 | -2.6 dB |
| Peaking | 467 Hz  |  1.52 | -2.1 dB |
| Peaking | 900 Hz  |  4.47 | -5.0 dB |
| Peaking | 2301 Hz |  0.4  | 6.7 dB  |
| Peaking | 1133 Hz | 15.16 | 2.0 dB  |
| Peaking | 2379 Hz |  2.54 | -0.9 dB |
| Peaking | 6560 Hz |  1.35 | 5.3 dB  |
| Peaking | 7695 Hz |  1.34 | -5.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.2 dB  |
| Peaking | 125 Hz   | 1.41 | -2.2 dB |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | -1.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC7b/Audio-Technica%20ATH-ANC7b.png)