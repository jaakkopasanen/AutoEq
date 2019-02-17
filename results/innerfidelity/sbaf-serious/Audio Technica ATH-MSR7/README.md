# Audio Technica ATH-MSR7
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.9; 31 -1.2; 34 -1.6; 37 -1.9; 41 -2.2; 45 -2.5; 49 -2.8; 54 -3.0; 60 -3.3; 66 -3.6; 72 -3.9; 79 -4.2; 87 -4.6; 96 -5.0; 106 -5.2; 116 -5.4; 128 -5.7; 141 -5.8; 155 -6.1; 170 -5.9; 187 -5.6; 206 -5.8; 227 -5.8; 249 -5.8; 274 -5.5; 302 -5.2; 332 -4.7; 365 -4.0; 402 -3.4; 442 -2.9; 486 -2.9; 535 -3.0; 588 -3.0; 647 -3.8; 712 -4.7; 783 -5.1; 861 -5.8; 947 -6.3; 1042 -6.5; 1146 -6.7; 1261 -6.9; 1387 -7.6; 1526 -8.3; 1678 -8.7; 1846 -8.6; 2031 -7.8; 2234 -6.0; 2457 -4.4; 2703 -2.9; 2973 -1.6; 3270 -1.1; 3597 -1.0; 3957 -1.8; 4353 -5.1; 4788 -5.2; 5267 -1.4; 5793 -0.5; 6373 -1.0; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-MSR7 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-MSR7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  0.67 | 5.8 dB  |
| Peaking | 60 Hz   |  1    | 1.5 dB  |
| Peaking | 486 Hz  |  1.7  | 4.0 dB  |
| Peaking | 3344 Hz |  3.08 | 6.1 dB  |
| Peaking | 5928 Hz |  3.84 | 6.4 dB  |
| Peaking | 641 Hz  |  4.69 | 0.8 dB  |
| Peaking | 1768 Hz |  2.06 | -3.1 dB |
| Peaking | 2606 Hz |  3.3  | 2.1 dB  |
| Peaking | 4588 Hz | 12.12 | -1.5 dB |
| Peaking | 8198 Hz |  5.69 | -0.9 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.9dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 2.0 dB  |
| Peaking | 125 Hz   | 1.41 | 0.2 dB  |
| Peaking | 250 Hz   | 1.41 | -0.1 dB |
| Peaking | 500 Hz   | 1.41 | 4.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.8 dB |
| Peaking | 2000 Hz  | 1.41 | -1.8 dB |
| Peaking | 4000 Hz  | 1.41 | 5.8 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.6 dB  |
| Peaking | 16000 Hz | 1.41 | -0.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-MSR7/Audio%20Technica%20ATH-MSR7.png)