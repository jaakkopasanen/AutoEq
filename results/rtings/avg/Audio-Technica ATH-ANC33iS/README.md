# Audio-Technica ATH-ANC33iS
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -0.5; 23 -0.5; 25 -0.5; 28 -0.5; 31 -0.7; 34 -1.2; 37 -1.7; 41 -2.3; 45 -2.9; 49 -3.5; 54 -4.2; 60 -5.1; 66 -5.9; 72 -6.6; 79 -7.4; 87 -8.3; 96 -9.2; 106 -10.2; 116 -11.2; 128 -12.1; 141 -13.0; 155 -13.7; 170 -14.3; 187 -14.8; 206 -15.1; 227 -15.3; 249 -15.4; 274 -15.5; 302 -15.7; 332 -15.7; 365 -15.6; 402 -15.4; 442 -14.9; 486 -14.4; 535 -13.5; 588 -12.5; 647 -10.9; 712 -9.6; 783 -7.8; 861 -7.2; 947 -6.9; 1042 -6.1; 1146 -5.5; 1261 -6.6; 1387 -9.5; 1526 -12.0; 1678 -12.2; 1846 -10.9; 2031 -9.1; 2234 -6.8; 2457 -5.0; 2703 -4.5; 2973 -5.5; 3270 -7.3; 3597 -9.0; 3957 -10.1; 4353 -11.2; 4788 -12.1; 5267 -13.6; 5793 -12.7; 6373 -11.7; 7010 -9.1; 7711 -7.7; 8482 -8.8; 9330 -9.7; 10263 -7.1; 11289 -6.5; 12418 -6.5; 13660 -6.5; 15026 -6.5; 16529 -6.5; 18182 -6.5; 20000 -10.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC33iS GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC33iS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-6.3dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.67 | 6.7 dB   |
| Peaking | 256 Hz   | 0.57 | -10.1 dB |
| Peaking | 1645 Hz  | 5.69 | -5.6 dB  |
| Peaking | 5412 Hz  | 2.1  | -7.3 dB  |
| Peaking | 20001 Hz | 2.69 | -3.9 dB  |
| Peaking | 509 Hz   | 2.33 | -2.5 dB  |
| Peaking | 1091 Hz  | 1.28 | 4.9 dB   |
| Peaking | 1675 Hz  | 1.01 | -3.8 dB  |
| Peaking | 2656 Hz  | 2.66 | 4.7 dB   |
| Peaking | 3828 Hz  | 3.6  | -1.5 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-7.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.9 dB  |
| Peaking | 62 Hz    | 1.41 | 1.2 dB  |
| Peaking | 125 Hz   | 1.41 | -4.6 dB |
| Peaking | 250 Hz   | 1.41 | -8.4 dB |
| Peaking | 500 Hz   | 1.41 | -6.7 dB |
| Peaking | 1000 Hz  | 1.41 | 1.7 dB  |
| Peaking | 2000 Hz  | 1.41 | -1.7 dB |
| Peaking | 4000 Hz  | 1.41 | -3.0 dB |
| Peaking | 8000 Hz  | 1.41 | -3.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.5 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC33iS/Audio-Technica%20ATH-ANC33iS.png)