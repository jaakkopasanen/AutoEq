# Audio-Technica ATH-ANC9
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.5; 23 -10.9; 25 -11.2; 28 -11.5; 31 -11.6; 34 -11.4; 37 -11.2; 41 -10.9; 45 -10.5; 49 -10.1; 54 -9.7; 60 -9.3; 66 -9.2; 72 -9.2; 79 -9.4; 87 -9.8; 96 -10.3; 106 -10.9; 116 -11.3; 128 -11.6; 141 -11.7; 155 -11.4; 170 -10.8; 187 -10.1; 206 -9.2; 227 -8.4; 249 -7.6; 274 -7.1; 302 -6.7; 332 -6.4; 365 -5.9; 402 -5.7; 442 -5.6; 486 -5.6; 535 -5.6; 588 -5.2; 647 -4.1; 712 -2.4; 783 -1.2; 861 -0.5; 947 -1.6; 1042 -4.1; 1146 -6.3; 1261 -8.0; 1387 -8.5; 1526 -8.6; 1678 -8.2; 1846 -8.2; 2031 -7.9; 2234 -7.7; 2457 -7.4; 2703 -7.9; 2973 -8.2; 3270 -8.4; 3597 -8.8; 3957 -10.6; 4353 -10.1; 4788 -11.9; 5267 -12.7; 5793 -12.1; 6373 -9.4; 7010 -8.7; 7711 -9.0; 8482 -7.0; 9330 -3.1; 10263 -3.0; 11289 -6.2; 12418 -13.0; 13660 -15.2; 15026 -12.6; 16529 -9.6; 18182 -8.5; 20000 -6.6
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Audio-Technica ATH-ANC9 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio-Technica ATH-ANC9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **--0.4dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.64 | -8.1 dB  |
| Peaking | 145 Hz   | 0.75 | -7.8 dB  |
| Peaking | 1683 Hz  | 1.67 | -5.1 dB  |
| Peaking | 4938 Hz  | 1.26 | -8.9 dB  |
| Peaking | 14428 Hz | 1.47 | -12.0 dB |
| Peaking | 848 Hz   | 2.51 | 8.0 dB   |
| Peaking | 856 Hz   | 0.99 | -3.7 dB  |
| Peaking | 7833 Hz  | 5.26 | -2.3 dB  |
| Peaking | 9943 Hz  | 3.81 | 5.3 dB   |
| Peaking | 19156 Hz | 0.93 | -3.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 1.41 | -9.2 dB  |
| Peaking | 62 Hz    | 1.41 | -3.1 dB  |
| Peaking | 125 Hz   | 1.41 | -7.9 dB  |
| Peaking | 250 Hz   | 1.41 | -3.5 dB  |
| Peaking | 500 Hz   | 1.41 | -0.9 dB  |
| Peaking | 1000 Hz  | 1.41 | 0.8 dB   |
| Peaking | 2000 Hz  | 1.41 | -4.5 dB  |
| Peaking | 4000 Hz  | 1.41 | -7.0 dB  |
| Peaking | 8000 Hz  | 1.41 | -3.4 dB  |
| Peaking | 16000 Hz | 1.41 | -12.1 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Audio-Technica%20ATH-ANC9/Audio-Technica%20ATH-ANC9.png)