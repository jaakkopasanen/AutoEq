# Audio Technica ATH-ANC7B
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.7; 28 -2.1; 31 -4.6; 34 -6.9; 37 -8.8; 41 -10.7; 45 -11.8; 49 -12.0; 54 -11.4; 60 -10.5; 66 -10.0; 72 -9.7; 79 -9.6; 87 -9.5; 96 -9.4; 106 -9.2; 116 -9.1; 128 -9.0; 141 -9.0; 155 -9.1; 170 -8.8; 187 -8.7; 206 -8.4; 227 -8.2; 249 -7.9; 274 -7.7; 302 -7.5; 332 -7.1; 365 -7.2; 402 -7.1; 442 -7.5; 486 -8.0; 535 -8.7; 588 -9.6; 647 -10.5; 712 -10.7; 783 -9.8; 861 -8.0; 947 -6.6; 1042 -7.1; 1146 -8.7; 1261 -7.8; 1387 -7.0; 1526 -5.5; 1678 -4.5; 1846 -7.0; 2031 -5.9; 2234 -4.9; 2457 -3.4; 2703 -1.5; 2973 -1.6; 3270 -1.8; 3597 -3.1; 3957 -2.5; 4353 -1.7; 4788 -2.1; 5267 -7.2; 5793 -5.1; 6373 -1.8; 7010 -4.0; 7711 -6.2; 8482 -6.5; 9330 -8.0; 10263 -9.7; 11289 -8.5; 12418 -6.7; 13660 -8.0; 15026 -10.9; 16529 -10.5; 18182 -7.1; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-ANC7B GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ANC7B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.0dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.66 | 17.0 dB  |
| Peaking | 39 Hz    | 0.63 | -15.8 dB |
| Peaking | 3341 Hz  | 0.75 | 8.1 dB   |
| Peaking | 4492 Hz  | 0.09 | -3.4 dB  |
| Peaking | 6619 Hz  | 6.23 | 5.0 dB   |
| Peaking | 678 Hz   | 1    | 2.8 dB   |
| Peaking | 684 Hz   | 2.5  | -5.4 dB  |
| Peaking | 2016 Hz  | 6.31 | -1.6 dB  |
| Peaking | 12839 Hz | 4.47 | 3.0 dB   |
| Peaking | 15690 Hz | 2.92 | -2.8 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.4 dB  |
| Peaking | 62 Hz    | 1.41 | -5.0 dB |
| Peaking | 125 Hz   | 1.41 | -1.7 dB |
| Peaking | 250 Hz   | 1.41 | -0.5 dB |
| Peaking | 500 Hz   | 1.41 | -1.8 dB |
| Peaking | 1000 Hz  | 1.41 | -2.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 4.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -0.3 dB |
| Peaking | 16000 Hz | 1.41 | -4.8 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ANC7B/Audio%20Technica%20ATH-ANC7B.png)