# Audio-Technica ATH-M20x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.4; 28 -2.5; 31 -3.6; 34 -4.4; 37 -5.2; 41 -6.0; 45 -6.7; 49 -7.3; 54 -8.0; 60 -8.8; 66 -9.2; 72 -9.5; 79 -9.5; 87 -9.4; 96 -9.4; 106 -9.6; 116 -9.7; 128 -9.7; 141 -9.1; 155 -8.3; 170 -7.3; 187 -6.1; 206 -4.6; 227 -3.3; 249 -3.1; 274 -4.2; 302 -5.5; 332 -6.2; 365 -6.7; 402 -7.3; 442 -7.7; 486 -7.9; 535 -7.9; 588 -7.9; 647 -7.8; 712 -7.5; 783 -7.2; 861 -7.0; 947 -6.9; 1042 -6.7; 1146 -6.9; 1261 -7.4; 1387 -8.0; 1526 -8.6; 1678 -9.3; 1846 -10.2; 2031 -10.7; 2234 -10.1; 2457 -8.7; 2703 -7.6; 2973 -7.1; 3270 -6.4; 3597 -3.6; 3957 -1.9; 4353 -3.4; 4788 -2.2; 5267 -0.5; 5793 -0.5; 6373 -1.4; 7010 -6.4; 7711 -9.3; 8482 -9.3; 9330 -6.9; 10263 -6.5; 11289 -7.0; 12418 -8.5; 13660 -7.8; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M20x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M20x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 0.81 | 7.2 dB  |
| Peaking | 122 Hz   | 0.29 | -4.6 dB |
| Peaking | 237 Hz   | 1.65 | 7.3 dB  |
| Peaking | 2020 Hz  | 2.42 | -4.6 dB |
| Peaking | 5142 Hz  | 2.34 | 6.5 dB  |
| Peaking | 3849 Hz  | 6.79 | 5.3 dB  |
| Peaking | 4220 Hz  | 1.77 | -1.8 dB |
| Peaking | 6141 Hz  | 5.29 | 4.0 dB  |
| Peaking | 7846 Hz  | 3.7  | -4.5 dB |
| Peaking | 12819 Hz | 4.31 | -2.3 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.6 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 4.0 dB  |
| Peaking | 500 Hz   | 1.41 | -2.4 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.5 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.1 dB |
| Peaking | 16000 Hz | 1.41 | -0.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M20x/Audio-Technica%20ATH-M20x.png)