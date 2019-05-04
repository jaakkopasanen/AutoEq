# Audio-Technica ATH-ANC70
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.0; 23 -1.7; 25 -1.6; 28 -1.4; 31 -1.2; 34 -1.1; 37 -1.1; 41 -1.1; 45 -1.2; 49 -1.4; 54 -1.6; 60 -1.9; 66 -2.3; 72 -2.6; 79 -3.1; 87 -3.6; 96 -4.2; 106 -4.7; 116 -5.2; 128 -5.7; 141 -6.0; 155 -6.3; 170 -6.5; 187 -6.5; 206 -6.5; 227 -6.6; 249 -6.5; 274 -6.3; 302 -6.2; 332 -6.1; 365 -5.8; 402 -5.5; 442 -5.2; 486 -4.8; 535 -4.4; 588 -4.0; 647 -3.9; 712 -4.3; 783 -5.4; 861 -6.8; 947 -8.3; 1042 -10.2; 1146 -12.0; 1261 -12.9; 1387 -12.6; 1526 -11.5; 1678 -10.4; 1846 -10.4; 2031 -10.6; 2234 -9.9; 2457 -10.0; 2703 -10.1; 2973 -10.7; 3270 -10.8; 3597 -8.9; 3957 -6.4; 4353 -4.1; 4788 -1.9; 5267 -0.5; 5793 -1.9; 6373 -4.3; 7010 -4.0; 7711 -6.2; 8482 -6.4; 9330 -6.4; 10263 -6.4; 11289 -9.9; 12418 -12.0; 13660 -12.1; 15026 -11.5; 16529 -8.1; 18182 -9.2; 20000 -21.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC70 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC70 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-5.8dB**.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.59 | 5.7 dB  |
| Peaking | 1312 Hz  | 2.78 | -6.4 dB |
| Peaking | 3055 Hz  | 1.24 | -5.8 dB |
| Peaking | 5103 Hz  | 1.54 | 8.2 dB  |
| Peaking | 20782 Hz | 0.08 | -5.7 dB |
| Peaking | 646 Hz   | 1.87 | 3.4 dB  |
| Peaking | 1045 Hz  | 2.44 | -1.6 dB |
| Peaking | 6984 Hz  | 3.02 | 0.5 dB  |
| Peaking | 10512 Hz | 2.48 | 3.4 dB  |
| Peaking | 12171 Hz | 2.95 | -3.6 dB |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-6.7dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 5.5 dB  |
| Peaking | 62 Hz    | 1.41 | 3.8 dB  |
| Peaking | 125 Hz   | 1.41 | 0.1 dB  |
| Peaking | 250 Hz   | 1.41 | -1.1 dB |
| Peaking | 500 Hz   | 1.41 | 3.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -2.8 dB |
| Peaking | 2000 Hz  | 1.41 | -5.8 dB |
| Peaking | 4000 Hz  | 1.41 | 2.0 dB  |
| Peaking | 8000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 16000 Hz | 1.41 | -6.5 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC70/Audio-Technica%20ATH-ANC70.png)