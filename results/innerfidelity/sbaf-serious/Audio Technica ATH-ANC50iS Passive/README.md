# Audio Technica ATH-ANC50iS Passive
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -7.4; 23 -8.2; 25 -8.9; 28 -9.7; 31 -10.4; 34 -11.0; 37 -11.3; 41 -11.7; 45 -12.0; 49 -12.3; 54 -12.5; 60 -12.6; 66 -12.7; 72 -12.7; 79 -12.7; 87 -13.3; 96 -13.8; 106 -14.1; 116 -14.1; 128 -14.4; 141 -14.7; 155 -14.9; 170 -14.9; 187 -15.3; 206 -15.4; 227 -15.4; 249 -15.3; 274 -15.1; 302 -14.2; 332 -13.6; 365 -13.6; 402 -13.4; 442 -13.5; 486 -13.1; 535 -11.4; 588 -8.9; 647 -6.7; 712 -5.5; 783 -4.6; 861 -5.6; 947 -6.8; 1042 -5.6; 1146 -3.9; 1261 -2.4; 1387 -1.2; 1526 -0.5; 1678 -0.5; 1846 -0.5; 2031 -0.5; 2234 -0.5; 2457 -0.5; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.5; 5267 -0.5; 5793 -0.5; 6373 -1.1; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC50iS Passive GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC50iS Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.8dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.36 | -6.1 dB |
| Peaking | 248 Hz  | 0.88 | -5.7 dB |
| Peaking | 462 Hz  | 3.11 | -4.3 dB |
| Peaking | 2088 Hz | 0.65 | 6.4 dB  |
| Peaking | 5174 Hz | 1.88 | 4.5 dB  |
| Peaking | 18 Hz   | 2.47 | 1.4 dB  |
| Peaking | 769 Hz  | 3.52 | 2.1 dB  |
| Peaking | 953 Hz  | 5.41 | -3.0 dB |
| Peaking | 6424 Hz | 5.04 | 2.9 dB  |
| Peaking | 7804 Hz | 1.84 | -2.1 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.8dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -3.2 dB |
| Peaking | 62 Hz    | 1.41 | -4.7 dB |
| Peaking | 125 Hz   | 1.41 | -6.0 dB |
| Peaking | 250 Hz   | 1.41 | -7.8 dB |
| Peaking | 500 Hz   | 1.41 | -4.2 dB |
| Peaking | 1000 Hz  | 1.41 | 2.4 dB  |
| Peaking | 2000 Hz  | 1.41 | 5.5 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-ANC50iS%20Passive/Audio%20Technica%20ATH-ANC50iS%20Passive.png)