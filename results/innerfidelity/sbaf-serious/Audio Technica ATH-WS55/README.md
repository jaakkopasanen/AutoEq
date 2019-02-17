# Audio Technica ATH-WS55
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -3.1; 25 -3.8; 28 -4.6; 31 -5.2; 34 -5.8; 37 -6.2; 41 -6.5; 45 -6.9; 49 -7.3; 54 -7.7; 60 -8.0; 66 -8.2; 72 -8.3; 79 -8.5; 87 -8.6; 96 -8.7; 106 -9.0; 116 -9.3; 128 -9.8; 141 -9.9; 155 -10.0; 170 -9.8; 187 -9.8; 206 -9.5; 227 -8.5; 249 -7.4; 274 -6.8; 302 -6.5; 332 -5.9; 365 -5.9; 402 -5.3; 442 -4.5; 486 -4.3; 535 -4.3; 588 -4.3; 647 -4.7; 712 -5.2; 783 -5.5; 861 -6.0; 947 -6.4; 1042 -6.6; 1146 -4.9; 1261 -6.1; 1387 -6.7; 1526 -6.6; 1678 -5.6; 1846 -4.5; 2031 -2.7; 2234 -0.9; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -2.2; 7010 -4.8; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-WS55 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-WS55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.08 | 5.0 dB  |
| Peaking | 75 Hz   | 0.72 | -1.7 dB |
| Peaking | 163 Hz  | 1.39 | -3.1 dB |
| Peaking | 493 Hz  | 1.83 | 2.6 dB  |
| Peaking | 3677 Hz | 0.89 | 7.0 dB  |
| Peaking | 1541 Hz | 2.75 | -2.1 dB |
| Peaking | 2317 Hz | 3.27 | 2.6 dB  |
| Peaking | 3678 Hz | 2.76 | -1.2 dB |
| Peaking | 5890 Hz | 2.39 | 4.3 dB  |
| Peaking | 7203 Hz | 1.25 | -2.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -1.5 dB |
| Peaking | 125 Hz   | 1.41 | -3.3 dB |
| Peaking | 250 Hz   | 1.41 | -1.5 dB |
| Peaking | 500 Hz   | 1.41 | 3.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.2 dB |
| Peaking | 2000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-WS55/Audio%20Technica%20ATH-WS55.png)