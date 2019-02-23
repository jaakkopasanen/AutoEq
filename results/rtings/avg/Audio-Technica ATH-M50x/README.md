# Audio-Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -6.0; 23 -6.4; 25 -6.7; 28 -7.1; 31 -7.4; 34 -7.6; 37 -7.7; 41 -7.8; 45 -7.7; 49 -7.5; 54 -7.2; 60 -6.9; 66 -6.7; 72 -6.7; 79 -7.1; 87 -7.8; 96 -8.5; 106 -8.9; 116 -9.1; 128 -9.1; 141 -9.1; 155 -9.2; 170 -8.9; 187 -8.4; 206 -7.5; 227 -6.3; 249 -4.9; 274 -3.5; 302 -3.0; 332 -3.3; 365 -3.4; 402 -4.5; 442 -5.4; 486 -6.0; 535 -6.4; 588 -6.5; 647 -6.7; 712 -6.6; 783 -6.6; 861 -6.6; 947 -6.5; 1042 -6.4; 1146 -6.3; 1261 -6.4; 1387 -6.6; 1526 -6.6; 1678 -7.3; 1846 -8.8; 2031 -9.5; 2234 -8.6; 2457 -7.8; 2703 -7.1; 2973 -6.9; 3270 -5.9; 3597 -5.4; 3957 -7.9; 4353 -10.3; 4788 -7.2; 5267 -3.1; 5793 -0.5; 6373 -2.3; 7010 -4.0; 7711 -6.1; 8482 -6.4; 9330 -6.6; 10263 -7.8; 11289 -9.2; 12418 -8.1; 13660 -6.4; 15026 -6.4; 16529 -8.2; 18182 -12.3; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 182 Hz   | 0.66 | -4.2 dB |
| Peaking | 297 Hz   | 1.5  | 6.4 dB  |
| Peaking | 2023 Hz  | 4.77 | -2.9 dB |
| Peaking | 6077 Hz  | 3.21 | 7.6 dB  |
| Peaking | 19742 Hz | 0.04 | -2.2 dB |
| Peaking | 40 Hz    | 3.04 | -1.0 dB |
| Peaking | 4143 Hz  | 2.04 | 3.3 dB  |
| Peaking | 4333 Hz  | 5.26 | -7.5 dB |
| Peaking | 15446 Hz | 1.53 | 4.4 dB  |
| Peaking | 18300 Hz | 0.9  | -4.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.1 dB |
| Peaking | 250 Hz   | 1.41 | 2.4 dB  |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.1 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M50x/Audio-Technica%20ATH-M50x.png)