# Audio Technica ATH-IM02
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.4; 23 -4.5; 25 -4.7; 28 -4.8; 31 -5.0; 34 -5.1; 37 -5.3; 41 -5.5; 45 -5.6; 49 -5.8; 54 -6.1; 60 -6.4; 66 -6.8; 72 -7.1; 79 -7.5; 87 -7.9; 96 -8.4; 106 -8.7; 116 -8.9; 128 -9.2; 141 -9.5; 155 -9.7; 170 -9.8; 187 -9.9; 206 -9.9; 227 -9.8; 249 -9.8; 274 -9.6; 302 -9.5; 332 -9.3; 365 -9.0; 402 -8.7; 442 -8.3; 486 -8.1; 535 -7.7; 588 -7.0; 647 -6.7; 712 -6.5; 783 -6.1; 861 -6.2; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -7.0; 1387 -7.5; 1526 -8.1; 1678 -8.6; 1846 -8.9; 2031 -9.1; 2234 -8.7; 2457 -7.1; 2703 -3.8; 2973 -0.7; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -2.5; 4788 -4.2; 5267 -6.3; 5793 -5.8; 6373 -3.7; 7010 -4.7; 7711 -7.3; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -7.1; 15026 -6.8; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-IM02 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-IM02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.56 | 2.1 dB  |
| Peaking | 192 Hz  | 0.63 | -3.7 dB |
| Peaking | 2219 Hz | 1.8  | -5.9 dB |
| Peaking | 3068 Hz | 1.77 | 8.0 dB  |
| Peaking | 3985 Hz | 4.55 | 2.8 dB  |
| Peaking | 828 Hz  | 2.47 | 1.0 dB  |
| Peaking | 1585 Hz | 5.61 | -0.7 dB |
| Peaking | 5483 Hz | 6.37 | -2.4 dB |
| Peaking | 6588 Hz | 3.54 | 3.3 dB  |
| Peaking | 7619 Hz | 4.22 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.0 dB  |
| Peaking | 62 Hz    | 1.41 | 0.0 dB  |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -3.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.8 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.3 dB |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-IM02/Audio%20Technica%20ATH-IM02.png)