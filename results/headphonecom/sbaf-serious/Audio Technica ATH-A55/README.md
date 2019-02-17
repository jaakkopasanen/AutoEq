# Audio Technica ATH-A55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -0.5; 87 -0.5; 96 -0.5; 106 -0.5; 116 -0.5; 128 -0.5; 141 -0.5; 155 -0.5; 170 -0.5; 187 -0.5; 206 -0.5; 227 -0.5; 249 -1.3; 274 -4.3; 302 -6.2; 332 -7.5; 365 -7.7; 402 -7.3; 442 -6.8; 486 -6.4; 535 -6.2; 588 -6.2; 647 -6.0; 712 -6.0; 783 -6.1; 861 -5.7; 947 -6.3; 1042 -6.7; 1146 -6.9; 1261 -7.0; 1387 -7.1; 1526 -6.8; 1678 -5.4; 1846 -4.9; 2031 -5.0; 2234 -6.0; 2457 -6.1; 2703 -4.3; 2973 -3.5; 3270 -2.1; 3597 -0.5; 3957 -5.3; 4353 -10.2; 4788 -6.0; 5267 -1.3; 5793 -0.5; 6373 -3.4; 7010 -5.8; 7711 -8.8; 8482 -9.2; 9330 -7.7; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-A55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 60 Hz   | 0.27 | 6.8 dB   |
| Peaking | 1225 Hz | 3.99 | -0.8 dB  |
| Peaking | 3688 Hz | 1.56 | 22.0 dB  |
| Peaking | 4229 Hz | 1.35 | -23.0 dB |
| Peaking | 5509 Hz | 2.84 | 11.4 dB  |
| Peaking | 18 Hz   | 2.53 | 1.2 dB   |
| Peaking | 232 Hz  | 1.89 | 4.3 dB   |
| Peaking | 328 Hz  | 1.86 | -4.8 dB  |
| Peaking | 1844 Hz | 6.97 | 1.5 dB   |
| Peaking | 8151 Hz | 6.9  | -2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 4.1 dB  |
| Peaking | 125 Hz   | 1.41 | 5.6 dB  |
| Peaking | 250 Hz   | 1.41 | 3.0 dB  |
| Peaking | 500 Hz   | 1.41 | -1.5 dB |
| Peaking | 1000 Hz  | 1.41 | -0.0 dB |
| Peaking | 2000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.1 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.9 dB |
| Peaking | 16000 Hz | 1.41 | 0.0 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A55/Audio%20Technica%20ATH-A55.png)