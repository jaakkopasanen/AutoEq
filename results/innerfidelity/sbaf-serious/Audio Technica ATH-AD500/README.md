# Audio Technica ATH-AD500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.6; 72 -1.2; 79 -1.7; 87 -2.6; 96 -3.7; 106 -4.3; 116 -4.5; 128 -5.1; 141 -5.4; 155 -5.5; 170 -5.5; 187 -5.6; 206 -5.6; 227 -5.4; 249 -5.5; 274 -5.5; 302 -5.4; 332 -5.4; 365 -5.4; 402 -5.2; 442 -5.1; 486 -5.3; 535 -5.4; 588 -5.2; 647 -5.3; 712 -5.4; 783 -5.3; 861 -5.8; 947 -6.3; 1042 -6.7; 1146 -7.0; 1261 -7.5; 1387 -7.7; 1526 -7.5; 1678 -6.9; 1846 -6.5; 2031 -5.4; 2234 -4.8; 2457 -3.0; 2703 -2.0; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -3.6; 4353 -5.1; 4788 -4.2; 5267 -1.0; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -7.4; 9330 -9.5; 10263 -7.2; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 37 Hz   | 0.5  | 6.7 dB  |
| Peaking | 487 Hz  | 1.52 | 1.3 dB  |
| Peaking | 3137 Hz | 2.65 | 6.5 dB  |
| Peaking | 5923 Hz | 3.09 | 6.3 dB  |
| Peaking | 9195 Hz | 4.03 | -3.5 dB |
| Peaking | 71 Hz   | 1.66 | 3.3 dB  |
| Peaking | 74 Hz   | 0.85 | -2.2 dB |
| Peaking | 1439 Hz | 1.41 | -3.3 dB |
| Peaking | 1534 Hz | 0.56 | 1.7 dB  |
| Peaking | 4249 Hz | 8.88 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 5.2 dB  |
| Peaking | 125 Hz   | 1.41 | 0.3 dB  |
| Peaking | 250 Hz   | 1.41 | 0.4 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.9 dB |
| Peaking | 2000 Hz  | 1.41 | 0.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.2 dB |
| Peaking | 16000 Hz | 1.41 | -0.2 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD500/Audio%20Technica%20ATH-AD500.png)