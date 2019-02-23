# Audio Technica ATH-R70x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.6; 23 -1.0; 25 -1.6; 28 -2.6; 31 -3.4; 34 -4.2; 37 -4.8; 41 -5.5; 45 -6.1; 49 -6.5; 54 -7.0; 60 -7.5; 66 -7.8; 72 -8.1; 79 -8.4; 87 -8.5; 96 -8.2; 106 -8.8; 116 -9.1; 128 -9.3; 141 -9.3; 155 -9.4; 170 -9.3; 187 -9.3; 206 -9.2; 227 -8.9; 249 -8.8; 274 -8.6; 302 -8.4; 332 -8.1; 365 -7.9; 402 -7.6; 442 -7.3; 486 -7.4; 535 -7.2; 588 -6.8; 647 -6.7; 712 -6.9; 783 -6.4; 861 -6.6; 947 -6.5; 1042 -6.3; 1146 -6.5; 1261 -6.9; 1387 -7.6; 1526 -8.2; 1678 -8.8; 1846 -8.7; 2031 -8.2; 2234 -7.5; 2457 -6.4; 2703 -4.5; 2973 -3.9; 3270 -4.8; 3597 -6.8; 3957 -5.3; 4353 -4.0; 4788 -2.5; 5267 -0.6; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -7.4; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-R70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-R70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  1.18 | 6.0 dB  |
| Peaking | 146 Hz  |  0.54 | -3.0 dB |
| Peaking | 1809 Hz |  2.5  | -2.7 dB |
| Peaking | 2877 Hz |  6.35 | 3.2 dB  |
| Peaking | 5634 Hz |  2.73 | 6.8 dB  |
| Peaking | 61 Hz   |  2.46 | -0.4 dB |
| Peaking | 1008 Hz |  3.2  | 0.6 dB  |
| Peaking | 3613 Hz | 13.2  | -1.4 dB |
| Peaking | 6613 Hz |  9    | 1.9 dB  |
| Peaking | 8546 Hz |  2.26 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.3 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.5 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.3 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -2.5 dB |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-R70x/Audio%20Technica%20ATH-R70x.png)