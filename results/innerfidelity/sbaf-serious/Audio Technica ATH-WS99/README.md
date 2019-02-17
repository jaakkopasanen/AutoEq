# Audio Technica ATH-WS99
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.5; 23 -4.1; 25 -4.6; 28 -5.3; 31 -5.8; 34 -6.2; 37 -6.6; 41 -7.0; 45 -7.4; 49 -7.7; 54 -8.0; 60 -8.3; 66 -8.5; 72 -9.0; 79 -9.7; 87 -9.9; 96 -10.7; 106 -11.2; 116 -11.4; 128 -11.7; 141 -11.7; 155 -11.9; 170 -11.7; 187 -11.8; 206 -11.7; 227 -11.4; 249 -11.0; 274 -10.4; 302 -10.0; 332 -9.5; 365 -8.8; 402 -8.2; 442 -7.8; 486 -6.9; 535 -5.7; 588 -3.9; 647 -3.0; 712 -3.1; 783 -3.6; 861 -4.7; 947 -5.8; 1042 -6.8; 1146 -7.6; 1261 -8.3; 1387 -9.0; 1526 -9.4; 1678 -9.2; 1846 -8.1; 2031 -6.6; 2234 -4.9; 2457 -2.8; 2703 -0.9; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -4.2; 4788 -8.1; 5267 -4.2; 5793 -0.6; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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
| Peaking | 11 Hz   | 0.46 | 4.7 dB  |
| Peaking | 611 Hz  | 0.12 | -7.3 dB |
| Peaking | 672 Hz  | 0.98 | 10.4 dB |
| Peaking | 3090 Hz | 1.45 | 11.6 dB |
| Peaking | 6183 Hz | 4.24 | 7.1 dB  |
| Peaking | 301 Hz  | 3.64 | 0.7 dB  |
| Peaking | 1586 Hz | 4.31 | -1.5 dB |
| Peaking | 4013 Hz | 8.77 | 2.9 dB  |
| Peaking | 4763 Hz | 9.2  | -4.4 dB |
| Peaking | 5470 Hz | 0.22 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -4.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.2 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.0 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-WS99/Audio%20Technica%20ATH-WS99.png)