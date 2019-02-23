# Audio Technica ATH-ANC50iS Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.1; 23 -8.8; 25 -9.5; 28 -10.4; 31 -11.1; 34 -11.6; 37 -12.0; 41 -12.4; 45 -12.7; 49 -13.0; 54 -13.1; 60 -13.3; 66 -13.4; 72 -13.3; 79 -13.4; 87 -13.9; 96 -14.5; 106 -14.8; 116 -14.8; 128 -15.1; 141 -15.3; 155 -15.5; 170 -15.5; 187 -15.9; 206 -16.0; 227 -16.1; 249 -16.0; 274 -15.8; 302 -14.9; 332 -14.2; 365 -14.3; 402 -14.1; 442 -14.1; 486 -13.7; 535 -12.0; 588 -9.6; 647 -7.4; 712 -6.2; 783 -5.3; 861 -6.3; 947 -7.4; 1042 -6.3; 1146 -4.6; 1261 -3.0; 1387 -1.9; 1526 -0.8; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.6; 3957 -0.6; 4353 -0.9; 4788 -0.6; 5267 -0.5; 5793 -0.5; 6373 -1.9; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC50iS Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC50iS Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 77 Hz   | 0.35 | -6.3 dB |
| Peaking | 248 Hz  | 0.78 | -6.4 dB |
| Peaking | 465 Hz  | 2.85 | -4.3 dB |
| Peaking | 2709 Hz | 0.5  | 6.9 dB  |
| Peaking | 782 Hz  | 3.38 | 2.8 dB  |
| Peaking | 940 Hz  | 3.25 | -3.5 dB |
| Peaking | 1517 Hz | 3.24 | 1.7 dB  |
| Peaking | 5878 Hz | 1.77 | 7.1 dB  |
| Peaking | 6552 Hz | 0.89 | -5.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.8 dB |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -6.5 dB |
| Peaking | 250 Hz   | 1.41 | -8.3 dB |
| Peaking | 500 Hz   | 1.41 | -4.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.7 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.1 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC50iS%20Passive/Audio%20Technica%20ATH-ANC50iS%20Passive.png)