# Audio-Technica ATH-M40x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -1.0; 23 -1.7; 25 -2.3; 28 -3.1; 31 -3.7; 34 -4.2; 37 -4.6; 41 -5.0; 45 -5.3; 49 -5.5; 54 -5.6; 60 -5.7; 66 -5.8; 72 -5.7; 79 -5.4; 87 -5.6; 96 -6.4; 106 -7.3; 116 -8.0; 128 -8.1; 141 -7.8; 155 -7.4; 170 -7.2; 187 -6.5; 206 -5.5; 227 -4.3; 249 -3.2; 274 -2.2; 302 -1.4; 332 -0.5; 365 -0.6; 402 -1.2; 442 -1.2; 486 -1.3; 535 -1.6; 588 -1.8; 647 -1.8; 712 -1.8; 783 -1.8; 861 -1.7; 947 -2.0; 1042 -2.7; 1146 -3.4; 1261 -3.9; 1387 -4.1; 1526 -4.3; 1678 -4.6; 1846 -4.6; 2031 -4.5; 2234 -3.7; 2457 -2.6; 2703 -2.2; 2973 -2.7; 3270 -3.5; 3597 -3.6; 3957 -3.8; 4353 -4.9; 4788 -3.4; 5267 -2.0; 5793 -0.6; 6373 -1.3; 7010 -3.3; 7711 -6.1; 8482 -8.0; 9330 -8.7; 10263 -8.1; 11289 -6.5; 12418 -5.3; 13660 -7.7; 15026 -11.8; 16529 -11.1; 18182 -7.6; 20000 -7.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M40x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M40x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.1dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 1.1  | -2.9 dB |
| Peaking | 135 Hz   | 1.64 | -5.7 dB |
| Peaking | 1724 Hz  | 2.33 | -2.4 dB |
| Peaking | 9209 Hz  | 3.19 | -5.5 dB |
| Peaking | 16226 Hz | 0.97 | -9.5 dB |
| Peaking | 199 Hz   | 3.21 | -1.9 dB |
| Peaking | 350 Hz   | 1.51 | 2.4 dB  |
| Peaking | 810 Hz   | 4.06 | 0.8 dB  |
| Peaking | 4367 Hz  | 4.66 | -2.2 dB |
| Peaking | 6008 Hz  | 4.89 | 3.3 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-2.1dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -0.9 dB  |
| Peaking | 62 Hz    | 1.41 | -2.0 dB  |
| Peaking | 125 Hz   | 1.41 | -5.9 dB  |
| Peaking | 250 Hz   | 1.41 | -0.0 dB  |
| Peaking | 500 Hz   | 1.41 | 2.0 dB   |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.9 dB  |
| Peaking | 4000 Hz  | 1.41 | 0.6 dB   |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB  |
| Peaking | 16000 Hz | 1.41 | -11.3 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M40x/Audio-Technica%20ATH-M40x.png)