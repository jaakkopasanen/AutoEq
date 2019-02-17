# Audio-Technica ATH-AD700X
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.5; 34 -0.5; 37 -0.5; 41 -0.5; 45 -0.5; 49 -0.5; 54 -0.5; 60 -0.9; 66 -1.6; 72 -2.1; 79 -2.7; 87 -3.2; 96 -3.8; 106 -4.5; 116 -4.9; 128 -5.4; 141 -5.7; 155 -5.9; 170 -6.1; 187 -6.3; 206 -6.2; 227 -6.1; 249 -6.0; 274 -5.9; 302 -5.9; 332 -6.1; 365 -6.2; 402 -6.3; 442 -6.5; 486 -6.6; 535 -6.6; 588 -6.3; 647 -6.2; 712 -6.2; 783 -6.3; 861 -6.2; 947 -6.4; 1042 -6.6; 1146 -6.8; 1261 -7.1; 1387 -7.4; 1526 -7.5; 1678 -7.3; 1846 -6.7; 2031 -5.7; 2234 -3.2; 2457 -0.6; 2703 -0.5; 2973 -0.5; 3270 -0.5; 3597 -2.5; 3957 -7.0; 4353 -5.8; 4788 -0.6; 5267 -0.7; 5793 -4.7; 6373 -1.4; 7010 -4.0; 7711 -6.2; 8482 -6.8; 9330 -10.9; 10263 -11.2; 11289 -8.1; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -7.4; 18182 -10.1; 20000 -12.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-AD700X GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-AD700X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.9dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.55 | 6.7 dB  |
| Peaking | 1685 Hz | 1.88 | -2.3 dB |
| Peaking | 2723 Hz | 2.18 | 6.9 dB  |
| Peaking | 5830 Hz | 1.77 | 4.3 dB  |
| Peaking | 9811 Hz | 3.34 | -6.2 dB |
| Peaking | 65 Hz   | 2.67 | 0.7 dB  |
| Peaking | 154 Hz  | 2.06 | -0.7 dB |
| Peaking | 3472 Hz | 6.37 | 3.2 dB  |
| Peaking | 4156 Hz | 4.27 | -5.3 dB |
| Peaking | 4826 Hz | 6.98 | 4.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.4 dB  |
| Peaking | 62 Hz    | 1.41 | 4.5 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | 0.1 dB  |
| Peaking | 500 Hz   | 1.41 | 0.3 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 5.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.0 dB |
| Peaking | 16000 Hz | 1.41 | -1.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-AD700X/Audio-Technica%20ATH-AD700X.png)