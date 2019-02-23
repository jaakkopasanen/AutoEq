# Audio-Technica ATH-M60x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.6; 23 -5.7; 25 -5.9; 28 -6.1; 31 -6.3; 34 -6.4; 37 -6.5; 41 -6.6; 45 -6.8; 49 -7.0; 54 -7.1; 60 -7.3; 66 -7.5; 72 -7.6; 79 -7.8; 87 -8.0; 96 -8.2; 106 -8.5; 116 -8.7; 128 -8.8; 141 -8.9; 155 -9.0; 170 -9.0; 187 -8.9; 206 -8.7; 227 -8.3; 249 -7.9; 274 -7.4; 302 -6.5; 332 -5.1; 365 -2.8; 402 -0.6; 442 -0.5; 486 -2.2; 535 -4.6; 588 -6.2; 647 -7.1; 712 -7.4; 783 -7.4; 861 -7.3; 947 -7.3; 1042 -7.4; 1146 -7.4; 1261 -7.5; 1387 -7.5; 1526 -7.2; 1678 -7.6; 1846 -7.8; 2031 -7.4; 2234 -6.0; 2457 -4.4; 2703 -4.2; 2973 -4.0; 3270 -4.1; 3597 -4.6; 3957 -8.2; 4353 -10.0; 4788 -7.2; 5267 -5.0; 5793 -4.3; 6373 -6.7; 7010 -9.7; 7711 -8.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.9; 15026 -13.8; 16529 -13.4; 18182 -12.0; 20000 -13.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M60x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M60x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 157 Hz   | 0.71 | -2.2 dB |
| Peaking | 423 Hz   | 2.41 | 8.5 dB  |
| Peaking | 822 Hz   | 0.23 | -1.5 dB |
| Peaking | 2858 Hz  | 2.7  | 4.1 dB  |
| Peaking | 17830 Hz | 0.68 | -7.3 dB |
| Peaking | 4346 Hz  | 5.45 | -5.7 dB |
| Peaking | 5786 Hz  | 1.57 | 4.0 dB  |
| Peaking | 7027 Hz  | 3.89 | -5.8 dB |
| Peaking | 13424 Hz | 0.87 | 3.2 dB  |
| Peaking | 14968 Hz | 2.44 | -6.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 0.5 dB  |
| Peaking | 62 Hz    | 1.41 | -0.5 dB |
| Peaking | 125 Hz   | 1.41 | -2.6 dB |
| Peaking | 250 Hz   | 1.41 | -1.4 dB |
| Peaking | 500 Hz   | 1.41 | 4.8 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -8.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M60x/Audio-Technica%20ATH-M60x.png)