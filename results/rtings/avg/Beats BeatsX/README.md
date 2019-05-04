# Beats BeatsX
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -10.1; 23 -10.1; 25 -10.1; 28 -10.0; 31 -10.0; 34 -10.0; 37 -10.0; 41 -10.0; 45 -10.1; 49 -10.0; 54 -10.0; 60 -10.1; 66 -10.1; 72 -10.1; 79 -9.9; 87 -9.6; 96 -9.2; 106 -8.8; 116 -8.5; 128 -8.1; 141 -7.6; 155 -7.2; 170 -6.7; 187 -6.2; 206 -5.8; 227 -5.3; 249 -5.2; 274 -5.2; 302 -5.1; 332 -4.9; 365 -4.7; 402 -4.6; 442 -4.6; 486 -4.5; 535 -4.4; 588 -4.4; 647 -4.4; 712 -4.6; 783 -4.9; 861 -5.6; 947 -6.4; 1042 -7.2; 1146 -7.8; 1261 -8.0; 1387 -8.1; 1526 -8.1; 1678 -8.1; 1846 -8.4; 2031 -8.7; 2234 -8.7; 2457 -8.0; 2703 -6.4; 2973 -3.6; 3270 -1.3; 3597 -0.5; 3957 -0.6; 4353 -1.1; 4788 -2.6; 5267 -4.5; 5793 -4.8; 6373 -2.7; 7010 -2.9; 7711 -5.0; 8482 -5.3; 9330 -5.8; 10263 -9.6; 11289 -10.8; 12418 -12.6; 13660 -12.2; 15026 -6.6; 16529 -5.3; 18182 -6.3; 20000 -9.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Beats BeatsX GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beats BeatsX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-3.7dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 43 Hz    | 0.35 | -5.2 dB  |
| Peaking | 1325 Hz  | 0.87 | -11.3 dB |
| Peaking | 1827 Hz  | 0.38 | 10.4 dB  |
| Peaking | 2249 Hz  | 2.05 | -8.1 dB  |
| Peaking | 12377 Hz | 1.6  | -8.6 dB  |
| Peaking | 2731 Hz  | 6.12 | -1.9 dB  |
| Peaking | 3728 Hz  | 1.95 | 2.0 dB   |
| Peaking | 5488 Hz  | 3.52 | -3.2 dB  |
| Peaking | 6666 Hz  | 8    | 2.3 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-5.3dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -4.7 dB |
| Peaking | 62 Hz    | 1.41 | -4.1 dB |
| Peaking | 125 Hz   | 1.41 | -2.3 dB |
| Peaking | 250 Hz   | 1.41 | 0.5 dB  |
| Peaking | 500 Hz   | 1.41 | 1.6 dB  |
| Peaking | 1000 Hz  | 1.41 | -1.0 dB |
| Peaking | 2000 Hz  | 1.41 | -4.7 dB |
| Peaking | 4000 Hz  | 1.41 | 5.9 dB  |
| Peaking | 8000 Hz  | 1.41 | -1.5 dB |
| Peaking | 16000 Hz | 1.41 | -3.9 dB |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Beats%20BeatsX/Beats%20BeatsX.png)