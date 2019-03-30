# Audio-Technica ATH-W1000X Grandioso
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.3; 23 -3.2; 25 -4.0; 28 -5.1; 31 -6.2; 34 -7.1; 37 -7.9; 41 -8.7; 45 -9.4; 49 -10.0; 54 -10.7; 60 -11.2; 66 -11.5; 72 -11.7; 79 -11.9; 87 -12.1; 96 -12.1; 106 -12.0; 116 -11.7; 128 -11.4; 141 -11.1; 155 -10.7; 170 -10.4; 187 -10.0; 206 -9.6; 227 -9.2; 249 -8.8; 274 -8.1; 302 -7.2; 332 -6.3; 365 -5.0; 402 -3.1; 442 -1.0; 486 -0.5; 535 -1.9; 588 -3.4; 647 -4.5; 712 -5.0; 783 -5.0; 861 -5.0; 947 -5.5; 1042 -6.1; 1146 -6.3; 1261 -6.3; 1387 -6.3; 1526 -6.4; 1678 -6.6; 1846 -6.6; 2031 -6.0; 2234 -4.0; 2457 -2.3; 2703 -4.0; 2973 -6.6; 3270 -7.4; 3597 -6.4; 3957 -7.0; 4353 -9.5; 4788 -10.4; 5267 -9.4; 5793 -7.5; 6373 -3.6; 7010 -3.5; 7711 -5.7; 8482 -6.0; 9330 -6.0; 10263 -6.0; 11289 -6.0; 12418 -6.0; 13660 -6.0; 15026 -6.0; 16529 -6.0; 18182 -6.0; 20000 -6.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-W1000X Grandioso GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-W1000X Grandioso ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.7dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.03 | 5.4 dB  |
| Peaking | 64 Hz   | 0.62 | -3.4 dB |
| Peaking | 131 Hz  | 0.43 | -3.8 dB |
| Peaking | 472 Hz  | 2.1  | 7.0 dB  |
| Peaking | 4766 Hz | 4.99 | -5.0 dB |
| Peaking | 262 Hz  | 2.85 | -0.1 dB |
| Peaking | 1824 Hz | 2.89 | -0.7 dB |
| Peaking | 2470 Hz | 4.86 | 4.8 dB  |
| Peaking | 3700 Hz | 0.72 | -0.8 dB |
| Peaking | 6683 Hz | 7.24 | 4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.6 dB  |
| Peaking | 62 Hz    | 1.41 | -5.6 dB |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -2.9 dB |
| Peaking | 500 Hz   | 1.41 | 5.7 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.5 dB |
| Peaking | 2000 Hz  | 1.41 | 1.8 dB  |
| Peaking | 4000 Hz  | 1.41 | -2.6 dB |
| Peaking | 8000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 16000 Hz | 1.41 | -0.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/referenceaudioanalyzer/zero/Audio-Technica%20ATH-W1000X%20Grandioso/Audio-Technica%20ATH-W1000X%20Grandioso.png)