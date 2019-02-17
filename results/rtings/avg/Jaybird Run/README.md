# Jaybird Run
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -3.3; 23 -3.4; 25 -3.4; 28 -3.4; 31 -3.4; 34 -3.4; 37 -3.4; 41 -3.4; 45 -3.4; 49 -3.4; 54 -3.5; 60 -3.9; 66 -4.2; 72 -4.4; 79 -4.7; 87 -5.1; 96 -5.4; 106 -5.8; 116 -6.2; 128 -6.5; 141 -6.9; 155 -7.4; 170 -7.6; 187 -7.7; 206 -7.4; 227 -7.1; 249 -6.6; 274 -6.2; 302 -5.7; 332 -5.2; 365 -4.7; 402 -4.2; 442 -3.6; 486 -3.0; 535 -2.4; 588 -1.8; 647 -1.1; 712 -0.6; 783 -0.5; 861 -0.9; 947 -1.6; 1042 -2.5; 1146 -3.3; 1261 -4.0; 1387 -4.2; 1526 -4.6; 1678 -5.1; 1846 -5.8; 2031 -6.5; 2234 -6.8; 2457 -6.7; 2703 -5.8; 2973 -4.4; 3270 -3.0; 3597 -2.0; 3957 -1.4; 4353 -1.1; 4788 -0.8; 5267 -1.2; 5793 -2.9; 6373 -7.7; 7010 -11.9; 7711 -7.9; 8482 -4.4; 9330 -6.3; 10263 -7.2; 11289 -2.6; 12418 -2.1; 13660 -2.1; 15026 -2.1; 16529 -2.1; 18182 -2.1; 20000 -2.1
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Jaybird Run GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Jaybird Run ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-1.8dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 176 Hz   | 0.58 | -5.4 dB  |
| Peaking | 713 Hz   | 1.99 | 2.9 dB   |
| Peaking | 2104 Hz  | 1.85 | -4.9 dB  |
| Peaking | 7122 Hz  | 4.43 | -10.1 dB |
| Peaking | 21198 Hz | 2.2  | -2.3 dB  |
| Peaking | 25 Hz    | 1.28 | -1.1 dB  |
| Peaking | 2691 Hz  | 3.66 | -1.9 dB  |
| Peaking | 5519 Hz  | 0.99 | 2.9 dB   |
| Peaking | 6572 Hz  | 6.01 | -4.1 dB  |
| Peaking | 9892 Hz  | 4.65 | -5.9 dB  |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-1.2dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -1.2 dB |
| Peaking | 62 Hz    | 1.41 | -0.8 dB |
| Peaking | 125 Hz   | 1.41 | -4.0 dB |
| Peaking | 250 Hz   | 1.41 | -4.7 dB |
| Peaking | 500 Hz   | 1.41 | 0.6 dB  |
| Peaking | 1000 Hz  | 1.41 | 1.6 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.7 dB |
| Peaking | 4000 Hz  | 1.41 | 2.7 dB  |
| Peaking | 8000 Hz  | 1.41 | -6.4 dB |
| Peaking | 16000 Hz | 1.41 | 0.8 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Jaybird%20Run/Jaybird%20Run.png)