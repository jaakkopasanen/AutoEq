# Audio-Technica ATH-M50xBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.9; 23 -8.3; 25 -8.6; 28 -9.0; 31 -9.3; 34 -9.5; 37 -9.6; 41 -9.6; 45 -9.5; 49 -9.2; 54 -8.6; 60 -8.2; 66 -8.3; 72 -8.8; 79 -9.4; 87 -10.1; 96 -10.7; 106 -10.9; 116 -11.0; 128 -11.0; 141 -11.0; 155 -10.8; 170 -10.4; 187 -9.8; 206 -9.0; 227 -8.0; 249 -7.1; 274 -5.7; 302 -3.3; 332 -2.0; 365 -1.2; 402 -1.0; 442 -0.9; 486 -1.3; 535 -1.9; 588 -2.5; 647 -3.2; 712 -3.7; 783 -3.8; 861 -3.8; 947 -4.9; 1042 -5.7; 1146 -6.2; 1261 -6.9; 1387 -7.5; 1526 -8.2; 1678 -8.6; 1846 -8.6; 2031 -8.6; 2234 -8.8; 2457 -8.6; 2703 -8.7; 2973 -8.5; 3270 -7.4; 3597 -5.8; 3957 -6.9; 4353 -9.6; 4788 -7.9; 5267 -3.9; 5793 -0.5; 6373 -0.8; 7010 -3.8; 7711 -7.2; 8482 -7.8; 9330 -7.2; 10263 -9.5; 11289 -12.5; 12418 -11.0; 13660 -7.8; 15026 -8.2; 16529 -8.4; 18182 -6.7; 20000 -7.7
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50xBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50xBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 1.46 | -2.7 dB |
| Peaking | 178 Hz   | 0.57 | -7.7 dB |
| Peaking | 388 Hz   | 0.74 | 9.5 dB  |
| Peaking | 6084 Hz  | 2.52 | 10.3 dB |
| Peaking | 6652 Hz  | 0.21 | -4.0 dB |
| Peaking | 1658 Hz  | 3.14 | -1.0 dB |
| Peaking | 3691 Hz  | 4.93 | 3.4 dB  |
| Peaking | 4493 Hz  | 5.79 | -3.3 dB |
| Peaking | 11593 Hz | 3.27 | -7.0 dB |
| Peaking | 11857 Hz | 1.23 | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -5.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.2 dB |
| Peaking | 500 Hz   | 1.41 | 6.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -3.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M50xBT/Audio-Technica%20ATH-M50xBT.png)