# Audio-Technica ATH-M50xBT
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -8.4; 23 -8.7; 25 -9.0; 28 -9.4; 31 -9.8; 34 -10.0; 37 -10.1; 41 -10.1; 45 -9.9; 49 -9.6; 54 -8.9; 60 -8.5; 66 -8.8; 72 -9.3; 79 -9.9; 87 -10.6; 96 -11.1; 106 -11.4; 116 -11.5; 128 -11.5; 141 -11.4; 155 -11.2; 170 -10.9; 187 -10.3; 206 -9.4; 227 -8.4; 249 -7.4; 274 -6.1; 302 -3.5; 332 -2.4; 365 -1.5; 402 -1.3; 442 -1.2; 486 -1.5; 535 -2.2; 588 -2.8; 647 -3.4; 712 -3.9; 783 -3.9; 861 -3.9; 947 -5.0; 1042 -5.8; 1146 -6.3; 1261 -7.0; 1387 -7.6; 1526 -8.2; 1678 -8.7; 1846 -8.5; 2031 -8.4; 2234 -8.3; 2457 -7.8; 2703 -8.4; 2973 -8.7; 3270 -7.9; 3597 -6.3; 3957 -7.3; 4353 -10.3; 4788 -7.5; 5267 -3.7; 5793 -0.5; 6373 -1.7; 7010 -4.0; 7711 -6.6; 8482 -8.4; 9330 -9.2; 10263 -10.2; 11289 -11.7; 12418 -11.0; 13660 -8.9; 15026 -8.9; 16529 -8.8; 18182 -7.2; 20000 -8.0
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M50xBT GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M50xBT ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.4dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.14 | -3.7 dB |
| Peaking | 165 Hz   | 0.54 | -7.9 dB |
| Peaking | 387 Hz   | 0.86 | 8.3 dB  |
| Peaking | 6103 Hz  | 2.32 | 10.8 dB |
| Peaking | 7611 Hz  | 0.22 | -5.6 dB |
| Peaking | 853 Hz   | 6.82 | 1.2 dB  |
| Peaking | 1595 Hz  | 3.11 | -1.2 dB |
| Peaking | 3902 Hz  | 2.72 | 3.7 dB  |
| Peaking | 4377 Hz  | 5.91 | -5.6 dB |
| Peaking | 11584 Hz | 6.04 | -2.0 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.5 dB |
| Peaking | 62 Hz    | 1.41 | -1.6 dB |
| Peaking | 125 Hz   | 1.41 | -6.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.0 dB |
| Peaking | 500 Hz   | 1.41 | 5.4 dB  |
| Peaking | 1000 Hz  | 1.41 | -0.4 dB |
| Peaking | 2000 Hz  | 1.41 | -3.6 dB |
| Peaking | 4000 Hz  | 1.41 | -0.6 dB |
| Peaking | 8000 Hz  | 1.41 | -0.7 dB |
| Peaking | 16000 Hz | 1.41 | -5.6 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M50xBT/Audio-Technica%20ATH-M50xBT.png)