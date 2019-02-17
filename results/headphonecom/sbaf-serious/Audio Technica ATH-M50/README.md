# Audio Technica ATH-M50
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.1; 23 -4.9; 25 -5.6; 28 -6.4; 31 -7.1; 34 -7.6; 37 -8.0; 41 -8.3; 45 -8.5; 49 -8.8; 54 -8.9; 60 -8.2; 66 -5.7; 72 -2.9; 79 -4.6; 87 -7.4; 96 -9.1; 106 -9.8; 116 -9.9; 128 -10.1; 141 -10.5; 155 -10.1; 170 -9.3; 187 -9.3; 206 -8.2; 227 -7.1; 249 -6.4; 274 -5.3; 302 -4.3; 332 -3.6; 365 -3.5; 402 -4.1; 442 -4.8; 486 -5.7; 535 -6.4; 588 -6.8; 647 -7.0; 712 -7.1; 783 -6.9; 861 -6.7; 947 -6.5; 1042 -6.5; 1146 -7.3; 1261 -7.4; 1387 -7.8; 1526 -8.8; 1678 -10.2; 1846 -10.8; 2031 -10.1; 2234 -8.9; 2457 -7.7; 2703 -5.8; 2973 -4.3; 3270 -3.4; 3597 -3.6; 3957 -6.4; 4353 -7.9; 4788 -5.1; 5267 -0.9; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -8.8; 9330 -11.1; 10263 -8.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.4
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 135 Hz  |  2.12 | -4.5 dB |
| Peaking | 1868 Hz |  2.4  | -4.7 dB |
| Peaking | 3201 Hz |  4.6  | 3.7 dB  |
| Peaking | 5948 Hz |  3.34 | 7.0 dB  |
| Peaking | 9202 Hz |  4.68 | -5.6 dB |
| Peaking | 18 Hz   |  1.51 | 3.6 dB  |
| Peaking | 57 Hz   |  0.86 | -3.3 dB |
| Peaking | 72 Hz   |  4.52 | 7.0 dB  |
| Peaking | 350 Hz  |  2.66 | 3.6 dB  |
| Peaking | 4247 Hz | 10.03 | -3.2 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-3.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.3 dB |
| Peaking | 62 Hz    | 1.41 | 1.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | 1.2 dB  |
| Peaking | 500 Hz   | 1.41 | 1.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -4.0 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-M50/Audio%20Technica%20ATH-M50.png)