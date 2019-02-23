# Audio Technica ATH-ANC7B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -2.3; 31 -4.8; 34 -7.1; 37 -9.0; 41 -10.9; 45 -12.0; 49 -12.2; 54 -11.6; 60 -10.7; 66 -10.2; 72 -10.0; 79 -9.8; 87 -9.7; 96 -9.6; 106 -9.4; 116 -9.3; 128 -9.2; 141 -9.2; 155 -9.3; 170 -9.0; 187 -8.9; 206 -8.6; 227 -8.4; 249 -8.2; 274 -7.9; 302 -7.7; 332 -7.3; 365 -7.4; 402 -7.3; 442 -7.7; 486 -8.2; 535 -8.9; 588 -9.8; 647 -10.7; 712 -11.0; 783 -10.0; 861 -8.2; 947 -6.8; 1042 -7.3; 1146 -8.9; 1261 -8.0; 1387 -7.2; 1526 -5.7; 1678 -4.7; 1846 -7.2; 2031 -6.1; 2234 -5.1; 2457 -3.6; 2703 -1.7; 2973 -1.8; 3270 -2.0; 3597 -3.3; 3957 -2.7; 4353 -1.9; 4788 -2.3; 5267 -7.4; 5793 -5.3; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.2; 10263 -9.9; 11289 -8.7; 12418 -6.9; 13660 -8.2; 15026 -11.1; 16529 -10.7; 18182 -7.3; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC7B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.66 | 17.2 dB  |
| Peaking | 40 Hz    | 0.61 | -16.1 dB |
| Peaking | 3363 Hz  | 0.75 | 8.1 dB   |
| Peaking | 4394 Hz  | 0.09 | -3.6 dB  |
| Peaking | 6648 Hz  | 5.75 | 5.1 dB   |
| Peaking | 394 Hz   | 2.27 | 1.5 dB   |
| Peaking | 692 Hz   | 2.91 | -2.7 dB  |
| Peaking | 943 Hz   | 6.02 | 2.5 dB   |
| Peaking | 12670 Hz | 4.5  | 3.0 dB   |
| Peaking | 15518 Hz | 2.88 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.2 dB  |
| Peaking | 62 Hz    | 1.41 | -5.2 dB |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.6 dB |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | -2.2 dB |
| Peaking | 2000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.4 dB |
| Peaking | 16000 Hz | 1.41 | -5.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ANC7B/Audio%20Technica%20ATH-ANC7B.png)