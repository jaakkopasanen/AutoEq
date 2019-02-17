# Audio Technica ATH-ANC7b
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.7; 31 -1.1; 34 -1.6; 37 -2.0; 41 -2.5; 45 -2.8; 49 -3.1; 54 -3.5; 60 -3.9; 66 -4.2; 72 -4.5; 79 -4.8; 87 -5.1; 96 -5.5; 106 -5.5; 116 -5.6; 128 -5.6; 141 -5.8; 155 -5.8; 170 -5.6; 187 -5.4; 206 -5.3; 227 -5.0; 249 -4.7; 274 -4.4; 302 -4.1; 332 -3.8; 365 -3.7; 402 -3.5; 442 -3.6; 486 -3.9; 535 -3.8; 588 -3.7; 647 -3.7; 712 -4.5; 783 -6.1; 861 -6.6; 947 -6.6; 1042 -6.8; 1146 -5.8; 1261 -1.6; 1387 -0.6; 1526 -1.0; 1678 -0.5; 1846 -0.5; 2031 -1.1; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC7b GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7b ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.8  | 6.0 dB  |
| Peaking | 54 Hz   | 1.28 | 1.1 dB  |
| Peaking | 384 Hz  | 0.95 | 2.0 dB  |
| Peaking | 962 Hz  | 2.47 | -5.3 dB |
| Peaking | 2387 Hz | 0.4  | 6.8 dB  |
| Peaking | 1142 Hz | 7.33 | -3.1 dB |
| Peaking | 1275 Hz | 3.36 | 2.6 dB  |
| Peaking | 2250 Hz | 1.47 | -0.9 dB |
| Peaking | 6223 Hz | 1.68 | 6.3 dB  |
| Peaking | 7473 Hz | 1.32 | -5.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.2 dB  |
| Peaking | 62 Hz    | 1.41 | 1.3 dB  |
| Peaking | 125 Hz   | 1.41 | -0.1 dB |
| Peaking | 250 Hz   | 1.41 | 1.4 dB  |
| Peaking | 500 Hz   | 1.41 | 2.9 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC7b/Audio%20Technica%20ATH-ANC7b.png)