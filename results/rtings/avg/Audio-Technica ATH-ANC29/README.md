# Audio-Technica ATH-ANC29
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -5.2; 23 -4.9; 25 -4.6; 28 -4.3; 31 -4.2; 34 -4.1; 37 -4.2; 41 -4.2; 45 -4.3; 49 -4.4; 54 -4.5; 60 -4.7; 66 -4.9; 72 -5.1; 79 -5.3; 87 -5.7; 96 -6.1; 106 -6.4; 116 -6.8; 128 -7.2; 141 -7.5; 155 -7.7; 170 -7.9; 187 -8.0; 206 -8.0; 227 -8.0; 249 -8.0; 274 -8.1; 302 -8.2; 332 -8.3; 365 -8.4; 402 -8.7; 442 -9.0; 486 -9.4; 535 -9.7; 588 -9.9; 647 -10.0; 712 -10.1; 783 -10.0; 861 -8.3; 947 -7.8; 1042 -10.9; 1146 -13.9; 1261 -13.3; 1387 -10.7; 1526 -7.7; 1678 -5.5; 1846 -4.5; 2031 -4.1; 2234 -3.7; 2457 -3.6; 2703 -4.4; 2973 -4.1; 3270 -1.5; 3597 -0.5; 3957 -0.5; 4353 -0.5; 4788 -0.7; 5267 -3.8; 5793 -4.3; 6373 -10.0; 7010 -11.5; 7711 -9.5; 8482 -6.5; 9330 -6.5; 10263 -6.5; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -6.5
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC29 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC29 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.5dB**.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 541 Hz  | 0.7  | -3.1 dB |
| Peaking | 1220 Hz | 3.91 | -7.5 dB |
| Peaking | 1935 Hz | 2.44 | 2.5 dB  |
| Peaking | 4190 Hz | 1.37 | 6.9 dB  |
| Peaking | 6836 Hz | 3.83 | -7.7 dB |
| Peaking | 40 Hz   | 0.55 | 2.4 dB  |
| Peaking | 155 Hz  | 1.55 | -1.3 dB |
| Peaking | 781 Hz  | 3.73 | -2.0 dB |
| Peaking | 916 Hz  | 3.72 | 3.0 dB  |
| Peaking | 1082 Hz | 7.54 | -1.8 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 2.3 dB  |
| Peaking | 62 Hz    | 1.41 | 1.8 dB  |
| Peaking | 125 Hz   | 1.41 | -0.8 dB |
| Peaking | 250 Hz   | 1.41 | -1.2 dB |
| Peaking | 500 Hz   | 1.41 | -1.9 dB |
| Peaking | 1000 Hz  | 1.41 | -5.1 dB |
| Peaking | 2000 Hz  | 1.41 | 1.4 dB  |
| Peaking | 4000 Hz  | 1.41 | 6.6 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.5 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC29/Audio-Technica%20ATH-ANC29.png)