# Audio-Technica ATH-ANC7b
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.8; 23 -4.3; 25 -4.8; 28 -5.4; 31 -6.0; 34 -6.5; 37 -6.9; 41 -7.3; 45 -7.6; 49 -7.9; 54 -8.3; 60 -8.7; 66 -9.0; 72 -9.3; 79 -9.7; 87 -10.1; 96 -10.5; 106 -10.8; 116 -11.1; 128 -11.4; 141 -11.6; 155 -11.7; 170 -11.6; 187 -11.4; 206 -11.2; 227 -11.0; 249 -10.8; 274 -10.7; 302 -10.6; 332 -10.6; 365 -10.6; 402 -10.6; 442 -10.7; 486 -10.6; 535 -10.2; 588 -9.6; 647 -8.9; 712 -8.7; 783 -9.7; 861 -10.8; 947 -10.7; 1042 -7.6; 1146 -4.7; 1261 -5.0; 1387 -4.6; 1526 -4.0; 1678 -4.0; 1846 -3.8; 2031 -3.3; 2234 -4.7; 2457 -3.2; 2703 -0.8; 2973 -0.5; 3270 -0.5; 3597 -1.3; 3957 -1.9; 4353 -2.3; 4788 -1.7; 5267 -4.1; 5793 -5.4; 6373 -2.2; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -7.6; 16529 -7.0; 18182 -6.5; 20000 -12.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC7b GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.6dB**.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  1.44 | 3.3 dB  |
| Peaking | 150 Hz   |  0.51 | -5.0 dB |
| Peaking | 473 Hz   |  1.52 | -2.7 dB |
| Peaking | 890 Hz   |  5.1  | -4.7 dB |
| Peaking | 3178 Hz  |  0.79 | 5.6 dB  |
| Peaking | 1166 Hz  |  5.93 | 1.7 dB  |
| Peaking | 2287 Hz  |  5.15 | -4.1 dB |
| Peaking | 2412 Hz  |  1.16 | 2.4 dB  |
| Peaking | 6567 Hz  | 10.61 | 3.7 dB  |
| Peaking | 16452 Hz |  0.02 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.9 dB |
| Peaking | 125 Hz   | 1.41 | -4.4 dB |
| Peaking | 250 Hz   | 1.41 | -3.4 dB |
| Peaking | 500 Hz   | 1.41 | -3.3 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | 3.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 16000 Hz | 1.41 | -1.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC7b/Audio-Technica%20ATH-ANC7b.png)