# Oppo PM3
See [usage instructions](https://github.com/jaakkopasanen/AutoEq#usage) for more options and info.

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
GraphicEQ: 21 -2.7; 23 -2.5; 25 -2.3; 28 -2.0; 31 -1.7; 34 -1.4; 37 -1.2; 41 -1.1; 45 -1.0; 49 -0.9; 54 -1.1; 60 -1.4; 66 -2.0; 72 -2.6; 79 -3.2; 87 -3.8; 96 -4.3; 106 -4.7; 116 -5.1; 128 -5.4; 141 -5.6; 155 -5.7; 170 -5.5; 187 -5.3; 206 -4.8; 227 -4.3; 249 -3.8; 274 -3.2; 302 -2.6; 332 -2.2; 365 -2.0; 402 -2.2; 442 -2.5; 486 -3.1; 535 -3.6; 588 -4.2; 647 -4.2; 712 -3.8; 783 -3.1; 861 -2.3; 947 -1.5; 1042 -1.3; 1146 -2.3; 1261 -3.2; 1387 -3.7; 1526 -4.2; 1678 -4.6; 1846 -5.6; 2031 -5.5; 2234 -6.2; 2457 -5.8; 2703 -5.7; 2973 -5.4; 3270 -4.9; 3597 -4.5; 3957 -4.0; 4353 -4.5; 4788 -2.9; 5267 -1.1; 5793 -0.5; 6373 -4.5; 7010 -9.3; 7711 -10.5; 8482 -12.1; 9330 -11.8; 10263 -6.2; 11289 -1.4; 12418 -1.6; 13660 -4.0; 15026 -2.3; 16529 -1.2; 18182 -1.2; 20000 -3.8
```

### HeSuVi
HeSuVi 2.0 ships with most of the pre-processed results. If this model can't be found in HeSuVi add
`Oppo PM3 GraphicEQ.txt` to `C:\Program Files\EqualizerAPO\config\HeSuVi\eq\custom\` folder.

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Oppo PM3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of **-0.1dB**.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 148 Hz   | 0.97 | -4.7 dB  |
| Peaking | 616 Hz   | 3.04 | -2.7 dB  |
| Peaking | 2327 Hz  | 1.16 | -4.9 dB  |
| Peaking | 8528 Hz  | 2.59 | -12.1 dB |
| Peaking | 14076 Hz | 6.63 | -2.3 dB  |
| Peaking | 18 Hz    | 2.53 | -1.2 dB  |
| Peaking | 1005 Hz  | 7.34 | 1.4 dB   |
| Peaking | 5729 Hz  | 3.89 | 8.1 dB   |
| Peaking | 6183 Hz  | 1.76 | -4.6 dB  |
| Peaking | 11487 Hz | 5.61 | 3.2 dB   |

### Fixed Band EQs
In case of using fixed band (also called graphic) equalizer, apply preamp of **-0.5dB** and set
gains manually with these parameters.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | -0.4 dB |
| Peaking | 62 Hz    | 1.41 | 0.5 dB  |
| Peaking | 125 Hz   | 1.41 | -4.7 dB |
| Peaking | 250 Hz   | 1.41 | -1.3 dB |
| Peaking | 500 Hz   | 1.41 | -1.7 dB |
| Peaking | 1000 Hz  | 1.41 | 0.4 dB  |
| Peaking | 2000 Hz  | 1.41 | -5.0 dB |
| Peaking | 4000 Hz  | 1.41 | 0.2 dB  |
| Peaking | 8000 Hz  | 1.41 | -9.1 dB |
| Peaking | 16000 Hz | 1.41 | 0.1 dB  |

### Impulse Response
In case of using Viper4Android or other convolution engine select WAV file with correct sampling frequency.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/rtings/avg/Oppo%20PM3/Oppo%20PM3.png)