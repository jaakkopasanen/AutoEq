# Audio Technica ATH-CKM500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.0; 23 -3.6; 25 -4.1; 28 -4.7; 31 -5.2; 34 -5.7; 37 -6.1; 41 -6.6; 45 -7.1; 49 -7.5; 54 -8.0; 60 -8.6; 66 -9.1; 72 -9.5; 79 -10.1; 87 -10.5; 96 -11.0; 106 -11.3; 116 -11.5; 128 -11.8; 141 -12.0; 155 -12.0; 170 -12.0; 187 -11.9; 206 -11.7; 227 -11.3; 249 -11.0; 274 -10.5; 302 -9.9; 332 -9.2; 365 -8.5; 402 -7.7; 442 -6.7; 486 -5.9; 535 -4.9; 588 -3.6; 647 -2.6; 712 -1.7; 783 -0.8; 861 -0.5; 947 -0.5; 1042 -0.5; 1146 -0.7; 1261 -1.5; 1387 -2.4; 1526 -3.4; 1678 -4.1; 1846 -4.5; 2031 -4.9; 2234 -5.6; 2457 -5.7; 2703 -6.1; 2973 -6.3; 3270 -5.6; 3597 -5.0; 3957 -4.9; 4353 -6.8; 4788 -7.9; 5267 -8.5; 5793 -9.7; 6373 -8.0; 7010 -6.3; 7711 -6.2; 8482 -6.5; 9330 -6.6; 10263 -7.7; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-CKM500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-CKM500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.84 | 4.4 dB  |
| Peaking | 97 Hz    | 0.73 | -2.2 dB |
| Peaking | 206 Hz   | 0.56 | -4.9 dB |
| Peaking | 891 Hz   | 0.91 | 7.2 dB  |
| Peaking | 5665 Hz  | 4.6  | -3.6 dB |
| Peaking | 608 Hz   | 4.9  | 0.2 dB  |
| Peaking | 3699 Hz  | 1.55 | -2.1 dB |
| Peaking | 3736 Hz  | 3.57 | 3.6 dB  |
| Peaking | 7321 Hz  | 6.21 | 1.2 dB  |
| Peaking | 10100 Hz | 9.85 | -1.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.5 dB  |
| Peaking | 62 Hz    | 1.41 | -2.1 dB |
| Peaking | 125 Hz   | 1.41 | -4.8 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 1.0 dB  |
| Peaking | 1000 Hz  | 1.41 | 7.0 dB  |
| Peaking | 2000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 4000 Hz  | 1.41 | -0.3 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-CKM500/Audio%20Technica%20ATH-CKM500.png)