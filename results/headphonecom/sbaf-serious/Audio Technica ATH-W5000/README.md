# Audio Technica ATH-W5000
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.5; 66 -0.5; 72 -0.6; 79 -1.5; 87 -2.2; 96 -2.9; 106 -3.3; 116 -3.7; 128 -4.0; 141 -4.2; 155 -4.4; 170 -4.3; 187 -4.3; 206 -4.3; 227 -4.3; 249 -4.6; 274 -5.1; 302 -5.1; 332 -5.0; 365 -4.8; 402 -2.5; 442 -3.0; 486 -3.6; 535 -4.1; 588 -5.2; 647 -7.5; 712 -8.9; 783 -9.3; 861 -9.9; 947 -10.4; 1042 -10.9; 1146 -11.4; 1261 -12.2; 1387 -13.0; 1526 -13.5; 1678 -12.8; 1846 -12.5; 2031 -12.4; 2234 -10.8; 2457 -8.5; 2703 -5.5; 2973 -3.0; 3270 -0.9; 3597 -3.8; 3957 -10.0; 4353 -8.4; 4788 -4.9; 5267 -2.2; 5793 -3.9; 6373 -7.1; 7010 -4.1; 7711 -6.2; 8482 -7.7; 9330 -14.3; 10263 -11.5; 11289 -6.6; 12418 -6.5; 13660 -8.1; 15026 -12.3; 16529 -15.8; 18182 -18.3; 20000 -18.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio Technica ATH-W5000 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-W5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.45 | 6.5 dB   |
| Peaking | 1434 Hz  | 0.77 | -12.1 dB |
| Peaking | 3111 Hz  | 0.09 | 5.1 dB   |
| Peaking | 9493 Hz  | 4.52 | -10.5 dB |
| Peaking | 18686 Hz | 0.5  | -14.7 dB |
| Peaking | 440 Hz   | 5.08 | 2.5 dB   |
| Peaking | 2136 Hz  | 3.81 | -2.9 dB  |
| Peaking | 3335 Hz  | 2.64 | 7.3 dB   |
| Peaking | 3979 Hz  | 4.94 | -9.6 dB  |
| Peaking | 12661 Hz | 4.19 | 2.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB   |
| Peaking | 62 Hz    | 1.41 | 5.0 dB   |
| Peaking | 125 Hz   | 1.41 | 1.5 dB   |
| Peaking | 250 Hz   | 1.41 | 0.9 dB   |
| Peaking | 500 Hz   | 1.41 | 3.7 dB   |
| Peaking | 1000 Hz  | 1.41 | -5.5 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB  |
| Peaking | 4000 Hz  | 1.41 | 3.8 dB   |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB  |
| Peaking | 16000 Hz | 1.41 | -10.4 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-W5000/Audio%20Technica%20ATH-W5000.png)