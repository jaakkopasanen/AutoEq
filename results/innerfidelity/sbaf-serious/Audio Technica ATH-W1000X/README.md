# Audio Technica ATH-W1000X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.8; 45 -1.7; 49 -2.6; 54 -3.6; 60 -5.0; 66 -5.9; 72 -6.5; 79 -7.5; 87 -8.2; 96 -8.6; 106 -8.9; 116 -8.8; 128 -8.9; 141 -8.9; 155 -8.8; 170 -8.4; 187 -8.3; 206 -8.2; 227 -7.8; 249 -7.5; 274 -7.0; 302 -6.6; 332 -6.1; 365 -5.5; 402 -4.5; 442 -3.4; 486 -3.9; 535 -5.1; 588 -5.9; 647 -6.1; 712 -6.3; 783 -5.4; 861 -5.8; 947 -6.5; 1042 -6.5; 1146 -6.4; 1261 -6.8; 1387 -7.2; 1526 -8.0; 1678 -7.8; 1846 -7.3; 2031 -7.4; 2234 -7.0; 2457 -5.5; 2703 -2.9; 2973 -1.5; 3270 -0.7; 3597 -0.8; 3957 -0.8; 4353 -3.1; 4788 -0.7; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.7; 18182 -8.9; 20000 -8.2
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-W1000X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W1000X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.49 | 8.5 dB  |
| Peaking | 89 Hz    | 0.57 | -5.9 dB |
| Peaking | 446 Hz   | 2.76 | 3.5 dB  |
| Peaking | 3399 Hz  | 2.84 | 5.8 dB  |
| Peaking | 5559 Hz  | 2.51 | 6.2 dB  |
| Peaking | 816 Hz   | 8.35 | 1.3 dB  |
| Peaking | 1852 Hz  | 1.65 | -1.8 dB |
| Peaking | 2792 Hz  | 6.33 | 2.1 dB  |
| Peaking | 8169 Hz  | 5.53 | -1.2 dB |
| Peaking | 18926 Hz | 1.32 | -2.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-8.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 7.9 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -3.2 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 2.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -2.0 dB |
| Peaking | 4000 Hz  | 1.41 | 7.4 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-W1000X/Audio%20Technica%20ATH-W1000X.png)