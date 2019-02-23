# Audio Technica ATH-WS99
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.6; 23 -4.2; 25 -4.8; 28 -5.4; 31 -5.9; 34 -6.4; 37 -6.7; 41 -7.2; 45 -7.6; 49 -7.9; 54 -8.2; 60 -8.4; 66 -8.6; 72 -9.2; 79 -9.9; 87 -10.1; 96 -10.8; 106 -11.4; 116 -11.5; 128 -11.8; 141 -11.9; 155 -12.1; 170 -11.8; 187 -11.9; 206 -11.9; 227 -11.5; 249 -11.1; 274 -10.5; 302 -10.2; 332 -9.7; 365 -9.0; 402 -8.4; 442 -8.0; 486 -7.1; 535 -5.8; 588 -4.0; 647 -3.2; 712 -3.2; 783 -3.7; 861 -4.8; 947 -5.9; 1042 -7.0; 1146 -7.7; 1261 -8.5; 1387 -9.2; 1526 -9.6; 1678 -9.4; 1846 -8.2; 2031 -6.7; 2234 -5.0; 2457 -2.9; 2703 -1.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -4.4; 4788 -8.3; 5267 -4.4; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-WS99 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-WS99 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.49 | 4.5 dB  |
| Peaking | 602 Hz  | 0.12 | -7.4 dB |
| Peaking | 672 Hz  | 0.98 | 10.4 dB |
| Peaking | 3086 Hz | 1.47 | 11.6 dB |
| Peaking | 6194 Hz | 4.26 | 7.2 dB  |
| Peaking | 1511 Hz | 3.86 | -1.3 dB |
| Peaking | 1735 Hz | 1.75 | 1.4 dB  |
| Peaking | 1763 Hz | 3.83 | -1.9 dB |
| Peaking | 4008 Hz | 8.28 | 3.0 dB  |
| Peaking | 4763 Hz | 9.58 | -4.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | -1.7 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -5.0 dB |
| Peaking | 500 Hz   | 1.41 | 2.1 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.1 dB |
| Peaking | 2000 Hz  | 1.41 | -1.3 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-WS99/Audio%20Technica%20ATH-WS99.png)