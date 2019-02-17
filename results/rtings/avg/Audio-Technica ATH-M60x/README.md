# Audio-Technica ATH-M60x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -4.8; 23 -4.9; 25 -5.0; 28 -5.2; 31 -5.4; 34 -5.6; 37 -5.6; 41 -5.8; 45 -6.0; 49 -6.1; 54 -6.3; 60 -6.4; 66 -6.6; 72 -6.7; 79 -7.0; 87 -7.2; 96 -7.4; 106 -7.6; 116 -7.8; 128 -8.0; 141 -8.1; 155 -8.2; 170 -8.2; 187 -8.1; 206 -7.8; 227 -7.5; 249 -7.0; 274 -6.5; 302 -5.7; 332 -4.2; 365 -2.0; 402 -0.5; 442 -0.5; 486 -1.3; 535 -3.7; 588 -5.4; 647 -6.2; 712 -6.5; 783 -6.6; 861 -6.5; 947 -6.4; 1042 -6.5; 1146 -6.6; 1261 -6.6; 1387 -6.6; 1526 -6.4; 1678 -6.8; 1846 -7.0; 2031 -6.6; 2234 -5.2; 2457 -3.6; 2703 -3.4; 2973 -3.1; 3270 -3.2; 3597 -3.7; 3957 -7.4; 4353 -9.2; 4788 -6.4; 5267 -4.2; 5793 -3.5; 6373 -5.9; 7010 -8.9; 7711 -7.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -9.1; 15026 -13.0; 16529 -12.6; 18182 -11.1; 20000 -13.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M60x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M60x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.98 | 1.7 dB  |
| Peaking | 428 Hz   | 3.3  | 7.0 dB  |
| Peaking | 2938 Hz  | 2.85 | 4.1 dB  |
| Peaking | 11783 Hz | 1.2  | 4.6 dB  |
| Peaking | 16448 Hz | 0.48 | -7.3 dB |
| Peaking | 157 Hz   | 1.27 | -2.0 dB |
| Peaking | 4306 Hz  | 6.78 | -4.7 dB |
| Peaking | 5801 Hz  | 2.4  | 4.6 dB  |
| Peaking | 7015 Hz  | 3.89 | -4.3 dB |
| Peaking | 8348 Hz  | 5.43 | 0.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.4 dB  |
| Peaking | 62 Hz    | 1.41 | 0.1 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -0.8 dB |
| Peaking | 500 Hz   | 1.41 | 5.2 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.3 dB  |
| Peaking | 4000 Hz  | 1.41 | 1.2 dB  |
| Peaking | 8000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 16000 Hz | 1.41 | -7.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M60x/Audio-Technica%20ATH-M60x.png)