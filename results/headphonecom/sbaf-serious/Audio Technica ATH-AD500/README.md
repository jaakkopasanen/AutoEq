# Audio Technica ATH-AD500
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.5; 79 -1.4; 87 -2.4; 96 -3.0; 106 -3.8; 116 -4.2; 128 -4.6; 141 -4.8; 155 -5.0; 170 -5.1; 187 -5.2; 206 -5.2; 227 -5.1; 249 -5.4; 274 -5.4; 302 -5.2; 332 -5.3; 365 -4.9; 402 -4.7; 442 -4.9; 486 -5.0; 535 -5.0; 588 -4.9; 647 -5.0; 712 -4.9; 783 -5.3; 861 -5.7; 947 -6.2; 1042 -6.8; 1146 -7.0; 1261 -7.3; 1387 -7.5; 1526 -7.2; 1678 -5.6; 1846 -4.5; 2031 -4.3; 2234 -4.6; 2457 -5.1; 2703 -5.1; 2973 -4.0; 3270 -3.7; 3597 -3.8; 3957 -10.0; 4353 -10.7; 4788 -9.5; 5267 -8.5; 5793 -0.8; 6373 -2.2; 7010 -7.6; 7711 -10.9; 8482 -13.7; 9330 -14.5; 10263 -12.2; 11289 -8.7; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-AD500 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 36 Hz    | 0.36 | 6.4 dB   |
| Peaking | 3635 Hz  | 1.59 | 10.3 dB  |
| Peaking | 4146 Hz  | 2.02 | -12.7 dB |
| Peaking | 6027 Hz  | 5.16 | 9.2 dB   |
| Peaking | 9027 Hz  | 2.45 | -8.9 dB  |
| Peaking | 34 Hz    | 2.62 | -0.3 dB  |
| Peaking | 617 Hz   | 0.99 | 1.8 dB   |
| Peaking | 1527 Hz  | 1.2  | -2.8 dB  |
| Peaking | 1885 Hz  | 2.79 | 3.6 dB   |
| Peaking | 12504 Hz | 4.93 | 1.6 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.0 dB  |
| Peaking | 62 Hz    | 1.41 | 5.3 dB  |
| Peaking | 125 Hz   | 1.41 | 0.8 dB  |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 8000 Hz  | 1.41 | -4.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-AD500/Audio%20Technica%20ATH-AD500.png)