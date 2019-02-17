# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.9; 23 -9.2; 25 -9.4; 28 -9.7; 31 -9.8; 34 -9.9; 37 -9.9; 41 -9.9; 45 -9.7; 49 -9.4; 54 -9.2; 60 -8.8; 66 -7.6; 72 -5.9; 79 -4.6; 87 -6.2; 96 -9.3; 106 -11.0; 116 -9.9; 128 -10.5; 141 -11.2; 155 -10.2; 170 -8.8; 187 -9.2; 206 -7.8; 227 -6.5; 249 -5.3; 274 -4.2; 302 -3.2; 332 -2.8; 365 -2.7; 402 -3.3; 442 -4.0; 486 -5.0; 535 -5.6; 588 -6.1; 647 -6.4; 712 -6.7; 783 -6.8; 861 -6.6; 947 -6.6; 1042 -6.4; 1146 -5.9; 1261 -6.6; 1387 -7.2; 1526 -8.3; 1678 -9.2; 1846 -9.4; 2031 -8.9; 2234 -8.1; 2457 -7.0; 2703 -5.9; 2973 -4.1; 3270 -2.5; 3597 -1.4; 3957 -2.9; 4353 -5.7; 4788 -3.0; 5267 -0.5; 5793 -1.1; 6373 -1.6; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.6dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 1.26 | -3.8 dB |
| Peaking | 139 Hz  | 1.75 | -4.8 dB |
| Peaking | 340 Hz  | 2.02 | 4.6 dB  |
| Peaking | 3541 Hz | 5.31 | 5.0 dB  |
| Peaking | 5652 Hz | 3.09 | 6.3 dB  |
| Peaking | 57 Hz   | 2.62 | -1.7 dB |
| Peaking | 79 Hz   | 3.48 | 4.0 dB  |
| Peaking | 102 Hz  | 6.32 | -3.0 dB |
| Peaking | 1871 Hz | 2.45 | -3.4 dB |
| Peaking | 3016 Hz | 5.81 | 1.6 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -5.2 dB |
| Peaking | 250 Hz   | 1.41 | 2.3 dB  |
| Peaking | 500 Hz   | 1.41 | 1.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.2 dB |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 5.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.8 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)