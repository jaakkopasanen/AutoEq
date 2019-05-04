# Audio-Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.7; 23 -6.1; 25 -6.5; 28 -6.9; 31 -7.2; 34 -7.4; 37 -7.5; 41 -7.6; 45 -7.5; 49 -7.3; 54 -7.0; 60 -6.7; 66 -6.4; 72 -6.4; 79 -6.8; 87 -7.5; 96 -8.2; 106 -8.6; 116 -8.8; 128 -8.9; 141 -8.9; 155 -8.9; 170 -8.7; 187 -8.1; 206 -7.3; 227 -6.1; 249 -4.8; 274 -3.4; 302 -2.9; 332 -3.1; 365 -3.4; 402 -4.4; 442 -5.3; 486 -6.0; 535 -6.4; 588 -6.6; 647 -6.7; 712 -6.8; 783 -6.8; 861 -6.6; 947 -6.5; 1042 -6.4; 1146 -6.2; 1261 -6.5; 1387 -6.7; 1526 -6.8; 1678 -7.5; 1846 -9.0; 2031 -9.9; 2234 -9.5; 2457 -8.6; 2703 -7.7; 2973 -6.9; 3270 -5.6; 3597 -5.1; 3957 -7.6; 4353 -9.8; 4788 -7.5; 5267 -3.4; 5793 -0.5; 6373 -1.3; 7010 -3.8; 7711 -6.1; 8482 -6.3; 9330 -6.3; 10263 -7.3; 11289 -10.1; 12418 -8.3; 13660 -6.3; 15026 -6.3; 16529 -8.2; 18182 -12.2; 20000 -9.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 324 Hz   | 3.39 | 4.0 dB  |
| Peaking | 2109 Hz  | 2.76 | -3.8 dB |
| Peaking | 6049 Hz  | 4.81 | 6.9 dB  |
| Peaking | 11415 Hz | 5.47 | -4.1 dB |
| Peaking | 18779 Hz | 1.39 | -6.7 dB |
| Peaking | 39 Hz    | 2.67 | -1.1 dB |
| Peaking | 144 Hz   | 1.21 | -3.0 dB |
| Peaking | 265 Hz   | 4.09 | 2.0 dB  |
| Peaking | 4260 Hz  | 1.84 | 3.1 dB  |
| Peaking | 4355 Hz  | 4.77 | -7.4 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.0 dB |
| Peaking | 62 Hz    | 1.41 | 0.6 dB  |
| Peaking | 125 Hz   | 1.41 | -3.8 dB |
| Peaking | 250 Hz   | 1.41 | 2.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.8 dB |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 16000 Hz | 1.41 | -2.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M50x/Audio-Technica%20ATH-M50x.png)