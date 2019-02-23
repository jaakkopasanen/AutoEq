# Audio Technica ATH-A55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -0.9; 79 -1.1; 87 -1.1; 96 -1.1; 106 -1.0; 116 -0.9; 128 -0.7; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.8; 249 -3.8; 274 -6.7; 302 -8.6; 332 -9.9; 365 -10.1; 402 -9.7; 442 -9.2; 486 -8.8; 535 -8.6; 588 -8.6; 647 -8.3; 712 -8.4; 783 -8.5; 861 -8.1; 947 -8.7; 1042 -9.1; 1146 -9.3; 1261 -9.4; 1387 -9.5; 1526 -9.2; 1678 -7.8; 1846 -7.3; 2031 -7.4; 2234 -8.4; 2457 -8.5; 2703 -6.7; 2973 -5.9; 3270 -4.5; 3597 -1.1; 3957 -7.7; 4353 -12.6; 4788 -8.4; 5267 -3.4; 5793 -1.1; 6373 -5.8; 7010 -8.2; 7711 -11.2; 8482 -11.6; 9330 -10.0; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 68 Hz   | 0.11 | 6.9 dB   |
| Peaking | 237 Hz  | 0.71 | 18.7 dB  |
| Peaking | 298 Hz  | 0.6  | -23.8 dB |
| Peaking | 5703 Hz | 8.04 | 7.3 dB   |
| Peaking | 8239 Hz | 3.37 | -5.8 dB  |
| Peaking | 1367 Hz | 1.67 | -3.6 dB  |
| Peaking | 2003 Hz | 0.59 | 3.3 dB   |
| Peaking | 2378 Hz | 3.38 | -3.5 dB  |
| Peaking | 3599 Hz | 7.01 | 6.3 dB   |
| Peaking | 4302 Hz | 5.76 | -8.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.3 dB  |
| Peaking | 62 Hz    | 1.41 | 3.6 dB  |
| Peaking | 125 Hz   | 1.41 | 5.9 dB  |
| Peaking | 250 Hz   | 1.41 | 1.8 dB  |
| Peaking | 500 Hz   | 1.41 | -3.6 dB |
| Peaking | 1000 Hz  | 1.41 | -1.7 dB |
| Peaking | 2000 Hz  | 1.41 | -1.4 dB |
| Peaking | 4000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.0 dB |
| Peaking | 16000 Hz | 1.41 | 0.4 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A55/Audio%20Technica%20ATH-A55.png)