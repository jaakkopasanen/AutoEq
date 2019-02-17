# Audio-Technica ATH-M70x
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.7; 23 -1.0; 25 -1.2; 28 -1.5; 31 -1.6; 34 -1.6; 37 -1.4; 41 -1.3; 45 -1.2; 49 -1.2; 54 -1.3; 60 -1.6; 66 -2.1; 72 -2.6; 79 -3.0; 87 -3.5; 96 -3.8; 106 -4.1; 116 -4.2; 128 -4.3; 141 -4.1; 155 -4.0; 170 -3.8; 187 -3.8; 206 -3.7; 227 -4.0; 249 -4.3; 274 -4.5; 302 -4.2; 332 -4.6; 365 -4.5; 402 -3.9; 442 -3.3; 486 -3.0; 535 -2.7; 588 -1.3; 647 -0.5; 712 -0.6; 783 -1.1; 861 -1.6; 947 -1.9; 1042 -2.3; 1146 -2.5; 1261 -2.8; 1387 -3.2; 1526 -3.8; 1678 -4.7; 1846 -5.8; 2031 -6.9; 2234 -6.9; 2457 -6.5; 2703 -6.0; 2973 -6.4; 3270 -8.1; 3597 -8.6; 3957 -8.3; 4353 -10.9; 4788 -10.9; 5267 -8.7; 5793 -5.8; 6373 -4.6; 7010 -5.3; 7711 -7.8; 8482 -10.0; 9330 -9.8; 10263 -8.5; 11289 -7.0; 12418 -4.6; 13660 -2.6; 15026 -3.0; 16529 -5.0; 18182 -6.7; 20000 -5.9
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-M70x GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-M70x ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.0dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 192 Hz   | 0.72 | -2.3 dB |
| Peaking | 2206 Hz  | 2.01 | -4.1 dB |
| Peaking | 4409 Hz  | 2.07 | -8.1 dB |
| Peaking | 9282 Hz  | 2.09 | -7.7 dB |
| Peaking | 18867 Hz | 1    | -5.1 dB |
| Peaking | 21 Hz    | 1.51 | 1.5 dB  |
| Peaking | 48 Hz    | 2.85 | 1.1 dB  |
| Peaking | 367 Hz   | 2.68 | -1.4 dB |
| Peaking | 690 Hz   | 2.56 | 2.3 dB  |
| Peaking | 6333 Hz  | 7.54 | 1.7 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 1.1 dB  |
| Peaking | 62 Hz    | 1.41 | 0.3 dB  |
| Peaking | 125 Hz   | 1.41 | -1.9 dB |
| Peaking | 250 Hz   | 1.41 | -2.1 dB |
| Peaking | 500 Hz   | 1.41 | -0.2 dB |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -3.1 dB |
| Peaking | 4000 Hz  | 1.41 | -6.0 dB |
| Peaking | 8000 Hz  | 1.41 | -5.7 dB |
| Peaking | 16000 Hz | 1.41 | -2.7 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-M70x/Audio-Technica%20ATH-M70x.png)