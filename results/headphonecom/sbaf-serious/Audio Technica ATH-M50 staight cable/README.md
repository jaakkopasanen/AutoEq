# Audio Technica ATH-M50 staight cable
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.9; 23 -4.7; 25 -5.4; 28 -6.2; 31 -6.9; 34 -7.4; 37 -7.8; 41 -8.1; 45 -8.3; 49 -8.6; 54 -8.7; 60 -8.0; 66 -5.5; 72 -2.7; 79 -4.4; 87 -7.2; 96 -8.9; 106 -9.6; 116 -9.7; 128 -9.9; 141 -10.3; 155 -9.9; 170 -9.1; 187 -9.1; 206 -7.9; 227 -6.9; 249 -6.2; 274 -5.1; 302 -4.1; 332 -3.4; 365 -3.3; 402 -3.8; 442 -4.6; 486 -5.5; 535 -6.2; 588 -6.6; 647 -6.8; 712 -6.9; 783 -6.7; 861 -6.5; 947 -6.3; 1042 -6.3; 1146 -7.1; 1261 -7.2; 1387 -7.6; 1526 -8.6; 1678 -10.0; 1846 -10.6; 2031 -9.9; 2234 -8.7; 2457 -7.5; 2703 -5.6; 2973 -4.1; 3270 -3.2; 3597 -3.4; 3957 -6.2; 4353 -7.7; 4788 -4.9; 5267 -0.8; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -8.6; 9330 -10.9; 10263 -7.9; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50 staight cable GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50 staight cable ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 135 Hz  |  2.29 | -4.3 dB |
| Peaking | 1870 Hz |  2.63 | -4.6 dB |
| Peaking | 3209 Hz |  4.52 | 3.8 dB  |
| Peaking | 5931 Hz |  3.28 | 7.0 dB  |
| Peaking | 9189 Hz |  4.74 | -5.4 dB |
| Peaking | 19 Hz   |  1.47 | 3.8 dB  |
| Peaking | 58 Hz   |  0.84 | -3.2 dB |
| Peaking | 73 Hz   |  4.34 | 7.0 dB  |
| Peaking | 351 Hz  |  2.47 | 3.8 dB  |
| Peaking | 4303 Hz | 10.48 | -3.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.1 dB |
| Peaking | 62 Hz    | 1.41 | 1.6 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.8 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-M50%20staight%20cable/Audio%20Technica%20ATH-M50%20staight%20cable.png)