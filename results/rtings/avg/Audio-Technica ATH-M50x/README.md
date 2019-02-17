# Audio-Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.9; 23 -6.3; 25 -6.6; 28 -7.0; 31 -7.3; 34 -7.5; 37 -7.6; 41 -7.7; 45 -7.6; 49 -7.4; 54 -7.1; 60 -6.7; 66 -6.5; 72 -6.6; 79 -7.0; 87 -7.7; 96 -8.3; 106 -8.8; 116 -8.9; 128 -9.0; 141 -9.0; 155 -9.1; 170 -8.8; 187 -8.2; 206 -7.4; 227 -6.1; 249 -4.7; 274 -3.3; 302 -2.9; 332 -3.1; 365 -3.3; 402 -4.3; 442 -5.3; 486 -5.9; 535 -6.2; 588 -6.4; 647 -6.6; 712 -6.5; 783 -6.5; 861 -6.4; 947 -6.4; 1042 -6.3; 1146 -6.2; 1261 -6.2; 1387 -6.5; 1526 -6.5; 1678 -7.2; 1846 -8.7; 2031 -9.4; 2234 -8.5; 2457 -7.6; 2703 -7.0; 2973 -6.8; 3270 -5.8; 3597 -5.2; 3957 -7.8; 4353 -10.2; 4788 -7.1; 5267 -3.0; 5793 -0.5; 6373 -2.2; 7010 -3.9; 7711 -6.1; 8482 -6.4; 9330 -6.5; 10263 -7.6; 11289 -9.0; 12418 -8.0; 13660 -6.4; 15026 -6.4; 16529 -8.1; 18182 -12.2; 20000 -10.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 156 Hz   | 0.87 | -3.5 dB |
| Peaking | 302 Hz   | 1.73 | 5.2 dB  |
| Peaking | 2018 Hz  | 4.78 | -2.9 dB |
| Peaking | 6067 Hz  | 3.24 | 7.6 dB  |
| Peaking | 20624 Hz | 0.04 | -2.1 dB |
| Peaking | 37 Hz    | 2.9  | -1.0 dB |
| Peaking | 3587 Hz  | 5.37 | 2.0 dB  |
| Peaking | 4344 Hz  | 6.51 | -4.8 dB |
| Peaking | 15507 Hz | 1.51 | 4.3 dB  |
| Peaking | 18217 Hz | 0.91 | -4.7 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.7 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M50x/Audio-Technica%20ATH-M50x.png)