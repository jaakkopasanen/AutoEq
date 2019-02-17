# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -7.9; 25 -8.3; 28 -8.7; 31 -9.1; 34 -9.3; 37 -9.5; 41 -9.6; 45 -9.7; 49 -9.6; 54 -9.5; 60 -9.4; 66 -9.1; 72 -8.2; 79 -7.0; 87 -6.2; 96 -6.4; 106 -8.0; 116 -8.6; 128 -9.6; 141 -10.5; 155 -9.9; 170 -8.4; 187 -9.4; 206 -8.4; 227 -7.1; 249 -6.0; 274 -4.8; 302 -4.1; 332 -4.2; 365 -4.5; 402 -4.9; 442 -5.3; 486 -5.9; 535 -6.4; 588 -6.3; 647 -6.6; 712 -6.9; 783 -6.8; 861 -6.9; 947 -6.5; 1042 -6.4; 1146 -6.1; 1261 -6.6; 1387 -7.5; 1526 -8.4; 1678 -9.3; 1846 -9.6; 2031 -9.2; 2234 -8.6; 2457 -7.1; 2703 -5.9; 2973 -4.0; 3270 -3.0; 3597 -2.5; 3957 -4.3; 4353 -6.6; 4788 -3.8; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-M50x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-M50x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 1.24 | -3.5 dB |
| Peaking | 144 Hz   | 3.15 | -4.0 dB |
| Peaking | 1884 Hz  | 2.56 | -3.7 dB |
| Peaking | 3350 Hz  | 3.93 | 4.1 dB  |
| Peaking | 5780 Hz  | 3.27 | 6.8 dB  |
| Peaking | 89 Hz    | 7.46 | 1.6 dB  |
| Peaking | 198 Hz   | 4.64 | -2.2 dB |
| Peaking | 321 Hz   | 2.11 | 2.8 dB  |
| Peaking | 1172 Hz  | 7.87 | 0.9 dB  |
| Peaking | 22050 Hz | 1.78 | 0.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.1 dB |
| Peaking | 62 Hz    | 1.41 | -0.7 dB |
| Peaking | 125 Hz   | 1.41 | -2.9 dB |
| Peaking | 250 Hz   | 1.41 | 0.9 dB  |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.4 dB |
| Peaking | 4000 Hz  | 1.41 | 4.5 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)