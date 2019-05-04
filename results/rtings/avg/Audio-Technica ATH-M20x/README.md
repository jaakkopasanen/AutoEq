# Audio-Technica ATH-M20x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.8; 25 -1.3; 28 -2.3; 31 -3.3; 34 -4.2; 37 -5.0; 41 -5.8; 45 -6.6; 49 -7.2; 54 -7.9; 60 -8.6; 66 -9.0; 72 -9.2; 79 -9.3; 87 -9.2; 96 -9.2; 106 -9.3; 116 -9.5; 128 -9.4; 141 -8.9; 155 -8.1; 170 -7.1; 187 -5.8; 206 -4.4; 227 -3.2; 249 -3.0; 274 -4.1; 302 -5.5; 332 -6.1; 365 -6.6; 402 -7.2; 442 -7.7; 486 -7.9; 535 -8.0; 588 -8.0; 647 -7.9; 712 -7.6; 783 -7.3; 861 -7.1; 947 -7.0; 1042 -6.8; 1146 -7.0; 1261 -7.5; 1387 -8.1; 1526 -8.9; 1678 -9.6; 1846 -10.5; 2031 -11.2; 2234 -11.0; 2457 -9.7; 2703 -8.1; 2973 -7.2; 3270 -6.3; 3597 -3.3; 3957 -1.7; 4353 -3.0; 4788 -2.6; 5267 -0.5; 5793 -0.5; 6373 -1.2; 7010 -6.7; 7711 -10.2; 8482 -8.9; 9330 -6.5; 10263 -6.5; 11289 -8.2; 12418 -8.8; 13660 -7.0; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M20x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M20x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.2dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 2.86 | 6.5 dB  |
| Peaking | 242 Hz   | 5.06 | 4.2 dB  |
| Peaking | 2090 Hz  | 1.39 | -4.7 dB |
| Peaking | 3905 Hz  | 3.34 | 5.3 dB  |
| Peaking | 5611 Hz  | 4.25 | 6.8 dB  |
| Peaking | 30 Hz    | 2.3  | 2.0 dB  |
| Peaking | 89 Hz    | 1.06 | -3.4 dB |
| Peaking | 547 Hz   | 2.97 | -1.5 dB |
| Peaking | 7888 Hz  | 6.37 | -5.0 dB |
| Peaking | 20713 Hz | 2.01 | -0.5 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.4dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 4.7 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB |
| Peaking | 125 Hz   | 1.41 | -3.4 dB |
| Peaking | 250 Hz   | 1.41 | 4.1 dB  |
| Peaking | 500 Hz   | 1.41 | -2.5 dB |
| Peaking | 1000 Hz  | 1.41 | 1.1 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.2 dB |
| Peaking | 4000 Hz  | 1.41 | 6.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.3 dB |
| Peaking | 16000 Hz | 1.41 | -0.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M20x/Audio-Technica%20ATH-M20x.png)