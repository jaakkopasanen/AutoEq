# Audio Technica ATH-M50x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.0; 23 -8.4; 25 -8.8; 28 -9.3; 31 -9.6; 34 -9.9; 37 -10.0; 41 -10.2; 45 -10.2; 49 -10.2; 54 -10.0; 60 -9.9; 66 -9.6; 72 -8.8; 79 -7.5; 87 -6.7; 96 -6.9; 106 -8.5; 116 -9.2; 128 -10.1; 141 -11.0; 155 -10.4; 170 -8.9; 187 -10.0; 206 -8.9; 227 -7.7; 249 -6.5; 274 -5.4; 302 -4.7; 332 -4.7; 365 -5.1; 402 -5.5; 442 -5.8; 486 -6.5; 535 -6.9; 588 -6.9; 647 -7.2; 712 -7.4; 783 -7.4; 861 -7.4; 947 -7.1; 1042 -6.9; 1146 -6.6; 1261 -7.1; 1387 -8.0; 1526 -9.0; 1678 -9.8; 1846 -10.2; 2031 -9.7; 2234 -9.1; 2457 -7.6; 2703 -6.5; 2973 -4.6; 3270 -3.6; 3597 -3.0; 3957 -4.9; 4353 -7.1; 4788 -4.4; 5267 -0.5; 5793 -0.5; 6373 -1.0; 7010 -3.9; 7711 -6.2; 8482 -6.4; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
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

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 1.07 | -4.1 dB |
| Peaking | 147 Hz  | 2.54 | -4.3 dB |
| Peaking | 1875 Hz | 1.97 | -4.0 dB |
| Peaking | 3331 Hz | 4.15 | 3.8 dB  |
| Peaking | 5808 Hz | 3.4  | 6.9 dB  |
| Peaking | 90 Hz   | 7.69 | 1.7 dB  |
| Peaking | 201 Hz  | 4.67 | -2.1 dB |
| Peaking | 319 Hz  | 2.12 | 2.4 dB  |
| Peaking | 700 Hz  | 2.68 | -0.9 dB |
| Peaking | 8242 Hz | 4.96 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.7 dB |
| Peaking | 62 Hz    | 1.41 | -1.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 0.5 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.3 dB |
| Peaking | 2000 Hz  | 1.41 | -3.9 dB |
| Peaking | 4000 Hz  | 1.41 | 4.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-M50x/Audio%20Technica%20ATH-M50x.png)