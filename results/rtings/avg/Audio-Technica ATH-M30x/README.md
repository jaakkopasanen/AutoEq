# Audio-Technica ATH-M30x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -5.8; 25 -6.3; 28 -7.1; 31 -7.7; 34 -8.2; 37 -8.6; 41 -8.9; 45 -9.1; 49 -9.2; 54 -9.2; 60 -9.1; 66 -9.0; 72 -8.8; 79 -8.6; 87 -8.7; 96 -9.0; 106 -9.3; 116 -9.5; 128 -9.5; 141 -9.1; 155 -8.5; 170 -7.7; 187 -6.6; 206 -5.1; 227 -3.7; 249 -2.8; 274 -2.7; 302 -4.2; 332 -5.3; 365 -6.2; 402 -6.9; 442 -7.3; 486 -7.5; 535 -7.6; 588 -7.6; 647 -7.6; 712 -7.4; 783 -7.2; 861 -7.1; 947 -6.9; 1042 -6.7; 1146 -7.0; 1261 -7.6; 1387 -8.3; 1526 -9.2; 1678 -10.2; 1846 -11.1; 2031 -11.6; 2234 -10.5; 2457 -9.1; 2703 -7.9; 2973 -7.5; 3270 -6.0; 3597 -5.0; 3957 -6.1; 4353 -3.5; 4788 -0.5; 5267 -0.5; 5793 -0.6; 6373 -2.0; 7010 -6.8; 7711 -9.0; 8482 -9.5; 9330 -9.4; 10263 -10.8; 11289 -13.4; 12418 -13.9; 13660 -11.2; 15026 -9.4; 16529 -8.6; 18182 -6.6; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M30x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M30x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-7.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 141 Hz   | 0.32 | -3.5 dB |
| Peaking | 254 Hz   | 1.81 | 7.1 dB  |
| Peaking | 1982 Hz  | 2.18 | -5.2 dB |
| Peaking | 5357 Hz  | 2.23 | 8.2 dB  |
| Peaking | 11804 Hz | 1.06 | -7.2 dB |
| Peaking | 20 Hz    | 1.27 | 2.9 dB  |
| Peaking | 39 Hz    | 0.54 | -1.3 dB |
| Peaking | 80 Hz    | 2.49 | 1.4 dB  |
| Peaking | 7802 Hz  | 3.75 | -4.3 dB |
| Peaking | 7916 Hz  | 1.77 | 2.4 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-4.6dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB |
| Peaking | 62 Hz    | 1.41 | -2.0 dB |
| Peaking | 125 Hz   | 1.41 | -3.6 dB |
| Peaking | 250 Hz   | 1.41 | 4.3 dB  |
| Peaking | 500 Hz   | 1.41 | -2.0 dB |
| Peaking | 1000 Hz  | 1.41 | 0.9 dB  |
| Peaking | 2000 Hz  | 1.41 | -6.1 dB |
| Peaking | 4000 Hz  | 1.41 | 5.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -2.4 dB |
| Peaking | 16000 Hz | 1.41 | -4.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M30x/Audio-Technica%20ATH-M30x.png)